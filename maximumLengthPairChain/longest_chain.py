from typing import List

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

# Casos de teste
casos_teste = {
    "Exemplo 1": [[1,2],[2,3],[3,4]],
    "Exemplo 2": [[1,2],[7,8],[4,5]]
}

res = Solution()

for key, value in casos_teste.items():
    print(key + ":")
    print("Input:", value)
    print("Output:", res.findLongestChain(value))
    print("-----------")
