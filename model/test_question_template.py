from model import question_template

def test_get_answer():
    question_t = question_template.QuestionTemplate()
    answer = question_t.get_question_answer("英雄的评分是多少呢", 0)
    print(answer)