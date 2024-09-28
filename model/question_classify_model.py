import os.path
import re

import jieba
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

from common import file_util, constant, nlp_util


class QuestionClassify:
    def __init__(self):
        print()
        self.train_x, self.train_y = load_train_data()
        # 文本向量化
        self.tfidf_vec = TfidfVectorizer()
        self.train_vec = self.tfidf_vec.fit_transform(self.train_x).toarray()
        # 训练模型
        self.model = self.train_model_nb()
        # 初始化问题模板
        self.init_question_category_desc()

    def train_model_nb(self):
        """
        利用朴素贝叶斯分类器训练模型
        :return:
        """
        # print(f"训练向量: {self.train_vec}")  # 添加调试信息
        # print(f"训练标签: {self.train_y}")  # 添加调试信息

        nb = MultinomialNB(alpha=0.01)
        nb.fit(self.train_vec, self.train_y)
        return nb

    def predict(self, question):
        # 词性标注
        text_cut_gen = nlp_util.posseg(question)
        # 获取模板
        # 原始问题
        text_src_list = []
        # 一般化的问题，把人名替换为nr，依此类推
        text_normal_list = []
        for item in text_cut_gen:
            text_src_list.append(item.word)
            if item.flag in ['nr', 'nm', 'nnt']:
                text_normal_list.append(item.flag)
            else:
                text_normal_list.append(item.word)
        question_normal = [" ".join(text_normal_list)]

        question_vector = self.tfidf_vec.transform(question_normal).toarray()
        # print(f"Question Vector: {question_vector}")
        predict = self.model.predict(question_vector)[0]
        # print(f"预测值: {predict}")
        return predict

    def init_question_category_desc(self):
        # 读取问题模板
        with(open(constant.DATA_DIR + "/question/question_classification.txt", "r", encoding="utf-8")) as f:
            question_mode_list = f.readlines()
        self.question_mode_dict = {}
        for one_mode in question_mode_list:
            # 读取一行
            mode_id, mode_str = str(one_mode).strip().split(":")
            # 处理一行，并存入
            self.question_mode_dict[int(mode_id)] = str(mode_str).strip()

    def get_question_category_desc(self, category):
        return self.question_mode_dict[category]


def load_train_data():
    train_x = []
    train_y = []
    file_path_list = file_util.get_file_list(os.path.join(constant.DATA_DIR, "question"))

    for file_item in file_path_list:
        # 从文件名中查找【数字】部分作为标签，只匹配【】中的数字
        label_match = re.search(r'【(\d+)】', file_item)
        if label_match:
            label_num = int(label_match.group(1))
            # 打印以检查标签值
            # print(f"文件: {file_item}, 标签: {label_num}")

            # 读取文件内容
            with open(file_item, "r", encoding="utf-8") as file:
                lines = file.readlines()
                for line in lines:
                    # 分词
                    word_list = list(jieba.cut(str(line).strip()))
                    train_x.append(" ".join(word_list))
                    train_y.append(label_num)
        else:
            print(f"警告: 文件 {file_item} 中未找到标签")
    return train_x, train_y

# 调用加载数据的方法来确认标签加载正确
train_x, train_y = load_train_data()
# print(f"训练标签列表: {train_y}")
