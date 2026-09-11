from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("main.html")

@app.route('/write')
def write():
    return render_template('write.html')

@app.route('/send', methods=["POST", "GET"])
def send():
    information = request.form.to_dict()
    for part in information:
        pass # FIXA SENARE
    return "Sent information"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')