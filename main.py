
<<<<<<< HEAD
B =   ['2', '+', '2', '*', '2', '+', '2']
=======
B =   ['2', '+', '2', '*', '2', '+', '2', '*', '2']
>>>>>>> b276f3d1e5af31c05e4315225d08ed12508e2989
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
<<<<<<< HEAD
                if priority[item] < priority[s2[-1]]:
=======

                if priority[s2[-1]] > priority[item] and len(s1) >= 2:
                    c1 = int(s1.pop())
                    c2 = int(s1.pop())
                    s1 = calc_dat_shit(s1, c1, c2, item)
                    s1.append(item)

                if priority[s2[-1]] < priority[item]:
>>>>>>> b276f3d1e5af31c05e4315225d08ed12508e2989
                    c1 = int(s1.pop())
                    c2 = int(s1.pop())
                    op = s2.pop()
                    s2.append(item)

<<<<<<< HEAD
                    if op == '+':
                        s1.append(c1+c2)
                    if op == '*':
                        s1.append(c1*c2)
=======
                    s1 = calc_dat_shit(s1, c1, c2, item)

                elif priority[s2[-1]] == priority[item]:
                    c1 = int(s1.pop())
                    c2 = int(s1.pop())

                    s1 = calc_dat_shit(s1, c1, c2, item)
                    pass
>>>>>>> b276f3d1e5af31c05e4315225d08ed12508e2989
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

            s1 = calc_dat_shit(s1, c1, c2, item)


    return s1
    pass

<<<<<<< HEAD
c(B)
=======
while 1:
    s = input('enter calcer: ')
    b = get_stack(s)
    a = c(b)
    print(b, s, "=",a)
>>>>>>> b276f3d1e5af31c05e4315225d08ed12508e2989
