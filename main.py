# TDL 작성 프로그램
from Check_Schedules import ck_schedule

print("1. 일정 확인")
print("2. 일정 추가")
print("3. 일정 제거")
user_answer = input("원하는 동작을 입력하세요 : ")
if user_answer == "1":
    ck_schedule.check()
elif user_answer =="2":
    pass # "원하는 날짜를 입력하세요 :" + "일정의 내용을 입력하세요" -> json 파일에 저장
elif user_answer == "3":
    pass # "원하는 날짜를 입력하세요 :" -> 해당 날짜 일정 출력 [1.- 2.- 3.-] -> 번호 선택 및 삭제 
