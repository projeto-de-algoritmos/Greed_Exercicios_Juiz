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
test_cases = {
    "Example 1": [[1,2],[2,3],[3,4]],
    "Example 2": [[1,2],[7,8],[4,5]]
}

solver = Solution()

for key, value in test_cases.items():
    print(key + ":")
    print("Input:", value)
    print("Output:", solver.findLongestChain(value))
    print("-----------")
