from collections import deque

with open("input.txt") as file:

    score = 0
    scores = []
    clean = []
    for line in file:
        chunk = [x for x in line.strip("\n") if x != ""]
        stack = []  # using a stack to track opened brackets

        for symbol in chunk:
            corrupted = False
            if symbol in ['(', '[', '{', '<']:
                stack.append(symbol)

            elif symbol == ')':
                if stack[-1] != '(':
                    score += 3
                    corrupted = True
                    break
                else:
                    stack.pop()
            elif symbol == ']':
                if stack[-1] != '[':
                    score += 57
                    corrupted = True
                    break
                else:
                    stack.pop()
            elif symbol == '}':
                if stack[-1] != '{':
                    score += 1197
                    corrupted = True
                    break
                else:
                    stack.pop()

            elif symbol == '>':
                if stack[-1] != '<':
                    score += 25137
                    corrupted = True
                    break
                else:
                    stack.pop()

        if not corrupted:
            score2 = 0
            remaining = []
            rev = stack[::-1]

            for symbol in rev:
                score2 *= 5
                if symbol == '(':
                    remaining.append(')')
                    score2 += 1
                elif symbol == '[':
                    remaining.append(']')
                    score2 += 2
                elif symbol == '{':
                    remaining.append('}')
                    score2 += 3
                elif symbol == '<':
                    remaining.append('>')
                    score2 += 4
            scores.append(score2)

scores.sort()
middle = len(scores) // 2
print(scores[middle])
