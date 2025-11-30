rules = [
    {"if": {"fever", "cough", "fatigue"}, "then": "Flu"},
    {"if": {"fever", "cough", "shortness of breath"}, "then": "COVID-19"},
    {"if": {"headache", "nausea", "sensitivity to light"}, "then": "Migraine"},
    {"if": {"sore throat", "runny nose", "sneezing"}, "then": "Common Cold"},
    {"if": {"chest pain", "shortness of breath", "dizziness"}, "then": "Heart Attack"},
]

# Inference engine: forward chaining
def diagnose(symptoms):
    matched_diseases = []
    symptoms_set = set(symptoms)
    for rule in rules:
        if symptoms_set.issubset(rule["if"]):
            matched_diseases.append(rule["then"])
    return matched_diseases

# User interface
def main():
    print("=== Forward Chaining Medical Expert System ===")
    print("Enter your symptoms separated by commas (e.g., fever, cough):")
    user_input = input("Symptoms: ").lower()
    symptoms = [s.strip() for s in user_input.split(",")]
    diagnoses = diagnose(symptoms)
    if diagnoses:
        print("\nPossible diagnosis(es):")
        for disease in diagnoses:
            print(f"- {disease}")
    else:
        print("No matching diagnosis found. Please consult a doctor.")

# Run program
if __name__ == "__main__":
    main()
