from flask import Flask, render_template, url_for, request, jsonify
import json # import json module
import random
app = Flask(__name__)

print("hello")

@app.route('/snack', methods=['GET', 'POST'])

def snacks():
    
    with open('config.json', encoding='UTF-8') as json_file:
        json_data = json.load(json_file)
        json_string = json_data["action"]["parameters"]["shortcut"]["value"]
        print(json_string)
        nugu_output = json_data["output"]
        nugu_output = "hello"

        nugu_prom = {
            'output': {
                'prompt': nugu_output
            }
        }

        print(nugu_prom)
        return nugu_prom
    

if __name__ == '__main__':
    app.run()