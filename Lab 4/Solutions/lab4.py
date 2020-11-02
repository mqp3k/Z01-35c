import re


class Node:
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None
        self.isFull = False

    def PrintNodes(self):
        if self.leftChild is not None:
            print('(', end='')
            self.leftChild.PrintNodes()
        print(self.value, end='')
        if self.rightChild is not None:
            self.rightChild.PrintNodes()
            print(')', end='')

    def IsOperator(self):
        if self.value == '+' or self.value == '-' or self.value == '*' or self.value == '/' or self.value == '^':
            return True
        return False

    def Calc(self):
        if self.IsOperator():
            if self.leftChild.IsOperator():
                self.leftChild.Calc()

            if self.rightChild.IsOperator():
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


class ExpressionTree:
    def __init__(self):
        self.root = None
        self.prevStack = list()

    def IsOperator(self, value):
        if value == '+' or value == '-' or value == '*' or value == '/' or value == '^':
            return True
        return False

    def InsertNode(self, value):
        if self.root is None:
            self.root = Node(value)

        else:
            curr = self.root
            prev = None
            toInsert = Node(value)
            while curr is not None:
                if self.IsOperator(curr.value):
                    if curr.leftChild is None:
                        curr.leftChild = toInsert
                        curr = None
                    elif self.IsOperator(curr.leftChild.value):
                        prev = curr
                        curr = curr.leftChild
                        self.prevStack.append(prev)
                    elif curr.rightChild is None:
                        curr.rightChild = toInsert
                        curr = None
                    elif self.IsOperator(curr.rightChild.value):
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

    def PrintValues(self):
        self.root.PrintNodes()
        print()

    def Count(self, expr):
        splitedExpr = splitExpr(expr)
        self.root = None

        print("Your expression is: " + expr)

        splitedExpr = infixToPrefix(splitedExpr)
        print('Inserting: ' + str(splitedExpr))
        for elem in splitedExpr:
            self.InsertNode(elem)

        print('Interpreting as: ', end='')
        self.PrintValues()

        self.Evaluate()
        print('Result: ' + str(self.root.value) + '\n\n')


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
        if expr[i] != '+' and expr[i] != '-' and expr[i] != '*' and expr[i] != '/' and expr[i] != '^' and expr[
            i] != '(' and expr[i] != ')':
            outputFix.append(expr[i])
        elif expr[i] == '(':
            stack.append('(')
        elif expr[i] == ')':
            while stack[-1] != '(':
                outputFix.append(stack.pop())
            stack.pop()
        else:
            if expr[i] == '+' or expr[i] == '-' or expr[i] == '*' or expr[i] == '/' or expr[i] == '^':
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

    def relBuff(buff):
        if buff != '':
            output.append(buff)

    for i in range(0, len(expr)):
        if expr[i] == '(' or expr[i] == ')':
            relBuff(buff)
            buff = ''
            output.append(expr[i])
        elif expr[i] == '+' or expr[i] == '-' or expr[i] == '*' or expr[i] == '/' or expr[i] == '^':
            if i == 0 or expr[i - 1] == '+' or expr[i - 1] == '-' or expr[i - 1] == '*' or expr[i - 1] == '/' or expr[
                i - 1] == '^' or expr[i - 1] == '(':
                buff = buff + expr[i]
            else:
                relBuff(buff)
                buff = ''
                output.append(expr[i])
        else:
            buff = buff + expr[i]

    relBuff(buff)
    return output


if __name__ == '__main__':
    et = ExpressionTree()

    et.Count("-2.75*(34/5)+4*((-7)^2)")
    et.Count("1")
