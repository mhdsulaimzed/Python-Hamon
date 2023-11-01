def evaluate(string):
    stack=[]
    for i in string:
        if i in ["+","-","*"]:
            opr1=stack.pop()
            opr2=stack.pop()

            if i == "+":
                stack.append(opr1+opr2)

            elif i == "-":
                stack.append(opr2-opr1)

            elif i == "*":
                stack.append(opr1*opr2)




        else:    
            stack.append(int(i))

    return stack.pop()








