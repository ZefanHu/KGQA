from model.question_classify_model import QuestionClassify


# pytest
def test_question_classify():
    # question = "英雄的主演有谁"
    question = "章子怡演过哪些电影"
    question_classify = QuestionClassify()
    result = question_classify.predict(question)
    print(f"{question}的分类是：{result}")