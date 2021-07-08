import jieba
import utils

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

    def analyze(self, sentences,
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
        self.source = source
        self.allow_pos = allow_pos
        self.path_stop_words = path_stop_words
        self.is_lower = is_lower





