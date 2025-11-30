import collections
import collections.abc
collections.Iterator = collections.abc.Iterator
collections.Hashable = collections.abc.Hashable

from kanren import Relation, facts, run, var, conde

# Knowledge base: hospital scenario
doctor = Relation()
treats = Relation()

# Facts
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

# Rule: A doctor is skilled if they treat at least one disease
def is_skilled(person):
    return conde((doctor(person), treats(person, var())),)

# Take user input
query = input("Enter query: ").strip().lower()
x = var()

# "Who" query
if query.startswith("who"):
    result = run(0, x, is_skilled(x))
    if result:
        print("✓ Skilled doctors found:")
        for name in result:
            print(f"- {name.replace('_',' ').title()}")
    else:
        print("X No skilled doctors found.")

# "Is" query
elif query.startswith("is"):
    words = query.replace("?", "").split()
    if len(words) >= 3:
        name = words[1]
        result = run(0, x, is_skilled(x))
        if name in result:
            print(f"✓ Yes, {name.replace('_',' ').title()} is skilled.")
        else:
            print(f"X No, {name.replace('_',' ').title()} is not skilled.")
    else:
        print("X Invalid query format.")

else:
    print("X Invalid query format.")
