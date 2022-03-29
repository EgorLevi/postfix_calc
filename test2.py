import time

a = ['(', '2', '+', '2', '*', '2', ')', '*','(', '2', '+', '2', ')']
s1 = []
s2 = []
oper = '*+()'
prior = {
    '+': (1, lambda x, y: x+y),
    '*': (2, lambda x, y: x*y)
}
# add cheks: парность скобок
for item in a:
    if item in oper:
        if item in "()":
            if item == '(':
                s2.append(item)
            else:
                close_breket = True

                while close_breket:
                        curop = s2.pop()
                        if curop == '(':
                            close_breket = False
                        else:
                            c1= int(s1.pop())
                            c2 = int(s1.pop())
                            s1.append(prior[curop][1](c1, c2))
                pass
            pass
        else:
            s2.append(item)
    if item in '0123456789':
        s1.append(item)

while len(s2) != 0:
    c1= int(s1.pop())
    c2 = int(s1.pop())
    curop = s2.pop()
    if curop == '+':
        s1.append(c1+c2)
    if curop == '*':
        s1.append(c1*c2)

r  = prior['+'][1](2,3)
print(r)