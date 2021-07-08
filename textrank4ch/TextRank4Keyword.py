import jieba.analyse
import jieba
import utils

class TextRank4Keywords(object):
    """
    提取关键字

    这里直接改造成引用jieba的textrank结果, 不再有逻辑分岔, 且集成了停用词路径等参数

    Attributes:
    ----------
    path_stop_words: str, 停用词表路径
    text: str, 文本字符串
    is_lower: bool, 是否要转小写字母
    keywords: 关键字列表, 一个元素包含关键词(必选), 词性(可选), 权重(可选)
    """
    def __init__(self):
        self.path_stop_words = None
        self.text = None
        self.is_lower = None
        self.keywords = None
        self.allow_pos = None

    def analyze(self, text, path_stop_words=None, allow_pos=utils.allow_pos, is_lower=True):
        """
        对文本进行分析, 找出所有的关键词候选列表

        Parameters:
        ----------
        text: str, 文本字符串
        path_stop_words: str, 停用词表路径
        is_lower: bool, 是否要转小写字母

        Returns:
        -------
        self

        """
        self.path_stop_words = path_stop_words
        self.text = text
        self.is_lower = is_lower
        self.allow_pos = allow_pos

        if self.is_lower:
            self.text = self.text.strip().replace(" ", "").lower()

        if path_stop_words:
            jieba.analyse.set_stop_words(stop_words_path=path_stop_words)

        self.keywords = jieba.analyse.textrank(sentence=self.text,
                                               topK=None,
                                               allowPOS=self.allow_pos,
                                               withWeight=True,
                                               withFlag=True)

    def get_keywords(self, top_k=6, word_min_len=1, with_weight=True, with_flag=False):
        """
        获取需要的关键词

        Parameters:
        ----------
        top_k: int, 获取topN权重的词
        word_min_len: int, 获取大于等于长度阈值的关键词
        with_weight: bool, 是否要带着权重(PR值)进行输出
        with_flag: bool, 是否要带着词性进行输出

        Returns:
        -------
        关键词列表

        """
        list_res = []

        words = [item[0].word for item in self.keywords if len(item[0].word) >= word_min_len]
        weights = [item[1] for item in self.keywords if len(item[0].word) >= word_min_len]
        flags = [item[0].flag for item in self.keywords if len(item[0].word) >= word_min_len]

        list_res.append(words)

        if with_weight:
            list_res.append(weights)

        if with_flag:
            list_res.append(flags)

        return list(zip(*list_res))[:top_k]

