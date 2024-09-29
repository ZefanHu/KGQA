from flask import Flask, render_template
from flask import request
from service.question_service import question_service_instant
from common import log_util

app = Flask("KGQASE")
log = log_util.get_main_logger()

def start_server():
    app.run(host='0.0.0.0', port=5000)

@app.route("/")
def web():
    log.warning("====== user ip: {} index======".format(request.remote_addr))
    answer = {
        "content" : "",
        "question" : ""
    }
    return render_template("index.html", answer=answer)

@app.route("/web_answer", methods=["GET","POST"])
def web_answer():
    log.warning("====== user ip: {} get_answer======".format(request.remote_addr))
    question = request.form["question"]
    answer_str = question_service_instant.get_answer(question)
    answer = {
        "question" : question,
        "content" : answer_str
    }
    return render_template("index.html", answer=answer)
