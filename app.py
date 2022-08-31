import jieba
import requests
import execute
from flask import Flask, render_template, request
from zhon.hanzi import punctuation
import re

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/processText', methods=['POST'])
def processText():
#从请求中获取输入信息
    test_text_pth = "./test_data/1.txt"

    req_msg = request.form['text']

#将语句使用结巴分词进行分词
    req_msg = re.sub(r"[%s]+" % punctuation, "", req_msg)
    req_msg = " ".join(jieba.cut(req_msg))
    req_msg = 'start ' + req_msg + ' end'
#调用decode_line对生成回答信息
    res_msg = execute.predict(req_msg)
    return res_msg[6:len(res_msg)-10]


if __name__ == '__main__':
    app.run(debug=True)
