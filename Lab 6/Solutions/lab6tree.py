class Node:
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None
        self.isFull = False

    def PrintNodes(self):
        expression = ''
        if self.leftChild is not None:
            expression = expression + '(' + self.leftChild.PrintNodes()
        expression = expression + self.value
        if self.rightChild is not None:
            expression = expression + self.rightChild.PrintNodes() +')'

        return expression

    def Calc(self):
        if IsOperator(self.value):
            if IsOperator(self.leftChild.value):
                self.leftChild.Calc()

            if IsOperator(self.rightChild.value):
                self.rightChild.Calc()

            if self.value == '+':
                self.value = float(self.leftChild.value) + float(self.rightChild.value)
            elif self.value == '-':
                self.value = float(self.leftChild.value) - float(self.rightChild.value)
            elif self.value == '*':
                self.value = float(self.leftChild.value) * float(self.rightChild.value)
            elif self.value == '/':
                self.value = float(self.leftChild.value) / float(self.rightChild.value)
            elif self.value == '^':
                self.value = pow(float(self.leftChild.value), float(self.rightChild.value))


    def printTree(self):
        if self.rightChild is None and self.leftChild is None:
            line = '%s' % self.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        elif self.rightChild is None:
            lines, n, p, x = self.leftChild.printTree()
            s = '%s' % self.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        elif self.leftChild is None:
            lines, n, p, x = self.rightChild.printTree()
            s = '%s' % self.value
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        else:
            left, n, p, x = self.leftChild.printTree()
            right, m, q, y = self.rightChild.printTree()
            s = '%s' % self.value
            u = len(s)
            first_line = (x+1)*' ' +(n-x-1)*'_'+s+y*'_'+(m-y)*' '
            second_line = x*' ' + '/'+(n-x-1+u+y)*' ' + '\\'+(m-y-1)*' '
            if p < q:
                left += [n*' '] *(q-p)
            elif q < p:
                right += [m*' ']*(p-q)

            zipped_lines = zip(left, right)
            lines = [first_line, second_line] + [a+u*' '+b for a, b in zipped_lines]
            return lines, n+m+u, max(p,q) + 2, n+u//2

class ExpressionTree:
    def __init__(self):
        self.root = None
        self.prevStack = list()

    def InsertNode(self, value):
        if self.root is None:
            self.root = Node(value)

        else:
            curr = self.root
            prev = None
            toInsert = Node(value)
            while curr is not None:
                if IsOperator(curr.value):
                    if curr.leftChild is None:
                        curr.leftChild = toInsert
                        curr = None
                    elif IsOperator(curr.leftChild.value):
                        prev = curr
                        curr = curr.leftChild
                        self.prevStack.append(prev)
                    elif curr.rightChild is None:
                        curr.rightChild = toInsert
                        curr = None
                    elif IsOperator(curr.rightChild.value):
                        prev = curr
                        curr = curr.rightChild
                        self.prevStack.append(prev)
                    else:
                        prev = self.prevStack.pop(-1)
                        if prev.rightChild is None:
                            prev.rightChild = toInsert
                            curr = None
                        else:
                            curr = prev.rightChild
                else:
                    print("Error")
                    return

    def Evaluate(self):
        self.root.Calc()

    def GetExpression(self):
        return self.root.PrintNodes()

    def Count(self, expr):
        splitedExpr = splitExpr(expr)
        self.root = None

        print("Your expression is: " + expr)

        splitedExpr = infixToPrefix(splitedExpr)
        print('Inserting: ' + str(splitedExpr))
        for elem in splitedExpr:
            self.InsertNode(elem)

        print('Interpreting as: ', end='')
        print(self.GetExpression())
        self.printTree()
        self.Evaluate()
        print('Result: ' + str(self.root.value) + '\n\n')


    def populate_tree(self, expr):
        splitedExpr = splitExpr(expr)
        self.root = None

        splitedExpr = infixToPrefix(splitedExpr)
        for elem in splitedExpr:
            self.InsertNode(elem)

    def printTree(self):
        tree_print = ''
        if self.root != None:
            lines, *_ = self.root.printTree()
            for line in lines:
                tree_print = tree_print + line + '\n'

        return tree_print


def getMax(a, b):
    if a >= b:
        return a
    else:
        return b

def IsOperator(value):
    if value == '+' or value == '-' or value == '*' or value == '/' or value == '^':
        return True
    return False


def getPriority(operator):
    if operator == '-' or operator == '+':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    elif operator == '^':
        return 3
    else:
        return 0


def infixToPostfix(expr):
    expr.insert(0, '(')
    expr.append(')')
    stack = []
    outputFix = []

    for i in range(0, len(expr)):
        if not IsOperator(expr[i]) and expr[i] != '(' and expr[i] != ')':
            outputFix.append(expr[i])
        elif expr[i] == '(':
            stack.append('(')
        elif expr[i] == ')':
            while stack[-1] != '(':
                outputFix.append(stack.pop())
            stack.pop()
        elif IsOperator(expr[i]):
            while getPriority(expr[i]) <= getPriority(stack[-1]):
                outputFix.append(stack.pop())

            stack.append(expr[i])

    return outputFix


def infixToPrefix(expr):
    expr = expr[::-1]

    expr = ['?' if x == '(' else x for x in expr]
    expr = ['(' if x == ')' else x for x in expr]
    expr = [')' if x == '?' else x for x in expr]

    expr = infixToPostfix(expr)

    expr = expr[::-1]

    return expr


def splitExpr(expr):
    output = []
    buff = ''

    def relBuff():
        if buff != '':
            output.append(buff)

    for i in range(0, len(expr)):
        if expr[i] == '(' or expr[i] == ')':
            relBuff()
            buff = ''
            output.append(expr[i])
        elif IsOperator(expr[i]):
            if i == 0 or IsOperator(expr[i-1]) or expr[i - 1] == '(':
                buff = buff + expr[i]
            else:
                relBuff()
                buff = ''
                output.append(expr[i])
        else:
            buff = buff + expr[i]

    relBuff()
    return output


if __name__ == '__main__':
    et = ExpressionTree()

    et.Count("-2.75*(34/5)+4*((-7)^2)")
    et.Count("1+2*3.3-7")
    et.Count("sqrt(1)")
