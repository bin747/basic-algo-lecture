import sys

while True:
    arr = []
    s = sys.stdin.readline().rstrip()

    if s == '.':
        break
    else:
        isRight = True
        for i in range(len(s)):
            if s[i] == '[' or s[i] == '(':
                arr.append(s[i])
            elif s[i] == ']':
                if not arr or arr.pop() != '[':
                    isRight = False
                    break
            elif s[i] == ')':
                if not arr or arr.pop() != '(':
                    isRight = False
                    break

        if len(arr) != 0:
            isRight = False

        if isRight:
            print('yes')
        else:
            print('no')
