from collections import deque


with open("input.txt") as file:
    symbols = {'(': ')', '[': ']', '{': '}', '<': '>'}

    score = 0
    for line in file:
        chunk = [x for x in line.strip("\n") if x != ""]
        stack = deque()  # using a stack to track opened brackets

        for symbol in chunk:
            if symbol in ['(', '[', '{', '<']:
                stack.append(symbol)

            elif symbol == ')':
                if stack[-1] != '(':
                    score += 3
                    break
                else:
                    stack.pop()
            elif symbol == ']':
                if stack[-1] != '[':
                    score += 57
                    break
                else:
                    stack.pop()
            elif symbol == '}':
                if stack[-1] != '{':
                    score += 1197
                    break
                else:
                    stack.pop()

            elif symbol == '>':
                if stack[-1] != '<':
                    score += 25137
                    break
                else:
                    stack.pop()

print(score)
