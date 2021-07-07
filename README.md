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



