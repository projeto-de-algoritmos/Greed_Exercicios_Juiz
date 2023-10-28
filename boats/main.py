import heapq

def numRescueBoats(people, limit):
    heap = []
    num_barcos = 0

    pessoas_ordenadas = sorted(people, reverse=True)

    for peso in pessoas_ordenadas:
        if not heap:
            heapq.heappush(heap, peso)
            num_barcos += 1
        elif heap[0] + peso > limit:
            heapq.heappush(heap, peso)
            num_barcos += 1
        else:
            heapq.heappop(heap)

    return num_barcos

print(numRescueBoats([3,8,7,1,4], 9))