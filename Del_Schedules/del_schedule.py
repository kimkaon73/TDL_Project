# json에 저장되어있는 일정 중 사용자가 원하는 날짜의 특정 일정을 삭제함

import json

def del_work(): # json파일 내의 날짜 여부 체크 후 생성 or pass
    while True:
        print              ("\n------------------------------------------------")
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
        print("\n*************")
        print("현재 일정 : ")
        print("0. 취소")
        cnt = 0 # 추후 사용자가 원하는 작업을 쉽게 선택할 수 있도록 번호를 매겨주는 변수수
        for i in json_data[day_input]: #for문을 사용해 현재 일정을 쭉 출력
            print(f"{cnt + 1}. {i}")
            cnt += 1
        print("*************\n")
    else:
        print("\n*******************************")
        print("해당 날짜에 일정이 존재하지 않습니다")
        print("*******************************\n")
        
    del_num = int(input("몇 번 일정을 삭제하시겠습니까? : "))
    if del_num == 0:
        print("취소되었습니다")
        exit()
    list_json = list(json_data[day_input]) # remove를 사용하기 위해선 index 요소의 이름이 필요하기에 json_data[day_input]을 리스트로 만들어서
                                           # 입력받은 del_num을 사용해 index를 지정함
    
    json_data[day_input].remove(list_json[del_num-1]) # 지정된 inodex를 json_data[day_input]에서 삭제함
    print("\n*************")
    print("삭제되었습니다.\n\n현재 일정 : ")
    cnt = 0 # 추후 사용자가 원하는 작업을 쉽게 선택할 수 있도록 번호를 매겨주는 변수수
    for i in json_data[day_input]: #for문을 사용해 현재 일정을 쭉 출력
        print(f"{cnt + 1}. {i}")
        cnt += 1
    print("*************\n")

    with open("storage.json", "w") as f: # 수정된 내용을 저장함
        json.dump(json_data, f)