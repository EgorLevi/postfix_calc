class StackCalc:
    def __init__(self) -> None:
        self.priority = {
            '+':(1, lambda x, y: x+y),
            '-':(1, lambda x, y: x-y),
            '*':(2, lambda x, y: x*y),
            '/':(2, lambda x, y: x/y),
            '^':(3, lambda x, y: y**x),
            '(':(1, None),
            ')':(1,None)
        }       
        self.operations = '+-*/^()'
        self.numbers = '0123456789'

        pass

    def stack_is_empty(self, stack):
        if len(stack) == 0:
            return True
        return False
    
    def get_stack(self, string_ex):
        rs = []
        collect_str = ''
        for item in string_ex:
            if item in self.operations:
                if collect_str != '':
                    rs.append(collect_str)
                rs.append(item)
                collect_str = ''
            else:
                collect_str+= item
        if collect_str!='':
            rs.append(collect_str)
        return rs

    def dual_brekets_check(self, inp_strin):
        if inp_strin.count('(') == inp_strin.count(')'):
            return True
        return False

    def calculate_string(self, inputed_string):
        if self.dual_brekets_check(inputed_string):
            inputed_stack = self.get_stack(inputed_string)
            
            numbers_stack = []
            operations_stack = []      

            for item in inputed_stack:
                if item not in self.operations:
                    numbers_stack.append(item)
                else:
                    if self.stack_is_empty(operations_stack):
                        operations_stack.append(item)
                    else:
                        if item in '()':
                            if item == '(':
                                operations_stack.append(item)
                            else:
                                while operations_stack[-1] != '(':
                                    numbers_stack.append(self.priority[operations_stack.pop()][1](int(numbers_stack.pop()), int(numbers_stack.pop())))
                                operations_stack.pop()

                        else:
                            if self.priority[item][0] < self.priority[operations_stack[-1]][0]:
                                numbers_stack.append(self.priority[operations_stack.pop()][1](int(numbers_stack.pop()), int(numbers_stack.pop())))
                                operations_stack.append(item)
                            else:
                                operations_stack.append(item)
            operations_stack.reverse()
            numbers_stack.reverse()
            while not self.stack_is_empty(operations_stack):
                numbers_stack.append(self.priority[operations_stack.pop()][1](int(numbers_stack.pop()), int(numbers_stack.pop())))
                
            return numbers_stack[0]
        return False

#print(get_stack("(2+2)^2+7*3-(11+5)"))
b = "(2+2)^2+7*3-(11+22)" #= 16 + 21 - 33
c = '16+21-33'
# 16 21 33
# + -
a = StackCalc()
print(a.calculate_string(b))


