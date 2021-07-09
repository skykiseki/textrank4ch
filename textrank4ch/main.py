from segment import WordSegment, SentenceSegment
import os
import re
import utils
import math


def get_similarity(word_list1, word_list2):
    """默认的用于计算两个句子相似度的函数。
    Keyword arguments:
    word_list1, word_list2  --  分别代表两个句子，都是由单词组成的列表
    """
    words = list(set(word_list1 + word_list2))
    vector1 = [float(word_list1.count(word)) for word in words]
    vector2 = [float(word_list2.count(word)) for word in words]

    vector3 = [vector1[x] * vector2[x] for x in range(len(vector1))]
    vector4 = [1 for num in vector3 if num > 0.]
    co_occur_num = sum(vector4)

    print(words)
    print(vector1, vector2)
    print(vector3, vector4)
    print(co_occur_num)

    if abs(co_occur_num) <= 1e-12:
        return 0.

    denominator = math.log(float(len(word_list1))) + math.log(float(len(word_list2)))  # 分母

    if abs(denominator) < 1e-12:
        return 0.

    return co_occur_num / denominator

if __name__ == '__main__':
    work_path = os.getcwd()
    path_stop_words = os.path.join(work_path, 'stop_words.txt')
    word_seg = WordSegment(path_stop_words=path_stop_words)
    ss = " 近日，   云南省德宏州瑞丽市出现本土新冠肺炎疫情，瑞丽市疫情防控工作指挥部已经发布通告，从7月5日8时起，所有人员非必要不进出瑞丽；；！；!；自7月6日12时起，将瑞丽市姐告国门社区调整为中风险地区，其他区域为低风险地区。鉴于云南省德宏州疫情变化形势，为严格落实“外防输入、内防反弹”的防控策略，有效控制和降低疫情传播风险，市疾控中心向广大市民发出紧急提醒"

    a = ['c','a', 'a']
    b = ['d', 'c', 'a', 'a', 'a']
    print(get_similarity([], b))

    print(utils.get_similarity([], b))

