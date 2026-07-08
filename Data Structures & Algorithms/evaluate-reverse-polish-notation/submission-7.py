class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        a = 0
        b = 0
        for i in tokens:
            if i not in {"+", "-","*","/"}:
                s.append(int(i))
            else:
                if(len(s) != 0):
                    a = s.pop()
                if(len(s) != 0):
                    b = s.pop()
                if i == "+":
                    s.append(b + a)
                elif i == "-":
                    s.append(b-a)
                elif i == "*":
                    s.append(b*a)
                if i == "/":
                    if(a != 0):
                        s.append(int(float(b)/a))
        return s[0]

        