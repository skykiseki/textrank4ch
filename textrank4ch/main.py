from segment import WordSegment
import os
import jieba
import jieba.analyse

if __name__ == '__main__':
    work_path = os.getcwd()
    word_seg = WordSegment(path_stop_words=os.path.join(work_path, 'stop_words.txt'))
    ss = ["""我是帅哥嗯,哈哈哈哈哈!哈哈哈哈 APP""", """我是帅哥嗯,哈哈哈哈哈!哈哈哈哈 APP"""]
    print(jieba.analyse.extract_tags('.'.join(ss), withWeight=True, withFlag=True))