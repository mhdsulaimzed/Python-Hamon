def evaluate(string):
    stack=[]
    for i in string:
        stack.append(int(i))
    return stack.pop()


