import utils
from segment import WordSegment, SentenceSegment

class TextRank4Sentence(object):
    """
    提取关键句

    Attributes:
    ----------
    sentences: list, 切分后的结果句子列表

    allow_pos: list, 切词时保留的词性

    path_stop_words: str, 停用词表路径

    punct: list, 剔除的特殊字符列表

    delimiters: list, 切句使用的特殊字符列表

    ws: class object, 用于切词的类

    ss: class object, 用于切句的类

    words_no_filters: list, 分词结果, 不剔除停用词、不剔除词性、

    words_stop_words_filters: list, 分词结果, 剔除停用词、不剔除词性

    words_flags_filters: list, 分词结果, 不剔除停用词, 剔除词性

    words_all_filters: list, 分词结果, 剔除停用词、剔除词性

    key_sentences: list, 提取的全量句子以及其权重(PR值)
    """
    def __init__(self):
        self.sentences = None
        self.allow_pos = None
        self.path_stop_words = None
        self.punct = None
        self.delimiters  = None
        self.ws = None
        self.ss = None

        self.words_no_filters = None
        self.words_stop_words_filters = None
        self.words_flags_filters = None
        self.words_all_filters = None

        self.key_sentences = None

    def analyze(self, text,
                punct=utils.word_delimiters,
                delimiters=utils.sentence_delimiters,
                source='all_filters',
                sim_func=utils.get_similarity,
                path_stop_words=None,
                allow_pos=utils.allow_pos,
                is_lower=True):
        """
        基于TextRank提取全量的句子以及其权重(PR值)


        Parameters:
        ----------
        text: str, 输入的文本

        punct: list, 剔除的特殊字符列表

        delimiters: list, 切句使用的特殊字符列表

        source: str, 最后用于提取摘要句计算PR时用的分词结果

        sim_func: function, 用于计算两个词列表的相似度函数, 支持用户自定义该函数, 格式为 func(list, list) -> float

        path_stop_words: str, 停用词表路径

        allow_pos: list, 切词时保留的词性

        is_lower: bool, 是否要转小写字母

        Returns:
        -------


        """
        self.punct = punct
        self.delimiters = delimiters
        self.allow_pos = allow_pos
        self.path_stop_words = path_stop_words

        self.ws = WordSegment(path_stop_words=self.path_stop_words,
                              allow_pos=self.allow_pos,
                              punct=self.punct)

        self.ss = SentenceSegment(delimiters=delimiters)

        # 切分句子, 这里会输出一个列表, 一个列表包含一个句子
        # PS:这里也处理了大小写转化
        self.sentences = self.ss.segment(content=text, use_is_lower=is_lower)

        # 对所有的句子开始切词, 其中要区分四种情况
        ## 1.no_filters, 不剔除停用词、不剔除词性、
        self.words_no_filters = self.ws.seg_sentences(sentences=self.sentences,
                                                      use_stop_words=False,
                                                      use_allow_pos=False)
        ## 2.stop_words_filters, 剔除停用词、不剔除词性
        self.words_stop_words_filters = self.ws.seg_sentences(sentences=self.sentences,
                                                              use_stop_words=True,
                                                              use_allow_pos=False)

        ## 3.flags_filters, 不剔除停用词, 剔除词性
        self.words_flags_filters = self.ws.seg_sentences(sentences=self.sentences,
                                                         use_stop_words=True,
                                                         use_allow_pos=False)

        ## 4.all_filters, 剔除停用词、剔除词性
        self.words_all_filters = self.ws.seg_sentences(sentences=self.sentences,
                                                       use_stop_words=True,
                                                       use_allow_pos=True)

        # 基于source决定输入的分词列表
        if source == 'no_filters':
            _words = self.words_no_filters
        elif source == 'stop_words_filters':
            _words = self.words_stop_words_filters
        elif source == 'flags_filters':
            _words = self.words_flags_filters
        else:
            ## all_filters作为兜底
            _words = self.words_all_filters

        self.key_sentences = utils.get_key_sentences(sentences=self.sentences,
                                                     words=_words,
                                                     sim_func=sim_func)








