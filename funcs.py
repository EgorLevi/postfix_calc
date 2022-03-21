def get_array_from_string(str_inputed):
    a =[]
    temsrt = ""
    opers = ['+','-','/','*']
    for item in str_inputed:
        
        if item in opers:
            a.append(temsrt)
            a.append(item)
            temsrt = ""
        else:
            temsrt += item
    a.append(temsrt)
    return a

print(get_array_from_string(input("#: ")))

def calculate(s1, s2, op):
        # get items from stack and cal it
        f1 = int(s1.pop())
        f2 = int(s1.pop())
        if op == '+':
            s1.append(f1+f2)
        if op == '*':
            s1.append(f1*f)

        return s1

