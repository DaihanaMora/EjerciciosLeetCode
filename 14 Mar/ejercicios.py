class Solution:
    # SUBPROBLEMA:
# Sea dp[i] el costo minimo total para LLEGAR al escalon i,
# considerando todos los escalones desde el 0 hasta el i,
# sin haber pagado aun por pisar ese escalon.

# RECURRENCIA:
# Para cada escalon i, hay dos opciones:
# Llegar desde i-1 → dp[i-1] + cost[i-1]
# Llegar desde i-2 → dp[i-2] + cost[i-2]
# dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])

# CASOS BASE:
# dp[0] = 0  (empezar en escalon 0 es gratis)
# dp[1] = 0  (empezar en escalon 1 es gratis)

# COMPLEJIDAD:
# Tiempo O(n), el algoritmo recorre el arreglo cost una sola vez.
# Espacio O(1), solo se usan dos variables auxiliares (prev2, prev1)
# en lugar de un arreglo adicional. La memoria se mantiene constante
# sin importar el tamaño de cost.

def minCostClimbingStairs(cost: list[int]) -> int:
    prev2, prev1 = 0, 0

    for i in range(2, len(cost) + 1):
        current = min(prev1 + cost[i-1], prev2 + cost[i-2])
        prev2, prev1 = prev1, current

    return prev1


if __name__ == "__main__":
    cost1 = [10, 15, 20]
    print(f"cost={cost1} → {minCostClimbingStairs(cost1)}")  # 15

    cost2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print(f"cost={cost2} → {minCostClimbingStairs(cost2)}")  # 6
        

class Solution:
    
    # SUBPROBLEMA:
    # Sea dp[i] el máximo dinero que se puede robar considerando 
    # las casas desde la 0 hasta la i, sin robar casas adyacentes.

    # RECURRENCIA:
    # Para cada casa i, hay dos opciones:
    # No robar la casa i → dp[i-1]
    # Robar la casa i → nums[i] + dp[i-2]

    # CASOS BASE:
    # dp[0] = nums[0]
    # dp[1] = max(nums[0], nums[1])

    # COMPLEJIDAD:
    # Tiempo O(n), el algoritmo recorre el arreglo nums una sola vez.
    # En cada paso hace operaciones simples como suma, comparación (max) y asignaciones.
    # Estas operaciones no dependen del tamaño del arreglo, por lo que el tiempo crece proporcionalmente.
    # Espacio O(1), ya que solo se utilizan variables auxiliares (prev1, prev2, current)
    # y no un arreglo adicional. El uso de memoria se mantiene constante sin importar el tamaño de nums.

    def rob(self, nums):
        prev2 = 0  # dp[i-2]
        prev1 = 0  # dp[i-1]

        for num in nums:
            current = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = current

        return prev1