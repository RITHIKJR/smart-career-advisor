import pickle

# Load the model
model = pickle.load(open("college_model.pkl", "rb"))

print("=" * 80)
print("🤖 ML MODEL INFORMATION")
print("=" * 80)

print(f"\n📊 Model Type: {type(model).__name__}")
print(f"\n📋 Features Used:")
for i, feature in enumerate(model.feature_names_in_, 1):
    print(f"   {i}. {feature}")

print(f"\n🎯 Total Features: {len(model.feature_names_in_)}")

print("\n" + "=" * 80)
print("✅ Model loaded successfully!")
print("=" * 80)
