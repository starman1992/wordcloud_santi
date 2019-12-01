import jieba.posseg as psg #中文分词工具
#如：psg.cut("还有什么是比jieba更好的中文分词工具呢？")
#还有/v 什么/r 是/v 比/p jieba/eng 更好/d 的/uj 中文/nz 分词/n 工具/n 呢/y ？/x

#根据词频降序排序
def 列表中的词频排序(lst):
    word_frequency = {}
    for word in lst:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
                
    word_sort = sorted(word_frequency.items(), key = lambda x:x[1], reverse = True)
    # 排序项目，按照关键字是'值'的数字顺序（匿名函数）来排倒序
    return word_sort
    
# 词云生成器
import numpy as np
from PIL import Image
from wordcloud import WordCloud,ImageColorGenerator,STOPWORDS
import  matplotlib.pyplot as plt

def 生成词云(lst):
    words_space_split = " ".join(lst) 
    # 设置停用词集合 
    sw = set(STOPWORDS) 
    sw.add("的")
    sw.add("这里不多写了，根据自己情况添加")
    # 图片模板和字体
    image=np.array(Image.open(r'.\111.jpg')) 
    font=r'C:\Windows\Fonts\STHUPO.TTF'
    fonttype=font.split('\\')[3].split('.')[0]
    # 生成词云
    my_wordcloud = WordCloud(scale=4, font_path=font, mask=image, stopwords=sw,
                             background_color = 'white', max_words = 200,
                             max_font_size = 60, random_state=20).generate(words_space_split) 
    # plt.imshow(my_wordcloud)
    # plt.axis("off") 
    # plt.show() 
    #保存生成的图片
    my_wordcloud.to_file(r'.\词云_%s.jpg'%fonttype)

if __name__ == "__main__":
    
    # 1. 打开存放项目名称的txt文件
    filename=r'.\111.txt'
    with open(filename, 'r') as f:
        content = (f.read())
        f.close()
    # 2. 分离出感兴趣的名词，放在 lst_words 里
    lst_words = list(set(content.split('，')))
    # for x in psg.cut(content):
        # # 保留名词、人名、地名，长度至少两个字
        # if x.flag in ['a', 'ad', 'an'] and len(x.word) > 1:
            # lst_words.append(x.word)
    # 3. 按照词频由大到小排序，放在 lst_sorted 的列表（元素是集合，(词,词频)）里     
    # lst_sorted = 列表中的词频排序(lst_words)
    # 4. 打印TOP10
    # print('\n序号\t名词\t词频\t柱图\n')
    # for i in range(10):
        # print( '{}\t{}\t{}\t{}\n'.format(i+1, lst_sorted[i][0], lst_sorted[i][1], '▂' * (lst_sorted[i][1] // 100)) )
    # 5. 生成词云
    生成词云(lst_words)
