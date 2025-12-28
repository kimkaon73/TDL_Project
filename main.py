# TDL 작성 프로그램
from Del_Schedules import del_schedule
from Add_Schedules import add_work
from Check_Work import check_work
import time


while(True):
    print("************")
    print("0. 프로그램 종료")
    print("1. 일정 확인")
    print("2. 일정 추가")
    print("3. 일정 제거")
    print("************\n") 
    user_answer = input("원하는 동작을 입력하세요 : ")
    if user_answer == "1":
        check_work.check_work ()
        time.sleep(2)
    elif user_answer =="2":
        add_work.check_day()
        time.sleep(2)
    elif user_answer == "3":
        del_schedule.del_work()
        time.sleep(2)
    elif user_answer == "0":
        break
    else:
        print("잘못된 입력입니다, 정확한 값을 입력해주세요\n")
        continue