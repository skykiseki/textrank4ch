import os
import sys

from .TextRank4Sentence import TextRank4Sentence
from .segment import WordSegment


if __name__ == '__main__':
    work_path = os.getcwd()
    path_stop_words = os.path.join(work_path, 'stop_words.txt')
    corpus = " 近日，云南省德宏州瑞丽市出现本土新冠肺炎疫情，瑞丽市疫情防控工作指挥部已经发布通告，从7月5日8时起，所有人员非必要不进出瑞丽；自7月6日12时起，将瑞丽市姐告国门社区调整为中风险地区，其他区域为低风险地区。鉴于云南省德宏州疫情变化形势，为严格落实“外防输入、内’防反弹”的防控策略，有效控制‘’和降''低疫情传播风险，市疾控中心向广大市民发出紧急提醒"

    t4ks = TextRank4Sentence()
    t4ks.analyze(text=corpus, source='no_filters')

    ws = WordSegment()
    ws.segment(content=corpus)
    print(ws.segment(content=corpus))

