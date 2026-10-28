import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import numpy as np
import os
from datetime import datetime

print("=" * 60)
print("ML MODEL RETRAINING - COMBINED DATASET (OLD + 2025)")
print("=" * 60)

# Load both datasets
print("\n[1/7] Loading datasets...")
old_data = pd.read_csv("tnea_cutoff_clean.csv")
new_data = pd.read_csv("tnea_cutoff_2025.csv")

print(f"   Old dataset: {len(old_data)} records")
print(f"   New dataset: {len(new_data)} records")

# Combine datasets
combined_data = pd.concat([old_data, new_data], ignore_index=True)
print(f"   Combined dataset: {len(combined_data)} records")

# Prepare data
print("\n[2/7] Preparing data...")
category_columns = ["OC", "BC", "BCM", "MBC", "SC", "SCA", "ST"]

long_data = combined_data.melt(
    id_vars=["college_code", "college", "branch"],
    value_vars=category_columns,
    var_name="Category",
    value_name="Required_Cutoff"
)

long_data = long_data.dropna()
print(f"   Total records after processing: {len(long_data)}")

# Generate training samples
print("\n[3/7] Generating training samples...")
X_list = []
y_list = []

for _, row in long_data.iterrows():
    required_cutoff = row["Required_Cutoff"]
    category = row["Category"]
    
    # Positive samples (admission likely)
    for _ in range(3):
        student_cutoff = required_cutoff + np.random.uniform(0, 10)
        X_list.append({
            "Student_Cutoff": student_cutoff,
            "Required_Cutoff": required_cutoff,
            f"Category_{category}": 1
        })
        y_list.append(1)
    
    # Negative samples (admission unlikely)
    for _ in range(2):
        student_cutoff = required_cutoff - np.random.uniform(5, 20)
        X_list.append({
            "Student_Cutoff": student_cutoff,
            "Required_Cutoff": required_cutoff,
            f"Category_{category}": 1
        })
        y_list.append(0)

# Create DataFrame
X = pd.DataFrame(X_list).fillna(0)
y = np.array(y_list)

print(f"   Training samples: {len(X)}")
print(f"   Positive samples: {sum(y)}")
print(f"   Negative samples: {len(y) - sum(y)}")

# Split data
print("\n[4/7] Splitting data...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"   Training set: {len(X_train)} samples")
print(f"   Test set: {len(X_test)} samples")

# Train model
print("\n[5/7] Training Random Forest model...")
model = RandomForestClassifier(n_estimators=100, random_state=42, max_depth=10)
model.fit(X_train, y_train)

# Evaluate
print("\n[6/7] Evaluating model...")
train_accuracy = model.score(X_train, y_train)
test_accuracy = model.score(X_test, y_test)
print(f"   Training Accuracy: {train_accuracy * 100:.2f}%")
print(f"   Test Accuracy: {test_accuracy * 100:.2f}%")

# Backup old model
print("\n[7/7] Saving model...")
if os.path.exists("college_model.pkl"):
    backup_name = f"college_model_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pkl"
    os.rename("college_model.pkl", backup_name)
    print(f"   Old model backed up as: {backup_name}")

# Save new model
with open("college_model.pkl", "wb") as f:
    pickle.dump(model, f)
print("   New model saved as: college_model.pkl")

# Update combined dataset
combined_data.to_csv("tnea_cutoff_combined.csv", index=False)
print("   Combined dataset saved as: tnea_cutoff_combined.csv")

# Test prediction
print("\n" + "=" * 60)
print("MODEL TESTING")
print("=" * 60)
test_input = pd.DataFrame([{
    "Student_Cutoff": 195,
    "Required_Cutoff": 190,
    "Category_OC": 1,
    "Category_BC": 0,
    "Category_BCM": 0,
    "Category_MBC": 0,
    "Category_SC": 0,
    "Category_SCA": 0,
    "Category_ST": 0
}])

probability = model.predict_proba(test_input)[0][1]
print(f"\nTest Case:")
print(f"  Student Cutoff: 195")
print(f"  Required Cutoff: 190")
print(f"  Category: OC")
print(f"  Admission Probability: {probability * 100:.2f}%")

print("\n" + "=" * 60)
print("RETRAINING COMPLETED SUCCESSFULLY!")
print("=" * 60)
print("\nNext Steps:")
print("1. Restart your Flask server (python server.py)")
print("2. The new model will automatically be used")
print("3. Combined dataset has more data = better predictions!")
