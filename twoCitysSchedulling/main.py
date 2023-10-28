class Solution:
    def twoCitySchedCost(self, custos: List[List[int]]) -> int:
        n = len(custos)
        diferencas = [(i, c1 - c2) for i, (c1, c2) in enumerate(custos)]
        diferencas.sort(key=lambda x: x[1])

        custoMinimo = 0
        for i in range(n):
            custoMinimo += custos[diferencas[i][0]][i // (n // 2)]

        return custoMinimo