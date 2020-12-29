class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        i1, j1 = 0, 0
        while S[i1] == '#':
            i1 += 1
        while T[j1] == '#':
            j1 += 1
        S1, T1 = '', ''
        for i in range(i1, len(S)):
            if S[i] == '#':
                if len(S1) > 0: S1 = S1[:len(S1)-1]
            else:
                S1 += S[i]
        for j in range(j1, len(T)):
            if T[j] == '#':
                if len(T1) > 0: T1 = T1[:len(T1)-1]
            else:
                T1 += T[j]
        
        return S1 == T1
