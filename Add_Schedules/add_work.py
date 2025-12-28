
# user에게 입력받은 날짜와 일정을 storage.json 파일에 추가함함

import json

def check_day(): # json파일 내의 날짜 여부 체크 후 생성 or pass
    while True:
        print("\n---------------------------------------------------")
        print("양식에 맞춰 날짜를 지정해주세요 ", end="")
        day_input = input("[양식 : YYYY-mm-dd]\n** 취소를 원할경우 0을 입력하세요**\n\n원하는 날짜를 입력하세요 : ")
        if len(day_input) == 10:
            break 
        elif int(day_input) == 0:
            print("취소되었습니다")
            exit()
        else:
            print("잘못된 양식을 입력했습니다.\n")
    work_input = input("원하는 일정을 입력하세요 : ")

    with open("./storage.json", "r") as f: # json 파일을 불러옴
        json_data = json.load(f) # json_data에 storage.json의 내용 저장

    in_json = False # json에 날이 저장되어있는지 확인 기본은 False(없음)

    for key in json_data.keys(): # json 파일내부(key)에 날이 존재하는지 for문을 통해 판별
        if day_input == key:
            in_json = True
            break
        else:
            continue

    if in_json == True: # json 파일 내의 날짜 존재여부를 확인하고 없다면 key에 날자 value는 list 형식으로 생성
        pass
    else:
        json_data[day_input] = []
    with open("storage.json", "w") as f: # 수정된 내용을 저장함
        json.dump(json_data, f)
    
    json_data[day_input].append(work_input) # 생성 or 원래 존재하던 날짜에 할 일을 작성

    print(f"\n------------------------\n일정이 추가되었습니다.\n")
    print("현재 일정 : ")
    for i in json_data[day_input]:
        print(f"- {i}")
    print("------------------------")
    with open("storage.json", "w") as f: # 수정된 내용을 저장함
        json.dump(json_data, f)