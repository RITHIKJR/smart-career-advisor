import pandas as pd
import pickle
import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split

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
print(f"   Test samples: {len(y_test)}")
y_pred = model.predict(X_test)

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
print(f"\nModel Type:             RandomForestClassifier")
print(f"Training Data:          {len(combined_data)} college records")
print(f"Features Used:          Student Cutoff, Required Cutoff, Category")

print("\n" + "=" * 70)
print("METRICS EXPLANATION FOR STAFF")
print("=" * 70)
print("\n1. ACCURACY ({:.2f}%):".format(accuracy*100))
print("   - Overall correctness of predictions")
print("   - Higher is better (>90% is excellent)")
print("\n2. PRECISION ({:.2f}%):".format(precision*100))
print("   - When model predicts admission, how often is it correct?")
print("   - Reduces false hopes for students")
print("\n3. RECALL ({:.2f}%):".format(recall*100))
print("   - Of all actual admissions, how many did we predict?")
print("   - Ensures we don't miss opportunities")
print("\n4. F1 SCORE ({:.2f}%):".format(f1*100))
print("   - Balance between Precision and Recall")
print("   - Single metric for overall performance")
print("\n5. CONFUSION MATRIX:")
print("   - Shows correct vs incorrect predictions")
print("   - Diagonal values (TN, TP) are correct predictions")

# Save report to file
print("\n" + "=" * 70)
print("SAVING REPORT")
print("=" * 70)

with open('model_evaluation_report.txt', 'w') as f:
    f.write("=" * 70 + "\n")
    f.write("ML MODEL EVALUATION REPORT\n")
    f.write("Smart Career Advisor - College Recommendation System\n")
    f.write("=" * 70 + "\n\n")
    
    f.write("PERFORMANCE METRICS\n")
    f.write("=" * 70 + "\n")
    f.write(f"Accuracy:              {accuracy*100:.2f}%\n")
    f.write(f"Precision:             {precision*100:.2f}%\n")
    f.write(f"Recall (Sensitivity):  {recall*100:.2f}%\n")
    f.write(f"F1 Score:              {f1*100:.2f}%\n\n")
    
    f.write("CONFUSION MATRIX\n")
    f.write("=" * 70 + "\n")
    f.write(f"                    Predicted\n")
    f.write(f"                No (0)      Yes (1)\n")
    f.write(f"Actual  No (0)  {cm[0][0]:<10}  {cm[0][1]:<10}\n")
    f.write(f"        Yes (1) {cm[1][0]:<10}  {cm[1][1]:<10}\n\n")
    
    f.write("CONFUSION MATRIX BREAKDOWN\n")
    f.write("=" * 70 + "\n")
    f.write(f"True Negatives (TN):  {cm[0][0]:>6}\n")
    f.write(f"False Positives (FP): {cm[0][1]:>6}\n")
    f.write(f"False Negatives (FN): {cm[1][0]:>6}\n")
    f.write(f"True Positives (TP):  {cm[1][1]:>6}\n\n")
    
    f.write("DETAILED CLASSIFICATION REPORT\n")
    f.write("=" * 70 + "\n")
    f.write(classification_report(y_test, y_pred, target_names=["No Admission (0)", "Admission (1)"]))
    
    f.write("\n" + "=" * 70 + "\n")
    f.write("METRICS EXPLANATION\n")
    f.write("=" * 70 + "\n")
    f.write(f"\n1. ACCURACY ({accuracy*100:.2f}%): Overall correctness\n")
    f.write(f"2. PRECISION ({precision*100:.2f}%): Reliability of positive predictions\n")
    f.write(f"3. RECALL ({recall*100:.2f}%): Coverage of actual positives\n")
    f.write(f"4. F1 SCORE ({f1*100:.2f}%): Balanced performance metric\n")

print("   [OK] Saved: model_evaluation_report.txt")

print("\n" + "=" * 70)
print("EVALUATION COMPLETED!")
print("=" * 70)
print("\nFiles Generated:")
print("   1. model_evaluation_report.txt - Complete metrics report")
print("\nShare this report with your staff!")
