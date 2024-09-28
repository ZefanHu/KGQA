import traceback

from common import nlp_util, log_util
from model.question_classify_model import QuestionClassify
from model.question_template import QuestionTemplate

log = log_util.get_main_logger()
class QuestionService:
    """
    问答核心类，接受问题输入，构造查询语句，输出查询结果
    """

    def __init__(self):
        print()
        self.classify_model = QuestionClassify()
        self.question_template = QuestionTemplate()

    def get_answer(self, question):
        print()
        # 通过分类器获取分类
        question_category = self.classify_model.predict(question)
        print(f"{question}的分类是：{question_category}")
        # self.classify_model.get_question_category_desc(question_category)
        try:
            answer = self.question_template.get_question_answer(question, question_category)
        except BaseException as e:
            traceback.print_exc()
            answer = "我也还不知道！"
        # answer = self.questiontemplate.get_question_answer(self.pos_quesiton, self.question_template_id_str)
        return answer

question_service_instant = QuestionService()