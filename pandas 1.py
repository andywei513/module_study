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
import seaborn as sns

#设置中文字体
mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei'] # 指定默认字体：解决plot不能显示中文问题
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

#读取本地excel文件
df = pd.read_excel('C://Users//ahuang3//Desktop//test.xlsx')

#使用numpy生成随机数据文件
df1 = pd.DataFrame(np.random.rand(50,4),columns=['a','b','c','d'])  #dataframe
ser1 = pd.Series(3*np.random.rand(4),index=['a','b','c','d'],name = 'series')  #列数据
df2 = pd.DataFrame(3*np.random.rand(4,2),index=['a','b','c','d'],columns = ['x','y'])  #dataframe
df3 = pd.DataFrame(np.random.randn(10, 4).cumsum(0), columns=list('ABCD'), index=np.arange(0, 100, 10))


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


#直方图
# t1 = np.random.normal(0,1,size=200)
# # t2 = np.random.normal(10,2,size = 200)
# # values = pd.Series(np.concatenate([t1,t2]))
# #
# # values.hist(bins =100,alpha =0.3,color = 'k',normed =True)
# # values.plot(kind = 'kde',style = 'k--')
# #
# # plt.xlabel('横轴')
# # plt.ylabel('纵轴')
# # # plt.xlim(0,10)        #设置x轴范围
# # # plt.ylim(0,20)       #设置Y轴范围
# # plt.title('测试')
# # plt.legend('分布')

#图表设置函数
# fig,axes = plt.subplots(1,2)
# df3.plot(ax=axes[0])
# df2.plot(ax=axes[1])

























plt.show()


