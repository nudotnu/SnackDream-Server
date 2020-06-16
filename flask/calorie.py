from flask import Flask, render_template, url_for, request, jsonify
import json # import json module
import random
app = Flask(__name__)

@app.route('/calorie', methods=['GET', 'POST']) // 이 주소로 들어가면 GET메소드나 POST 메소드 사용
def snacks():
    file_path = "config.json" // 파일 경로
    json_new = dict() // dict사용 예를 들어 {Key1:Value1, Key2:Value2, Key3:Value3, ...} 이런 거
    json_data = {} // 새로운 데이터 들어갈 공간

    with open(file_path, encoding='UTF-8') as json_file: 
        json_data = json.load(json_file)
        json_string = json_data["action"]["parameters"]["calorie"]["value"]
    // 파일 경로에 있는 json_file이라는 이름을 가진 파일 로드해오고 
    // json_string이라는 변수에 json_file의 action 안에 ... value 값 가져옴    
    
    print(json_string)

    if(json_string == "초콜릿"): 
        food = "초콜릿은 100g당 약 550칼로리 입니다."
    
    elif (json_string == "사탕"):
        food = "사탕은 3개당(14g) 52칼로리 입니다."

    json_new = {
        "prompt": food // prompt라는 키를 가진 food 값
    }
    

    json_data["output"] = json_new // data중에 output에 위에 키와 값을 넣음

    with open(file_path, 'w', encoding='utf-8') as make_file:
        json.dump(json_data, make_file, indent="\t")
    // 파일쓰기

    # with open(file_path, 'r', encoding='utf-8') as f:
    #     json_data = json.load(f)
    # print(json.dumps(json_data, indent="\t") )

    return jsonify(json_data)
    // json 형식으로 json_data를 

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, threaded=True)
