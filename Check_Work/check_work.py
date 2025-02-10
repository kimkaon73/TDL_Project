# 특정 날짜의 작업 일정 출력, 없다면 "작업이 존재하지 않습니다" 출력
import json
def check_work():
    while True:
        print              ("---------------------------------------------------")
        day_input = input("양식에 맞춰 날짜를 지정해주세요 [양식 : YYYY-mm-dd]\n원하는 날짜를 입력하세요 : ")
        if len(day_input) == 10:
            break
        else:
            print("잘못된 양식을 입력했습니다.")

    with open("storage.json", "r") as f: # json 파일을 불러옴
        json_data = json.load(f) # json_data에 storage.json의 내용 저장

    in_json = False # json에 날이 저장되어있는지 확인 기본은 False(없음)

    for key in json_data.keys(): # json 파일내부(key)에 날이 존재하는지 for문을 통해 판별
        if day_input == key:
            in_json = True
            break
        else:
            continue

    if in_json == True: # json 파일 내의 날짜 존재여부를 확인하고 없다면 key에 날자 value는 list 형식으로 생성
        print("\n------------------------\n       현재 일정")
        for i in json_data[day_input]:
            print(f"- {i}")
        print("------------------------")
    else:
        print('\n계획된 일정이 없습니다.')
    