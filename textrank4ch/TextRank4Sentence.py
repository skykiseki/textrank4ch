import jieba
import utils
from segment import WordSegment, SentenceSegment

class TextRank4Sentence(object):
    """
    提取关键句

    Attributes:
    ----------

    """
    def __init__(self):
        self.sentences = None
        self.allow_pos = None
        self.path_stop_words = None
        self.is_lower = None
        self.source = None
        self.delimiters  = None
        self.ss = SentenceSegment()

    def analyze(self, text,
                delimiters=utils.sentence_delimiters,
                source='all_filters',
                path_stop_words=None,
                allow_pos=utils.allow_pos,
                is_lower=True):
        """


        Parameters:
        ----------
        sentences
        Returns:
        -------


        """

        self.sentences = text
        self.delimiters = delimiters
        self.source = source
        self.allow_pos = allow_pos
        self.path_stop_words = path_stop_words
        self.is_lower = is_lower

        # 切分句子, 这里会输出一个列表, 一个列表包含一个句子
        sentences = self.ss.segment(content=text)

        #




