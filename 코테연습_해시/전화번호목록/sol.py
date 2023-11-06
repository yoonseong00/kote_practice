def solution(phone_book):
    book = []

    count = 0

    a = phone_book[0]

    

    for i in phone_book:
        if len(i) > 3:
            pass# phone.append(i[2:])
        # else:
        #     if i != a:
        #         count += 1
    for char in phone_book:
        for j in char:
            j = j.strip()
            book.append(j)

    # for k in book:
    #     if book[:len(a)] != a:
    #         count += 1
    print(book)



    # if count > 0:
    #     return True
    # else:
    #     return False

print(solution(["119", "97 674223", "11 95524421"]))
print(solution(["123","456","789"]))




# 접두어가 겹치면 false 하나도 안겹쳐야  


# 폰북의 첫번째 인자가 2~마지막 인자의 시작으로 시작하는게 있으면 True
# 그러나, 2번째나 3번째의 인자가 다른 숫자의 인자로 시작되면 False

# 일단.. 첫번째 인자를 시작으로 갖는 인자들을 한곳에 저장
# 후. 두번째 인자를 또 돌려서 겹치는 숫자가 있으면 제거
# 해서? 저장소의 길이가 1이상이면 faslse 아니면 tru

# 아 미친 접두어가 따로 있네 아~~~~~~~~ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ