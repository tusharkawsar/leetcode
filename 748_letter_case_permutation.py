class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        def backtrack(S: str, l):
            if len(S) < 1 or not S:
                return l
            
            if S[0].isdigit():
                # print("isdigit")
                ret_val = backtrack(S[1:], l)
                if len(l) < 1:
                    l.append(S[0])
                else:
                    for i in range(len(ret_val)):
                        ret_val[i] = S[0] + ret_val[i]
                # print(l)
                return l
            else:
                # print("ischar")
                ret_val = backtrack(S[1:], l)
                if len(l) < 1:
                    l.append(S[0].lower())
                    l.append(S[0].upper())
                else:
                    for i in range(len(ret_val)):
                        ret_val[i] = S[0].lower() + ret_val[i]
                    len1 = len(ret_val)
                    for i in range(len1):
                        l.append(S[0].upper() + ret_val[i][1:])
                # print(l)
                return l
            
        l = []
        return backtrack(S, l)
