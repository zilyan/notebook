import jieba
import jieba.analyse as analyse #提取关键词的组件



#################jieba动态的增加词语

jieba_dict=['车标','电机舱','发动机','格栅','雨刮','大灯','行李箱','行车灯','底盘']
for d in jieba_dict:
    jieba.add_word(d)


