def solution(citations):
    answer = 0

    citations = sorted(citations, reverse = True)

    for i in range(len(citations)):
        if citations[i] < i+1:
            return i

    return len(citations)

print(solution([3, 0, 6, 1, 5]))
print(solution([6,6,6,6,6]))