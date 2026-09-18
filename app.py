from flask import Flask, render_template, redirect, request
import json, os, time

json_file = "users.json"

app = Flask(__name__)

def loadFile():
    if not os.path.exists(json_file):
        return []
    try:
        with open(json_file, encoding='utf-8') as file:
            return json.load(file)
    except Exception:
        return []

@app.route('/')
def main():
    return render_template("main.html", messages=loadFile())

@app.route('/write')
def write():
    return render_template('write.html')

@app.route('/send', methods=["POST", "GET"])
def send():
    information = request.form.to_dict()
    currentFile = loadFile()
    currentFile.append(information)
    print(information)
    all_info = True
    for part in information:
        if information[part] == "":
            all_info = False

    if not all_info:
        return "Missing information, please try again!"
    

    with open(json_file, 'w', encoding="utf-8") as file:
        json.dump(currentFile, file, indent=4)

    return "Sent information"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')