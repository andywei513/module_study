# -*- coding: utf-8 -*-
# @Time    : 2018/4/5 12:22
# @Author  : Andywei
# @Email   : andycfa2@163.com
# @File    : pandas 1.py
# @Software: PyCharm


# pandas 绘图练习
import matplotlib.pyplot as plt #显示图片
import pandas as pd
import numpy as np
from pylab import mpl #解决中文显示乱码

#设置中文字体
mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei'] # 指定默认字体：解决plot不能显示中文问题
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

#读取本地excel文件
df = pd.read_excel('C://Users//ahuang3//Desktop//test.xlsx')

#使用numpy生成随机数据文件
df1 = pd.DataFrame(np.random.rand(50,4),columns=['a','b','c','d'])  #dataframe
ser1 = pd.Series(3*np.random.rand(4),index=['a','b','c','d'],name = 'series')  #列数据
df2 = pd.DataFrame(3*np.random.rand(4,2),index=['a','b','c','d'],columns = ['x','y'])  #dataframe


#绘图参数设置

# df.plot() #无参数默认形式

#柱状图
# df.plot(kind = 'bar')


#散点图
           #单一散点图
#df1.plot.scatter(x = 'a',y='b')
       # 不同散点绘制到一张表
# ab = df1.plot.scatter(x='a',y='b',color = 'DarkBlue',label = 'Group1')
# abc = df1.plot.scatter(x='c',y='d',color = 'DarkGreen',label = 'Group2',ax=ab)
# abcd = df1.plot.scatter(x='a',y='c',color = 'DarkRed',label = 'Group3',ax=abc)
# df1.plot.scatter(x='b',y='d',color = 'DarkGray',label = 'Group4',ax=abcd)
          #设置点大小和灰度水平
# df1.plot.scatter(x='b',y='d',c = 'c',s = 50)
# df1.plot.scatter(x='a',y='b',s = df1['c']*200)


#饼状图
# ser1.plot.pie(figsize=(6,6)) #单一列
# ser1.plot.pie(labels = ['AA','BB','CC','DD'],colors = ['r','g','b','c'],autopct = '%.1f',fontsize = 10) # '%.1f'设置小数点位数
# df2.plot.pie(subplots = True,figsize = (12,6)) #多列数据

























plt.show()


