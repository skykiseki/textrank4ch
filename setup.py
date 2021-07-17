# -*- coding: utf-8 -*-
from setuptools import setup

LONGDOC = """
我家还蛮大的, 欢迎你们来我家van.

https://github.com/skykiseki

textrank4ch
====

"基于textrank的关键字摘取与摘要句摘取", 


具体textrank的知识参考, 我个人觉得还不错:     
[《PageRank 笔记》](https://clvsit.blog.csdn.net/article/details/90322422)
[《textrank提取关键词与关键句》](https://blog.csdn.net/weixin_40746796/article/details/89963268)


完整文档见 ``README.md``

GitHub: https://github.com/skykiseki/textrank4ch
"""

setup(name='textrank4ch',
      version='1.2.0',
      description='Key words extracting and Key sentences extracting',
      long_description=LONGDOC,
      long_description_content_type="text/markdown",
      author='Wei, Zhihui',
      author_email='evelinesdd@qq.com',
      url='https://github.com/skykiseki/textrank4ch',
      license="MIT",
      classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Natural Language :: Chinese (Simplified)',
        'Natural Language :: Chinese (Traditional)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Indexing',
        'Topic :: Text Processing :: Linguistic',
      ],
      python_requires='>=3.6',
      install_requires=[
        'pandas',
        'numpy',
        'jieba',
        'networkx'
      ],
      keywords='NLP,Chinese,Chinese words,textrank',
      packages=['textrank4ch'],
      package_dir={'textrank4ch':'textrank4ch'}
)