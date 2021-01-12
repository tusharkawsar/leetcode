class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        T, B, L, R = 0, len(matrix)-1, 0, len(matrix[0])-1
        dir = 0 # 0: L to R, 1: T to B, 2: R to L, 3: B to T
        ret_val = []
        
        while T <= B and L <= R:
            if dir == 0:
                for i in range(L, R+1):
                    ret_val.append(matrix[T][i])
                dir = 1
                T += 1
                continue
                
            elif dir == 1:
                for i in range(T, B+1):
                    ret_val.append(matrix[i][R])
                dir = 2
                R -= 1
                continue
                
            elif dir == 2:
                for i in range(R, L-1, -1):
                    ret_val.append(matrix[B][i])
                dir = 3
                B -= 1
                continue
                
            elif dir == 3:
                for i in range(B, T-1, -1):
                    ret_val.append(matrix[i][L])
                dir = 0
                L += 1
                continue
                
        return ret_val
