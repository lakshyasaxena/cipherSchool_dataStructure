def check(string):
    
    stack = []
    mydict = {')': '(', ']': '[', '}': '{'}
    for char in string:
        if char in {'(', '[', '{'}:
            stack.append(char)
        else:
            if stack and mydict[char] == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
    if len(stack) == 0:
        return True
    else:
        return False

T = int(input())
while T > 0:
    string = input()
    if check(string):
        print('YES')
    else:
        print('NO')
    T -= 1    

# time complexity: O(n)
# space complexity: O(n) 
# by - Mayank Chaudhary
