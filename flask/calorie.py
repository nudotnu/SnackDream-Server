from flask import Flask, render_template, url_for, request, jsonify
import json # import json module
import random
app = Flask(__name__)

@app.route('/snack', methods=['GET', 'POST'])
def snacks():
    file_path = "config.json" 
    json_new = dict()
    json_data = {}
    with open(file_path, encoding='UTF-8') as json_file:
        json_data = json.load(json_file)
        json_string = json_data["action"]["parameters"]["shortcut"]["value"]
        print(json_string)

    json_new = {
        "prompt": json_string
    }

    json_data["output"] = json_new

    with open(file_path, 'w', encoding='utf-8') as make_file:
        json.dump(json_data, make_file, indent="\t")

    # with open(file_path, 'r', encoding='utf-8') as f:
    #     json_data = json.load(f)
    # print(json.dumps(json_data, indent="\t") )

    return jsonify(json_data)

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, threaded=True)