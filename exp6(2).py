from kanren import Relation, facts, run, var

# Define relations
doctor = Relation()
treats = Relation()

# Add facts to the knowledge base
facts(doctor,
      ("dr_smith",),
      ("dr_jones",),
      ("dr_lee",),
      ("dr_williams",),
      ("dr_davis",))

facts(treats,
      ("dr_smith", "flu"),
      ("dr_smith", "allergy"),
      ("dr_jones", "cold"),
      ("dr_lee", "covid"),
      ("dr_lee", "pneumonia"),
      ("dr_williams", "diabetes"),
      ("dr_davis", "hypertension"))

# Query function: find all doctors who treat a given disease
def find_doctors_treating(disease):
    x = var()
    return run(0, x, treats(x, disease))

# Example usage: find doctors treating 'flu'
if __name__ == "__main__":
    disease = input("Enter disease to find doctors who treat it: ").strip().lower()
    doctors = find_doctors_treating(disease)
    if doctors:
        print(f"Doctors who treat {disease}:")
        for doc in doctors:
            print(f"- {doc.replace('_', ' ').title()}")
    else:
        print(f"No doctors found treating {disease}.")
