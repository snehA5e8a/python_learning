#balanced eq prob: opening bracket added to stack, close one - value pair(opening one) checked with stack value
# on the logic, for the last open one -  first closing one should match it, opening ones and closing ones should be in order


from collections import deque
s = deque()
s.append('https://www.youtube.com/')
s.append('https://www.youtube.com/watch?v=Y346900i9qE')
s.append('https://www.youtube.com/watch?v=zcZkEM7Yk_8')
s.append('https://www.youtube.com/watch?v=Kw-XEmpAj40')
print(s)
print(s.pop())
print(s)

#implementing using class to deeply understand
class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


    def reverse_string(self, value):
        val = Stack()
        for i in value:
            val.push(i)
        rev = ''
        i = 0
        for i in range(val.size()):
            rev += val.pop()
        return rev

def is_match(ch1, ch2):
    match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    return match_dict[ch1] == ch2


def is_balanced(s):
    stack = Stack()
    for ch in s:
        if ch == '(' or ch == '{' or ch == '[':
            stack.push(ch)
        if ch == ')' or ch == '}' or ch == ']':
            if stack.size() == 0:
                return False
            if not is_match(ch, stack.pop()):
                return False

    return stack.size() == 0


if __name__ == '__main__':
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("((a+g))"))
    print(is_balanced("))"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))

    
s = Stack()
s.push('https://www.youtube.com/')
s.push('https://www.youtube.com/watch?v=Y346900i9qE')
s.push('https://www.youtube.com/watch?v=zcZkEM7Yk_8')
s.push('https://www.youtube.com/watch?v=Kw-XEmpAj40')
print(s.size())
s.pop()
print(s.size())
rev = Stack()
print(rev.reverse_string(("We will conquere COVID-19")))

#s = []
#s.append('https://www.youtube.com/')
#s.append('https://www.youtube.com/watch?v=Y346900i9qE')
#s.append('https://www.youtube.com/watch?v=zcZkEM7Yk_8')
#s.append('https://www.youtube.com/watch?v=Kw-XEmpAj40')
#print(s[-1])
#print(s[-3])
#print(s[-2])
#print(s.pop())
#print(s)
