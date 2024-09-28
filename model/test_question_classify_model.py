from model import question_classify_model
from model.question_classify_model import QuestionClassify

question_classify = QuestionClassify()


class TestQuestionClassifyModel:

    @classmethod
    def setup_class(cls):
        print()

    def test_load_train_data(self):
        train_x, train_y = question_classify_model.load_train_data()
        print(train_x)
        print(train_y)

    def test_question_classify0(self):
        question = "英雄的评分是多少呢"
        result = question_classify.predict(question)
        print(f"{question} category:{result}")
        assert result == 0

    def test_question_classify1(self):
        question = "英雄是什么时候上映的呢"

        result = question_classify.predict(question)
        print(f"{question} category:{result}")
        assert result == 1

    def test_question_classify2(self):
        question = "英雄是什么风格的电影呢"

        result = question_classify.predict(question)
        print(f"{question} category:{result}")
        assert result == 2

    def test_question_classify3(self):
        question = "英雄的剧情是什么呢"

        result = question_classify.predict(question)
        print(f"{question} category:{result}")
        assert result == 3

    def test_question_classify4(self):
        question = "英雄的演员有谁呢"

        result = question_classify.predict(question)
        print(f"{question} category:{result}")
        assert result == 4

    def test_question_classify5(self):
        question = "章子怡的详细信息"

        result = question_classify.predict(question)
        print(f"{question} category:{result}")
        assert result == 5

    def test_question_classify6(self):
        question = "章子怡演过哪些动作电影"

        result = question_classify.predict(question)
        print(f"{question} category:{result}")
        assert result == 6

    def test_question_classify7(self):
        question = "章子怡演过哪些电影"

        result = question_classify.predict(question)
        print(f"{question} category:{result}")
        assert result == 7

    def test_question_classify8(self):
        question = "章子怡演过的评分大于7分的电影有哪些"

        result = question_classify.predict(question)
        print(f"{question} category:{result}")
        assert result == 8

    def test_question_classify9(self):
        question = "章子怡演过的评分小于5分的电影有哪些"

        result = question_classify.predict(question)
        print(f"{question} category:{result}")
        assert result == 9

    def test_question_classify10(self):
        question = "章子怡燕娜哪些类型的电影"

        result = question_classify.predict(question)
        print(f"{question} category:{result}")
        assert result == 10

    def test_question_classify11(self):
        question = "章子怡和成龙合作演过哪些电影呢"

        result = question_classify.predict(question)
        print(f"{question} category:{result}")
        assert result == 11

    def test_question_classify12(self):
        question = "章子怡一个演过多少部电影呢"

        result = question_classify.predict(question)
        print(f"{question} category:{result}")
        assert result == 12

    def test_question_classify13(self):
        question = "章子怡的出生日期是哪天呢"

        result = question_classify.predict(question)
        print(f"{question} category:{result}")
        assert result == 13
