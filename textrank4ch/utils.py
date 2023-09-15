import networkx as nx
import numpy as np

word_delimiters = ['!', '"', '#', '%', '&', '(', ')', '*', '+',
                   ',', '-', '.', '...', '......', '/', ':', ';',
                   '<', '=', '>', '?', '@', '[', ']', '^', '_',
                   '`', '{', '|', '}', '~', '，', '。', '。。。',
                   '。。。。。。', '！', '；', '？', '：', '、', '（', '）',
                   '\t', '\n', '”', '’' , '“', '‘', "'"]

sentence_delimiters = ['？', '?', '；', ';', '！', '!', '。', '……', '…', '\n']

allow_pos = ['an', 'nz', 'vn', 'v', 'vd', 'x', 'n', 'nt', 'd']

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

    # 注意, 这里假设认为整个句式只有一个词的时候是无法对比相似度的
    if len(words1) <= 1 or len(words2) <= 1:
        sim_value = 0
    else:
        sim_value = float(len(set(words1).intersection(set(words2))) / (np.log(len(words1)) + np.log(len(words2))))

    return sim_value


def sort_sentences(sentences, words,
                   sim_func=get_similarity,
                   pagerank_config=None,
                   pr_error_handle='both'):
    f"""
    基于TextRank方法对句子以及分词结果进行提取摘要

    Parameters:
    ----------
    sentences: list, 切分后的结果句子列表

    words: list, 切分后的结果词列表

    pagerank_config: dict, networkx.pagerank的参数字典

    pr_error_handle: str, pagerank不收敛的时候的处理策略,
    iterator:增加迭代轮次（兜底）, 
    tolerance:增加迭代轮次前后的差值阈值
    both:增加迭代轮次的同时增加迭代轮次前后的差值阈值

    Returns:
    -------
    list_res: list, 结果列表
    """
    list_res = []

    # 默认的PR收敛时的参数
    pr_alpha = 1
    pr_max_iter = 200
    pr_tol = 1e-6

    if pagerank_config is None:
        pagerank_config = {'alpha': pr_alpha,
                           'max_iter': pr_max_iter,
                           'tol': pr_tol}

    len_sentences = len(sentences)

    # 初始化句子之间的无向权图, 整体为N*N的矩阵
    graph = np.zeros((len_sentences, len_sentences))

    # 计算权重, 权重由切词的相似度进行计算, 由于是无向的, a(ij) = a(ji)
    for i in range(len_sentences):
        for j in range(len_sentences):
            sim_value = sim_func(words[i], words[j])
            graph[i, j] = sim_value
            graph[j, i] = sim_value

    # 构造无向权图
    nx_graph = nx.from_numpy_array(graph)

    # 计算PR值, 注意, 初始参数在计算PR值时可能不收敛, 这个时候可以
    flag = True

    while flag:
        # noinspection PyBroadException
        try:
            ## 开始计算PR值, 可能存在不收敛的情况
            pr_values = nx.pagerank(nx_graph, **pagerank_config)
            ## 成功收敛则停止循环
            flag = False

        except Exception:
            ## 如果PR不收敛, 以提升迭代前后轮次之间的差值为策略
            if pr_error_handle == 'tolerance':
                pr_tol *= 10
            ## 以提升迭代轮次作为策略
            elif pr_error_handle == 'iterator':
                pr_max_iter += 100
            ## 两者同时进行
            else:
                pr_tol *= 10
                pr_max_iter += 100

            pagerank_config = {'alpha': pr_alpha,
                               'max_iter': pr_max_iter,
                               'tol': pr_tol}

    # pr_values: 一个dict, {index:pr, index:pr}
    for idx, val in sorted(pr_values.items(), key=lambda x: x[1], reverse=True):
        list_res.append({'sentence': sentences[idx],
                         'weight': val,
                         'index':idx})

    return list_res

