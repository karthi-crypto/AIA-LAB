def implies(p, q):
    return (not p) or q

def iff(p, q):
    return (p and q) or (not p and not q)

def evaluate_user_propositions():
    print(f"User input logical Propositions")
    n = int(input("Enter the number of propositions:"))
    propositions = {}
    for i in range(n):
        prop,val=input("Enter the propositions (True/False) propositions and its Value commas-separated (eg.. A True): ").strip().split(" ")
        propositions[prop]=val.lower()=='true'
    print(f"Propositions evaluated: {propositions}")
    print(f"logical propositions expression you may use 'and','or','not',implies','if' (eg.. A and not B")
    query=input("Enter the propositions: ")
    try:
        available_var={k: propositions.get(k, False) for k in propositions.keys()}
        available_var['implies']=implies
        available_var['iff']=iff
        result=eval(query,{"__builtins__":None},available_var)
        print(result)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    evaluate_user_propositions()