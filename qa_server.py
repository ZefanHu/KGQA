from flask import Flask, render_template
from flask import request
from service.question_service import question_service_instant


app = Flask("KGQASE")

def start_server():
    app.run(host='0.0.0.0', port=5000)


@app.route("/web")
def web():
    answer = {
        "content" : "",
        "question" : ""
    }
    return render_template("index.html", answer=answer)

@app.route("/web_answer", methods=["GET","POST"])
def web_answer():
    question = request.form["question"]
    answer_str = question_service_instant.get_answer(question)
    answer = {
        "question" : question,
        "content" : answer_str
    }
    return render_template("index.html", answer=answer)
