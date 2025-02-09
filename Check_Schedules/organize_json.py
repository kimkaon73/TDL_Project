

# json 데이터를 스트링 변환 후 비교군이 쉽게 정리


import json

def organize():
    with open("storage.json", "r") as f:
        json_data = json.load(f)
        json_data = json_data[0]
        json_data = list(json_data)
        json_data = str(json_data)
        json_data = json_data[2:-2]
    return json_data