# from itertools import permutations

# def solution(numbers):

#     numbers = list(map(str, numbers))

#     max_num = '0'

#     for i in permutations(numbers, len(numbers)): 
#         num = ''
#         for j in list(i):
#             num += j
#         if int(num) > int(max_num):
#             max_num = num
#         num = ''


#     return max_num

# 아아니 쉬이이이이이잉이이발 배열의 길이가 10만까지 있는데 이걸 어떻게 런타임에 안걸리게 만들어
# 후 슈퍼컴퓨터라도 맞춰야하나 ㅈ같네


def solution(numbers):

    answer = ''

    numbers=list(map(str, numbers))

    numbers.sort(key=lambda x:x*3, reverse=True)

    for i in numbers:
        answer += i

    return str(int(answer))

print(solution([6, 10, 2]))
# print(solution([3, 30, 34, 5, 9]))