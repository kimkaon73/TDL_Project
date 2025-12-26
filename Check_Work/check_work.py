# 특정 날짜의 작업 일정 출력, 없다면 "작업이 존재하지 않습니다" 출력
import json
def check_work():
    with open("storage.json", "r") as f: # json 파일을 불러옴
        json_data = json.load(f) # json_data에 storage.json의 내용 저장

    # 현재 할일의 개수를 파악하기 위해 json 파일에서 key의 개수를 확인
    num_dolist = 0
    for key in json_data.keys():
        num_dolist+=1
    print(f"현재 할 일의 개수{num_dolist}\n")

    # 확인된 날짜들을 번호형식으로 아래로 출력
    do_list = [100]
    di = 0
    for key in json_data.keys():
        do_list[di] = key
        di += 1
    
    for i in do_list:
        print(i)
    