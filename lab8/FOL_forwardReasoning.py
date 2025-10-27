name = "Sohan R"
usn = "1BM21CS000"

KB = [
    "American(Robert)",
    "Enemy(A, America)",
    "Missile(T1)",
    "Owns(A, T1)"
]

rules = [
    {"name": "R1", "if": ["American(p)", "Weapon(q)", "Sells(p, q, r)", "Hostile(r)"], "then": "Criminal(p)"},
    {"name": "R2", "if": ["Missile(x)"], "then": "Weapon(x)"},
    {"name": "R3", "if": ["Missile(x)", "Owns(A, x)"], "then": "Sells(Robert, x, A)"},
    {"name": "R4", "if": ["Enemy(x, America)"], "then": "Hostile(x)"}
]

def match(pattern, fact):
    return pattern.split("(")[0] == fact.split("(")[0]

def condition_satisfied(cond, KB):
    return any(match(cond, fact) for fact in KB)

def substitute(statement, mapping=None):
    if not mapping:
        mapping = {"p": "Robert", "r": "A", "q": "T1", "x": "T1"}
    for var, val in mapping.items():
        statement = statement.replace(var, val)
    return statement

def forward_chaining(KB, rules):
    inferred = set()
    derivations = {}
    added = True
    while added:
        added = False
        for rule in rules:
            if all(condition_satisfied(cond, KB) for cond in rule["if"]):
                conclusion = substitute(rule["then"])
                if conclusion not in KB:
                    KB.append(conclusion)
                    inferred.add(conclusion)
                    derivations[conclusion] = {"rule": rule["name"], "premises": [substitute(p) for p in rule["if"]]}
                    added = True
    return KB, derivations

def print_tree(derivations, goal, level=0):
    if goal not in derivations:
        print("   " * level + f"└── {goal}")
        return
    rule_info = derivations[goal]
    print("   " * level + f"└── {goal} ← ({rule_info['rule']})")
    for premise in rule_info["premises"]:
        print_tree(derivations, premise, level + 1)

final_KB, derivations = forward_chaining(KB.copy(), rules)

print("\n==============================")
print("   FORWARD CHAINING RESULT")
print("==============================")
for fact in final_KB:
    print(f"- {fact}")

print("\n==============================")
print("      INFERENCE TREE")
print("==============================")
for conclusion in derivations:
    print_tree(derivations, conclusion)
    print()

print("------------------------------")
print(f"Name : {name}")
print(f"USN  : {usn}")
print("------------------------------")
