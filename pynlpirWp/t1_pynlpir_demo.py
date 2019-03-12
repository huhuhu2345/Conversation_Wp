# coding:utf-8

import sys
import pynlpir

pynlpir.open()

print("------------pynlpir 分词效果------------")
s = '聊天机器人到底该怎么做呢？'
segments = pynlpir.segment(s)
for segment in segments:
    print(segment[0], '\t', segment[1])

print("------------关键字提取------------")
key_words = pynlpir.get_key_words(s, weighted=True)
for key_word in key_words:
    print(key_word[0], '\t', key_word[1])


pynlpir.close()