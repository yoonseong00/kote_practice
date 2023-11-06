import heapq

# def solution(scoville, K):

#     sco = sorted(scoville)

#     count = 0

#     for i in sco:
#         if i < K:
#             sco.append(sco[0]+sco[1]*2)
#             sco.sort()
#             sco = sco[2:]
#             count += 1
#         if sco[0] >= K:
#             break
        
#         if len(sco) == 1 and sco[0] < K:
#             return -1
#     return count

def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)

    while scoville[0] < K:
        sco = heapq.heappop(scoville) + heapq.heappop(scoville) * 2
        heapq.heappush(scoville, sco)
        answer += 1
        if len(scoville) == 1 and scoville[0] < K:
            return -1
    
    return answer

        

print(solution([1, 2, 3, 9, 10, 12], 7))
print(solution([1,1,1,1,1,1], 15))
