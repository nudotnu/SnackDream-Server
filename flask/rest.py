from flask import Flask, render_template, url_for, request, jsonify
import json # import json module
import random
app = Flask(__name__)

@app.route('/')
def helloWorld():
    return "<h1>Hello! Welcome!!</h1>"

@app.route('/snack/response', methods=['GET', 'POST'])
def snack():
    # api를 가져와야하는 것 : 열량
    # 데이터 교환해야하는 것 : 랜덤 간식
    number = req.body.action.parameters['num'].value #1,2,랜덤
    
    nugu = json_load()
    # return nugu;
    # print(nugu)
    output = nugu.response.output
    if(number == 3):
        snacks = random.randrange(1,2)
    
    if(number == 1):
        snacks = "사탕"
    elif(number == 2):
        snacks = "초콜릿"
    
    output = { "prompt": snacks + " 간식 입니다." }

    nugu.response.output = output
    return res.json(nugu.response)

@app.route('/config.json')
def json_load():
    response = make_response(render_template('config.json'))
    response.headers['Content-Type'] = 'application/json;charset=UTF-8'
    return response
    # with open('config.json') as json_file:
    # json_data = json.load(json_file)

    # # 문자열
    # # key가 json_string인 문자열 가져오기
    # json_string = json_data["json_string"]
    # print(json_string)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
