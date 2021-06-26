import pandas as pd
import numpy as np
import re
import string
from zhon.hanzi import punctuation

import jxys

#提取原始数据集
tdata = pd.read_excel('原始数据集.xlsx')
data = tdata.loc[:,['评论']].values
print("原始数据长度：" + str(len(data)))

#评论去重
data1 =  np.unique(data)
print("评论去重后数据长度：" + str(len(data1)))

#评论机械压缩   详见模块：jxys.py
# data11 = jxys.jxys(data1)
# print(data11)

#去掉过短的评论与默认评论：“此用户没有填写评论!”
data2 = []
for d in data1:
    if len(d) > 2:
        data2.append(d)
data2.remove('此用户没有填写评论!')
print("去部分评论后数据长度：" + str(len(data2)))
#print(data2)

#去掉中文标点与表情
data3 = []
for d in data2:
    comment = re.sub(r"[%s]+" %punctuation, "",d)
    comment = str(bytes(comment, encoding='utf-8').decode('utf-8').encode('gbk', 'ignore').decode('gbk'))
    data3.append(comment)
#print(data3)

#保存数据
df = pd.DataFrame()
df['data'] = data3
df.to_csv('newData.csv',index=False,encoding = 'utf-8')