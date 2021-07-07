import jieba.posseg as pseg
import utils

class WordSegment(object):
    """
    用于切词的类, 因为基于jieba分词, 所以需要提前load_userdict加载自定义词库

    Attributes:
    ----------
    stop_words: 停用词列表
    allow_pos: 选用的词性列表
    punct: 剔除的特殊字符列表
    is_lower: 是否转换英文为小写
    """

    def __init__(self, path_stop_words=None, allow_pos=None, punct=utils.word_delimiters, is_lower=True):
        self.stop_words = utils.get_stop_words(path_stop_words=path_stop_words)
        self.allow_pos = allow_pos
        self.punct = punct
        self.is_lower = is_lower

    def segment(self, content):
        """
        对单个句子进行分词, 其中包含四种分词结果（用于后面抽取摘要的相似值计算）

        Parameters:
        ----------
        content: str, 输入的文本, 可包含特殊字符

        Returns:
        -------
        list_words: list, 分词结果列表
        """
        # 先剔除空格符
        content = content.replace(" ", "")

        # 转化大小写
        if self.is_lower:
            content = content.lower()

        # pseg切出词和词性, 其中剔除特殊字符
        pseg_res = [item for item in pseg.lcut(content) if item.word not in self.punct and item.word]

        # 剔除停用词, 这里停用词可能是空集
        pseg_res = [item for item in pseg_res if item.word not in self.stop_words]

        # 剔除词性, None的时候则保留全词, 否则筛选对应的词性
        if self.allow_pos:
            pseg_res = [item for item in pseg_res if item.flag in self.allow_pos]

        list_words = [item.word for item in pseg_res]

        return list_words



