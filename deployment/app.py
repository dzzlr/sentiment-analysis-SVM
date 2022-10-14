import os
import sys
from flask import Flask, render_template, request
from werkzeug.serving import run_simple

sys.path.append('../')
os.chdir('../')

app = Flask(__name__)

@app.route('/predict', methods=["GET","POST"])
def sentiment_page():
    if request.method == "POST":
        inp = request.form.get("text")
        sid = sentistrength()
        score = sid.main(inp)

        output = {
            'text': 'Selamat Malam Pak, ada yang bisa saya bantu?',
            'label': 'informasi',
            'score': 0.77796
        }
        return output

if __name__ == '__main__':
    run_simple('http://127.0.0.1', 5000, app)
