name = "Sohan R"
usn = "1BM23CS336"

def negate(clause):
    if clause.startswith("¬"):
        return clause[1:]
    else:
        return "¬" + clause

def is_complementary(lit1, lit2):
    return lit1 == negate(lit2) or lit2 == negate(lit1)

def unify(lit1, lit2):
    subs = {}
    if "(" in lit1 and "(" in lit2:
        p1, args1 = lit1.split("(")
        p2, args2 = lit2.split("(")
        args1 = args1[:-1].split(",")
        args2 = args2[:-1].split(",")
        if p1 != p2 or len(args1) != len(args2):
            return None
        for a1, a2 in zip(args1, args2):
            a1, a2 = a1.strip(), a2.strip()
            if a1 != a2:
                if a1.islower():
                    subs[a1] = a2
                elif a2.islower():
                    subs[a2] = a1
                else:
                    return None
    elif lit1 != lit2:
        return None
    return subs

def substitute(clause, subs):
    if not subs:
        return clause
    for var, val in subs.items():
        clause = clause.replace(var, val)
    return clause

def resolve(ci, cj):
    ci_literals = ci.split(" ∨ ")
    cj_literals = cj.split(" ∨ ")
    resolvents = []
    for li in ci_literals:
        for lj in cj_literals:
            subs = unify(li.replace(" ", ""), negate(lj.replace(" ", "")))
            if subs is not None or is_complementary(li.strip(), lj.strip()):
                new_ci = [substitute(x, subs) for x in ci_literals if x != li] if subs else [x for x in ci_literals if x != li]
                new_cj = [substitute(x, subs) for x in cj_literals if x != lj] if subs else [x for x in cj_literals if x != lj]
                new_clause = list(set(new_ci + new_cj))
                if not new_clause:
                    return ["NIL"]
                resolvents.append(" ∨ ".join(new_clause))
    return resolvents

def resolution(KB, query):
    clauses = KB + [negate(query)]
    derived_from = {}
    new = set()
    print("\n==============================")
    print("   RESOLUTION STEPS")
    print("==============================")
    while True:
        n = len(clauses)
        pairs = [(clauses[i], clauses[j]) for i in range(n) for j in range(i+1, n)]
        for (ci, cj) in pairs:
            resolvents = resolve(ci, cj)
            for res in resolvents:
                print(f"{ci} + {cj} ⟹ {res}")
                derived_from[res] = (ci, cj)
                if res == "NIL":
                    print("\nThe query is proven true by refutation.\n")
                    print("==============================")
                    print("        RESOLUTION TREE")
                    print("==============================")
                    print_tree("NIL", derived_from, level=0)
                    return True
                new.add(res)
        if new.issubset(set(clauses)):
            print("\nThe query cannot be proven from the KB.")
            return False
        for c in new:
            if c not in clauses:
                clauses.append(c)

def print_tree(clause, derived_from, level=0):
    print("   " * level + f"└── {clause}")
    if clause in derived_from:
        parents = derived_from[clause]
        for p in parents:
            print_tree(p, derived_from, level + 1)

KB = [
    "¬Food(x) ∨ Likes(John, x)",
    "Food(Apple)",
    "Food(Vegetable)",
    "¬Eats(x, y) ∨ ¬Killed(x) ∨ Food(y)",
    "Eats(Anil, Peanut)",
    "¬Killed(Anil)",
    "¬Alive(x) ∨ ¬Killed(x)",
    "Killed(x) ∨ Alive(x)"
]

query = "Likes(John, Peanut)"

resolution(KB, query)

print("\n------------------------------")
print(f"Name : {name}")
print(f"USN  : {usn}")
print("------------------------------")
