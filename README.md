# textrank4ch

参考以下内容进行学习和开发
1. [TextRank4ZH](https://github.com/someus/TextRank4ZH)
2. [TextRank Bringing Order into Texts](http://web.eecs.umich.edu/~mihalcea/papers/mihalcea.emnlp04.pdf)



    原来的TextRank4ZH，都近5年莫得更新了！~~
    个人感觉这个包还不错，当前项目里也在使用，只不过这个包有不少体验不好的地方

    比如：  
    1.句子分词会直接删除x类型，但是自定义词库不少人是只填了个词的，这个情况下词性为x,最终textrank4zh就把这个词删了。  
    2.还有一些比如内部计算pagerank(默认最大迭代次数为100)时候会偶尔发生不收敛的情况, 这个异常也是没有捕捉处理的。

    既然没更新了，我就想着参考（chao xi）着开发优化更新一下咯，毕竟自己工作中也在用。
    竟然连名字都差不多, 希望那个大佬知道了不要打我


# 安装说明

```shell
pip install textrank4ch
```

# 使用说明
```python
# 加载模块
from textrank4ch.TextRank4Keyword import TextRank4Keywords
    
# 准备预料, 输入时一个字符长串, 可含特殊字符
corpus =  "近日，云南省德宏州瑞丽市出现本土新冠肺炎疫情，瑞丽市疫情防控工作指挥部已经发布通告，从7月5日8时起，所有人员非必要不进出瑞丽；自7月6日12时起，将瑞丽市姐告国门社区调整为中风险地区，其他区域为低风险地区。鉴于云南省德宏州疫情变化形势，为严格落实“外防输入、内防反弹”的防控策略，有效控制和降低疫情传播风险，市疾控中心向广大市民发出紧急提醒"

# 对输入进行分析、得到全量的关键词相关信息, 如权重(PR)、词性
t4kw = TextRank4Keywords()
t4kw.analyze(text=ss, path_stop_words=path_stop_words)
    
# 再基于上述analyze的结果进行按需提取需要的关键字
print(t4kw.get_keywords(3))
```

# 最终结果
[('疫情', 1.0, 'n'), ('风险', 0.6103855610600728, 'n'), ('防控', 0.5632699906648398, 'vn')]




