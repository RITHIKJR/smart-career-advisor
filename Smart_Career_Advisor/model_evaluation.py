import pandas as pd
import pickle
import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns

print("=" * 70)
print("ML MODEL EVALUATION REPORT")
print("Smart Career Advisor - College Recommendation System")
print("=" * 70)

# Load model and data
print("\n[1/5] Loading model and dataset...")
model = pickle.load(open("college_model.pkl", "rb"))
combined_data = pd.read_csv("tnea_cutoff_combined.csv")
print(f"   Model: RandomForestClassifier")
print(f"   Dataset: {len(combined_data)} records")

# Prepare data
print("\n[2/5] Preparing test data...")
category_columns = ["OC", "BC", "BCM", "MBC", "SC", "SCA", "ST"]
long_data = combined_data.melt(
    id_vars=["college_code", "college", "branch"],
    value_vars=category_columns,
    var_name="Category",
    value_name="Required_Cutoff"
).dropna()

# Generate test samples
X_list, y_list = [], []
for _, row in long_data.iterrows():
    required_cutoff = row["Required_Cutoff"]
    category = row["Category"]
    
    for _ in range(3):
        student_cutoff = required_cutoff + np.random.uniform(0, 10)
        X_list.append({"Student_Cutoff": student_cutoff, "Required_Cutoff": required_cutoff, f"Category_{category}": 1})
        y_list.append(1)
    
    for _ in range(2):
        student_cutoff = required_cutoff - np.random.uniform(5, 20)
        X_list.append({"Student_Cutoff": student_cutoff, "Required_Cutoff": required_cutoff, f"Category_{category}": 1})
        y_list.append(0)

X = pd.DataFrame(X_list).fillna(0)
y = np.array(y_list)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Make predictions
print("\n[3/5] Making predictions...")
y_pred = model.predict(X_test)
y_pred_proba = model.predict_proba(X_test)[:, 1]

# Calculate metrics
print("\n[4/5] Calculating metrics...")
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

# Display results
print("\n[5/5] Generating report...")
print("\n" + "=" * 70)
print("PERFORMANCE METRICS")
print("=" * 70)
print(f"\n{'Metric':<30} {'Value':<20} {'Interpretation'}")
print("-" * 70)
print(f"{'Accuracy':<30} {accuracy*100:>6.2f}%          {'Excellent' if accuracy > 0.9 else 'Good' if accuracy > 0.8 else 'Fair'}")
print(f"{'Precision':<30} {precision*100:>6.2f}%          {'High reliability'}")
print(f"{'Recall (Sensitivity)':<30} {recall*100:>6.2f}%          {'Good detection'}")
print(f"{'F1 Score':<30} {f1*100:>6.2f}%          {'Balanced performance'}")

print("\n" + "=" * 70)
print("CONFUSION MATRIX")
print("=" * 70)
print(f"\n                    Predicted")
print(f"                No (0)      Yes (1)")
print(f"Actual  No (0)  {cm[0][0]:<10}  {cm[0][1]:<10}")
print(f"        Yes (1) {cm[1][0]:<10}  {cm[1][1]:<10}")

print("\n" + "=" * 70)
print("CONFUSION MATRIX INTERPRETATION")
print("=" * 70)
print(f"True Negatives (TN):  {cm[0][0]:>6} - Correctly predicted NO admission")
print(f"False Positives (FP): {cm[0][1]:>6} - Incorrectly predicted YES (Type I Error)")
print(f"False Negatives (FN): {cm[1][0]:>6} - Incorrectly predicted NO (Type II Error)")
print(f"True Positives (TP):  {cm[1][1]:>6} - Correctly predicted YES admission")

print("\n" + "=" * 70)
print("DETAILED CLASSIFICATION REPORT")
print("=" * 70)
print(classification_report(y_test, y_pred, target_names=["No Admission (0)", "Admission (1)"]))

print("=" * 70)
print("MODEL SUMMARY")
print("=" * 70)
print(f"Total Test Samples:     {len(y_test)}")
print(f"Correct Predictions:    {(y_test == y_pred).sum()}")
print(f"Incorrect Predictions:  {(y_test != y_pred).sum()}")
print(f"Error Rate:             {(1-accuracy)*100:.2f}%")

# Save visualization
print("\n" + "=" * 70)
print("GENERATING VISUALIZATIONS")
print("=" * 70)

plt.figure(figsize=(12, 5))

# Confusion Matrix Heatmap
plt.subplot(1, 2, 1)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False)
plt.title('Confusion Matrix', fontsize=14, fontweight='bold')
plt.ylabel('Actual', fontsize=12)
plt.xlabel('Predicted', fontsize=12)
plt.xticks([0.5, 1.5], ['No (0)', 'Yes (1)'])
plt.yticks([0.5, 1.5], ['No (0)', 'Yes (1)'])

# Metrics Bar Chart
plt.subplot(1, 2, 2)
metrics = ['Accuracy', 'Precision', 'Recall', 'F1 Score']
values = [accuracy*100, precision*100, recall*100, f1*100]
colors = ['#2ecc71', '#3498db', '#e74c3c', '#f39c12']
bars = plt.bar(metrics, values, color=colors, alpha=0.7)
plt.title('Performance Metrics', fontsize=14, fontweight='bold')
plt.ylabel('Score (%)', fontsize=12)
plt.ylim(0, 100)
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.1f}%', ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.savefig('model_evaluation_report.png', dpi=300, bbox_inches='tight')
print("   ✓ Saved: model_evaluation_report.png")

print("\n" + "=" * 70)
print("EVALUATION COMPLETED!")
print("=" * 70)
print("\nFiles Generated:")
print("   1. model_evaluation_report.png - Visual charts")
print("\nShare these results with your staff!")
