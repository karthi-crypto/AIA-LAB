
rules = [
    {"if":{"fever","cough","fatigue"},"then":"Flu"},
    {"if":{"fever","cough","shortness of breath"},"then":"COVID-19"},
    {"if":{"headache","nausea","Sensitive to light"},"then":"Migraine"},
    {"if":{"sore throat","running nose","sneezing"},"then":"Common cold"},
    {"if":{"chest pain","shortness of breath","dizziness"},"then":"Heart Attack"}
]
def diseases(symptoms):
    symptom_set=set(symptoms)
    diseases_list = []
    for rule in rules:
        if rule["if"].issubset(symptom_set):
            diseases_list.append(rule["then"])
    return diseases_list
def main():
    print(f"Welcome to the Forward chaining Medical expert System")
    print(f"Enter your Symptoms as commas-separated(eg fever,cold)")
    user_i = input("Symptoms: ").lower()
    symptoms = [s.strip() for s in user_i.split(",")]
    diagnose=diseases(symptoms)
    if diagnose:
        for disease in diagnose:
            print(f"- {disease}")
    else:
        print("No diagnosis")
if __name__ == "__main__":
    main()