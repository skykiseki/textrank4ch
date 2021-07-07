
word_delimiters = ['!', '"', '#', '%', '&', '(', ')', '*', '+',
                   ',', '-', '.', '...', '......', '/', ':', ';',
                   '<', '=', '>', '?', '@', '[', ']', '^', '_',
                   '`', '{', '|', '}', '~', '，', '。', '。。。',
                   '。。。。。。', '！', '；', '？', '：', '、', '（', '）',
                   '\t', '\n']

sentence_delimiters = ['?', '!', ';', '？', '！', '。', '；', '……', '…', '\n']

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
