import heapq

def jump(nums):

    if len(nums) <=1:
        return 0

    pulos = 1
    dist_max = nums[0]
    max_heap = []

    for i in range(1, len(nums)):
        heapq.heappush(max_heap, -(nums[i] + i))
        if i == len(nums) - 1:
            break
        elif i == dist_max:
            dist_max = -max_heap[0]
            heapq.heappop(max_heap)
            pulos += 1
    
    return pulos

print(jump([2,3,1,1,4]))
