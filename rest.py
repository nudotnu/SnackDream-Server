from flask import Flask, render_template, url_for
import json # import json module
import inotify.adapters
import os
import random
app = Flask(__name__)

@app.route('/snack/response', methods=['GET', 'POST'])
def snack(req,res):
    # api를 가져와야하는 것 : 열량
    # 데이터 교환해야하는 것 : 랜덤 간식
    number = req.body.action.parameters['num'].value #1,2,랜덤
    
    nugu = json_load()
    output = nugu.response.output
    if(number == 3){
        snacks = random.randrange(1,2)
    }
    switch(number){
        case 1 : snacks = "사탕" break;
        case 2 : snacks = "초콜릿" break;
    }
    output = { "prompt": snacks + " 간식 입니다." }

    nugu.response.output = output
    return res.json(nugu.response)

def json_load():
    with open('config.json') as json_file:
    json_data = json.load(json_file)

    # 문자열
    # key가 json_string인 문자열 가져오기
    json_string = json_data["json_string"]
    print(json_string)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
