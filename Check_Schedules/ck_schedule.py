

# 입력받은 정보로 스케쥴 정보 확인


from . import q_schedule
from . import organize_json
import json

def check(): # check 값을 통해 storage.json에 값이 존재하는지 확인
    check_question = q_schedule.question()
    json_organize = organize_json.organize()
    if check_question == json_organize:
        print("일정이 존재합니다.")
    else:
        print("일정이 존재하지 않습니다.")
