from model import question_template

def test_get_answer():
    question_t = question_template.QuestionTemplate()
    answer = question_t.get_question_answer("章子怡演过哪些电影", 7)
    print(answer)