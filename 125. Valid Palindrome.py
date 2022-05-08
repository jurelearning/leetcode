class Solution:
    def isPalindrome(s:str)->bool:
            re_s = ''.join(c for c in s.lower() if c.isalnum())
            if re_s == re_s[::-1]:
                return True
            
            return False
            
            # end_ind = len(re_s) - 1  
            # if len(re_s) == 0:
            #     return True
            # for str_ind in range(len(re_s)):
            #     if re_s[str_ind] != re_s[end_ind]:
            #         return False
            #     if str_ind != end_ind and re_s[str_ind] == re_s[end_ind]:
            #         str_ind = str_ind + 1
            #         end_ind = end_ind - 1
            #     if str_ind > end_ind or str_ind == end_ind:
            #         return True

            ### Wait for future to rewrite isalnum() part