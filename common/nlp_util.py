import re

import jieba
import jieba.posseg

from common import constant


def posseg(text):
    """
    词性标注
    章子怡演过哪些电影
    example： [pair('章子怡', 'nr'), pair('演', 'v'), pair('过', 'ug'), pair('哪些', 'r'), pair('电影', 'n')]
    :return:
    """
    jieba.load_userdict(constant.DATA_DIR + "/userdict3.txt")
    # 清洗数据
    clean_text = re.sub("[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）]+", "", text)
    result = []
    question_word, qustion_flag = [], []
    # 分词
    text_cut = jieba.posseg.cut(clean_text)
    # for item in text_cut:
    #     temp_word = f"{item.word}/{item.flag}"
    #     result.append(temp_word)
    #     word, flag = item.word, item.flag
    #     question_word.append(word)
    #     qustion_flag.append(flag)
    return text_cut


def question_posseg(question):
    jieba.load_userdict(constant.DATA_DIR + "/userdict3.txt")
    clean_question = re.sub("[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）]+", "", question)
    # self.clean_question = clean_question
    question_seged = jieba.posseg.cut(str(clean_question))
    result = []
    question_word, question_flag = [], []
    for w in question_seged:
        temp_word = f"{w.word}/{w.flag}"
        result.append(temp_word)
        # 预处理问题
        word, flag = w.word, w.flag
        question_word.append(str(word).strip())
        question_flag.append(str(flag).strip())
    assert len(question_flag) == len(question_word)
    # self.question_word = question_word
    # self.question_flag = question_flag
    # print(result)
    return result
