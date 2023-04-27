# 문자열 폭발
string = input()
bomb = input()
stack = []
length = len(bomb)

for char in string:
    stack.append(char)
    if char == bomb[-1] :
        if ''.join(stack[-length:]) == bomb:
            del stack[-length:]
    
if not stack :
    print("FRULA")
else :
    print(''.join(stack))
