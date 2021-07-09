import networkx as nx
import numpy as np

word_delimiters = ['!', '"', '#', '%', '&', '(', ')', '*', '+',
                   ',', '-', '.', '...', '......', '/', ':', ';',
                   '<', '=', '>', '?', '@', '[', ']', '^', '_',
                   '`', '{', '|', '}', '~', '，', '。', '。。。',
                   '。。。。。。', '！', '；', '？', '：', '、', '（', '）',
                   '\t', '\n']

sentence_delimiters = ['？', '?', '；', ';', '！', '!', '。', '……', '…', '\n']

allow_pos = ['an', 'nz', 'vn', 'v', 'vd', 'x', 'n', 'nt', 'nz', 'd']

def get_stop_words(path_stop_words):
    """

    Parameters:
    ----------
    path_stop_words: 停用词文件路径, 其中一行存储一个停用词

    Returns:
    -------
    stop_words: list, 停用词列表

    """
    stop_words = set()
    if path_stop_words:
        with open(path_stop_words, 'r') as fr:
            stop_words = set([word.strip().replace('\n', '') for word in fr.readlines()])

    return stop_words

def get_similarity(words1, words2):
    """
    计算句子之间的相似度

    公式: similarity = |A∩B| / (log(|A|) + log(|B|))

    Parameters:
    ----------
    words1: list, 词列表

    words2: list, 词列表

    Returns:
    -------
    sim_value: float, 句子之间的相似度
    """

    if len(words1) == 0 or len(words2) == 0:
        return 0

    sim_value = float(len(set(words1).intersection(set(words2))) / (np.log(len(words1)) + np.log(len(words2))))

    return sim_value


def get_key_sentences(sentences, words, sim_func=get_similarity):
    """
    基于TextRank方法对句子以及分词结果进行提取摘要

    Parameters:
    ----------
    sentences: list, 切分后的结果句子列表

    words: list, 切分后的结果词列表

    Returns:
    -------

    """
    len_sentences = len(sentences)

    # 先构造句子之间的无向权图, 整体为N*N的矩阵
    graph = np.zeros((len_sentences, len_sentences))

    # 计算权重, 权重由切词的相似度进行计算, 由于是无向的, a(ij) = a(ji)
    for i in range(len_sentences):
        for j in range(len_sentences):
            sim_value = sim_func(words[i], words[j])
            graph[i, j] = sim_value
            graph[j, i] = sim_value

    return 1