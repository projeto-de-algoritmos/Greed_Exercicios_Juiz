class Solution:
    def findLongestChain(self, pares: List[List[int]]) -> int:
        pares.sort(key=lambda p: p[1])
        
        comprimento = 1
        fim = pares[0][1]
        
        i = 1
        n = len(pares)
        
        while i < n:
            if fim < pares[i][0]:
                comprimento += 1
                fim = pares[i][1]
            i += 1
        
        return comprimento