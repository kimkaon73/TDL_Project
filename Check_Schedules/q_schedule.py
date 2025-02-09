

# 사용자에게 원하는 날짜를 입력받음


def question(): # 입력받은 값 리턴턴
    while(True):
        user_answer = input("사용자 입력 : ") # user_answer라는 변수에 입력값 받기
        if len(user_answer) == 8:
            break
        else:
            print("양식을 확인해주세요")
            continue
    return user_answer