
B =   ['2', '+', '2', '*', '2', '+', '2', '*', '2']
priority = {
    '+':1,
    '-':1,
    '*':2,
    '/':2
}
oper = ['+', '*', '-', '/']

def stack_is_empty(stack):
    if len(stack) == 0:
        return True
    return False

def get_stack(string_ex):
    rs = []
    collect_str = ''
    for item in string_ex:
        if item in oper:
            rs.append(collect_str)
            rs.append(item)
            collect_str = ''
        else:
            collect_str+= item
    rs.append(collect_str)
    return rs

def calc_dat_shit(s1, c1, c2, item):
    if item == '+':
        s1.append(c1+c2)
    if item == '*':
        s1.append(c1*c2)
    if item == '-':
        s1.append(c1-c2)
    if item == '/':
        s1.append(c2/c1)
    return s1

def c(input):
    s1 = []
    s2 = []

    for item in input:
        print(s1)
        if item in oper:
            if stack_is_empty(s2):
                s2.append(item)

            else:
                if item == '(' or item == ')':
                    if item == '(':
                        s2.append(item)
                    if item == ')':
                        curop = item
                        while curop!= '(':
                            c1 = int(s1.pop())
                            c2 = int(s1.pop())
                            curop =  s2.pop()
                            
                            s1 = calc_dat_shit(s1, c1, c2, curop)
                    pass
                elif priority[s2[-1]] > priority[item] or (priority[s2[-1]] == priority[item] and priority[item] == 2):
                    c1 = int(s1.pop())
                    c2 = int(s1.pop())
                    op =  s2.pop()
                    s2.append(item)

                    s1 = calc_dat_shit(s1, c1, c2, op)

                else:
                    s2.append(item)
                    pass
                pass
            pass

        else:
            s1.append(item)
            pass

        pass

    while not stack_is_empty(s2):
        if not stack_is_empty(s1):
            c1 = int(s1.pop())
            c2 = int(s1.pop())
            item = s2.pop()

            s1 = calc_dat_shit(s1, c1, c2, item)


    return s1
    pass

while 1:
    s = input('enter calcer: ')
    b = get_stack(s)
    a = c(b)
    print(b, s, "=",a)
