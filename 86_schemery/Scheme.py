from collections import deque

class Scheme:
    def evaluate(expr):
        splitExpr = expr.split(" ")
        stack = deque()

        for i in range(len(splitExpr) - 1, -1, -1):
            stack.append(splitExpr[i])
        
            if stack[len(stack)-1] == "(":
                stack.pop()

                operator = stack.pop()

                result = int(stack.pop())

                while (stack[len(stack)-1] != ")"):
                    if (operator == "+"):
                        result += int(stack.pop())
                    if (operator == "-"):
                        result -= int(stack.pop())
                    if (operator == "*"):
                        result *= int(stack.pop())

                stack.pop()
                stack.append(str(result))

        return stack.pop()
    
    print(evaluate("( + 4 3 )"))
    print(evaluate("( + 4 ( * 2 5 ) 3 )"))
    print(evaluate("( + 4 ( * 2 5 ) 6 3 ( - 56 50 ) )"))
    print(evaluate("( - 1 2 3 )"))