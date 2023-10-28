from typing import List

class Solution:
    def twoCitySchedCost(self, custos: List[List[int]]) -> int:
        n = len(custos)
        diferencas = [(i, c1 - c2) for i, (c1, c2) in enumerate(custos)]
        diferencas.sort(key=lambda x: x[1])

        custoMinimo = 0
        for i in range(n):
            custoMinimo += custos[diferencas[i][0]][i // (n // 2)]

        return custoMinimo

# Casos de teste
casos_teste = {
    "Exemplo 1": [[10, 20], [30, 200], [400, 50], [30, 20]],
    "Exemplo 2": [[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]],
    "Exemplo 3": [[515, 563], [451, 713], [537, 709], [343, 819], [855, 779], [457, 60], [650, 359], [631, 42]]
}

res = Solution()

for key, value in casos_teste.items():
    print(key + ":")
    print("Input:", value)
    print("Output:", res.twoCitySchedCost(value))
    print("-----------")