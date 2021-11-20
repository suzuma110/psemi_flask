from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def index():
    lis = []
    for i in range(10):
        lis.append(i)
    
    dictionary = {"nickname": "ria", "age": 21, "address": "Tokyo"}
    ran = random.randint(0, 10)

    return render_template('flaskQ.html', lis=lis, dictionary=dictionary, ran=ran)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)