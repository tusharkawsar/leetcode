class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        trie={}
        for w in words:
            cur=trie
            for c in w:
                if c not in cur.keys():
                    cur[c]={}
                cur=cur[c]
            cur['#']=True
        
        res=[]
        lens=len(text)
        for i in range(lens):
            cur=trie
            cc=text[i]
            j=i
            while cc in cur.keys():
                cur=cur[cc]
                if '#' in cur.keys():
                    res.append([i,j])
                j+=1
                if j==lens:
                    break
                else:
                    cc=text[j]
        return res
