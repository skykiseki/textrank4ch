import jieba
import utils
from segment import WordSegment

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
        self.seg = None

    def analyze(self, sentences,
                delimiters=utils.sentence_delimiters,
                source='all_filters',
                path_stop_words=None,
                allow_pos=utils.allow_pos,
                is_lower=True):
        """


        Parameters:
        ----------

        Returns:
        -------


        """

        self.sentences = sentences
        self.delimiters = delimiters
        self.source = source
        self.allow_pos = allow_pos
        self.path_stop_words = path_stop_words
        self.is_lower = is_lower

        # 切分句子




