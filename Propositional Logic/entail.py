import re
def pl_true(expr, model):
    if isinstance(expr, str): 
        return model[expr]
    elif isinstance(expr, tuple):
        op = expr[0]
        if op == "not":
            return not pl_true(expr[1], model)
        elif op == "and":
            return pl_true(expr[1], model) and pl_true(expr[2], model)
        elif op == "or":
            return pl_true(expr[1], model) or pl_true(expr[2], model)
        elif op == "implies":
            return (not pl_true(expr[1], model)) or pl_true(expr[2], model)
    return False

def tt_entails(KB, query):
    symbols = list(get_symbols(KB) | get_symbols(query))
    return check_all(KB, query, symbols, {})

def get_symbols(expr):
    if isinstance(expr, str):
        return {expr}
    elif isinstance(expr, tuple):
        return get_symbols(expr[1]) | (get_symbols(expr[2]) if len(expr) > 2 else set())
    return set()

def check_all(KB, query, symbols, model):
    if not symbols:
        if pl_true(KB, model):
            return pl_true(query, model)
        else:
            return True
    else:
        rest = symbols[1:]
        p = symbols[0]
        m1 = model.copy(); m1[p] = True
        m2 = model.copy(); m2[p] = False
        return check_all(KB, query, rest, m1) and check_all(KB, query, rest, m2)


precedence = {
    'not': 3,
    'and': 2,
    'or': 1,
    'implies': 0
}

def infix_to_expr(infix_str):
    # Replace common symbols with standard keywords
    infix_str = infix_str.replace("¬", "not").replace("~", "not")
    infix_str = infix_str.replace("∧", "and").replace("&", "and")
    infix_str = infix_str.replace("∨", "or").replace("|", "or")
    infix_str = infix_str.replace("→", "implies").replace("->", "implies")

    tokens = re.findall(r'[A-Za-z]+|not|and|or|implies|\(|\)', infix_str)

    output = []
    ops = []

    def pop_op():
        op = ops.pop()
        if op == "not":
            right = output.pop()
            output.append((op, right))
        else:
            right = output.pop()
            left = output.pop()
            output.append((op, left, right))

    for token in tokens:
        if re.fullmatch(r'[A-Za-z]+', token):  # symbol
            output.append(token)
        elif token == '(':
            ops.append(token)
        elif token == ')':
            while ops and ops[-1] != '(':
                pop_op()
            ops.pop()  # remove '('
        elif token in precedence:
            while (ops and ops[-1] in precedence and
                   precedence[ops[-1]] >= precedence[token]):
                pop_op()
            ops.append(token)

    while ops:
        pop_op()

    return output[0]


print("Name: Sohan R")
print("USN : 1BM23CS336")

print("\nEnter logical expressions using standard infix notation.")
print("Supported operators: ¬ or ~ (not), ∧ or & (and), ∨ or | (or), → or -> (implies)")
print("Example KB   : (A ∨ C) ∧ (B ∨ ¬C)")
print("Example Query: A ∨ B")

KB_infix = input("Enter Knowledge Base (KB): ")
query_infix = input("Enter Query: ")

try:
    KB = infix_to_expr(KB_infix)
    query = infix_to_expr(query_infix)

    result = tt_entails(KB, query)

    print("\nParsed KB   :", KB)
    print("Parsed Query:", query)
    print("Does KB entail Query? :", "YES" if result else "NO")

except Exception as e:
    print("Error in parsing expression:", str(e))
