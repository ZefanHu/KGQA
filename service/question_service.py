from model import question_classify_model
from model import question_template

class QuestionService:
    """
    问答核心类，接收自然问句，匹配查询语句，输出答案
    """
    def __init__(self):
        self.classify_model = question_classify_model.QuestionClassify()
        self.template = question_template.QuestionTemplate()

    def get_answer(self, question):
        pass
        # 通过分类器获取分类

        # 根据分类获取模板，查询得到答案

