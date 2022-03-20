
B =   ['2', '+', '2', '*', '2', '+', '2']
priority = {
    '+':1,
    '*':2
}

def stack_is_empty(stack):
    if len(stack) == 0:
        return True
    return False

def c(input):
    s1 = []
    s2 = []
    oper = ['+', '*']

    for item in input:

        if item in oper:
            if stack_is_empty(s2):
                s2.append(item)
            else:
                if priority[item] < priority[s2[-1]]:
                    c1 = int(s1.pop())
                    c2 = int(s1.pop())
                    op = s2.pop()
                    s2.append(item)

                    if op == '+':
                        s1.append(c1+c2)
                    if op == '*':
                        s1.append(c1*c2)
                else:
                    s2.append(item)
                    pass
                pass
            pass

        else:
            s1.append(item)
            pass

        pass
    print(s1, s2)
    while not stack_is_empty(s2):
        if not stack_is_empty(s1):
            c1 = int(s1.pop())
            c2 = int(s1.pop())
            item = s2.pop()
            if item == '+':
                s1.append(c1+c2)
            if item == '*':
                s1.append(c1*c2)

    print(s1, s2)
    pass

c(B)
