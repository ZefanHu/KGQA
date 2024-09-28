from service.question_service import QuestionService

question_service = QuestionService()


class TestQuestionService():
    def test_get_answer0(self):
        question = "英雄的评分是多少呢"

        answer = question_service.get_answer(question)
        print(f"问题：{question} \n答案：{answer}")

    def test_get_answer1(self):
        question = "英雄是什么时候上映的呢"

        answer = question_service.get_answer(question)
        print(f"问题：{question} \n答案：{answer}")

    def test_get_answer2(self):
        question = "英雄是什么风格的电影呢"

        answer = question_service.get_answer(question)
        print(f"问题：{question} \n答案：{answer}")

    def test_get_answer3(self):
        question = "英雄的剧情是什么呢"

        answer = question_service.get_answer(question)
        print(f"问题：{question} \n答案：{answer}")

    def test_get_answer4(self):
        question = "英雄的演员有谁呢"

        answer = question_service.get_answer(question)
        print(f"问题：{question} \n答案：{answer}")
    # error
    def test_get_answer5(self):
        question = "章子怡的详细信息"

        answer = question_service.get_answer(question)
        print(f"问题：{question} \n答案：{answer}")

    def test_get_answer6(self):
        question = "章子怡演过的动作电影有哪些呢"

        answer = question_service.get_answer(question)
        print(f"问题：{question} \n答案：{answer}")

    def test_get_answer7(self):
        question = "章子怡演过哪些电影"

        answer = question_service.get_answer(question)
        print(f"问题：{question} \n答案：{answer}")

    def test_get_answer8(self):
        question = "章子怡演过的评分大于7分的电影有哪些"

        answer = question_service.get_answer(question)
        print(f"问题：{question} \n答案：{answer}")

    def test_get_answer9(self):
        question = "章子怡演过的评分小于5分的电影有哪些"

        answer = question_service.get_answer(question)
        print(f"问题：{question} \n答案：{answer}")
    # error
    def test_get_answer10(self):
        question = "章子怡演过哪些类型的电影"

        answer = question_service.get_answer(question)
        print(f"问题：{question} \n答案：{answer}")

    def test_get_answer11(self):
        question = "章子怡和成龙合作演过哪些电影呢"

        answer = question_service.get_answer(question)
        print(f"问题：{question} \n答案：{answer}")

    def test_get_answer12(self):
        question = "章子怡一个演过多少部电影呢"

        answer = question_service.get_answer(question)
        print(f"问题：{question} \n答案：{answer}")

    def test_get_answer13(self):
        question = "章子怡的出生日期是哪天呢"

        answer = question_service.get_answer(question)
        print(f"问题：{question} \n答案：{answer}")
