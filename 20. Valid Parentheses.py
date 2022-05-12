class Solution:
    def isstringValid(self, s:str) -> bool:
        stack_s = []
        for c in s:
            if len(stack_s) > 0:
                pre_c = stack_s[-1]
                if (pre_c == "(" and c ==")") 
                or (pre_c == "[" and c =="]") 
                or (pre_c == "{" and c =="}"):
                stack_s.pop()
                else:
                    stack_s.append(c) 
            else:
                stack_s.append(c)
        return False if len(stack_s)!=0 else True