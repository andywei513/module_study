# -*- coding: utf-8 -*-
# @Time    : 2018/4/5 12:23
# @Author  : Andywei
# @Email   : andycfa2@163.com
# @File    : matplotlib 1.py
# @Software: PyCharm


import matplotlib.pyplot as plt #显示图片
import pandas as pd
import numpy as np
from pylab import mpl #解决中文显示乱码
import seaborn as sns
from sklearn.datasets import load_iris #导入数据集
from pandas.tools.plotting import andrews_curves #调和曲线图使用
from pandas.tools.plotting import parallel_coordinates  #轮廓图
from pandas.tools.plotting import radviz  #高维点表现在二维平面的方法

# 高级绘图

#设置中文字体
mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei'] # 指定默认字体：解决plot不能显示中文问题
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

#读取本地excel文件
df = pd.read_excel('C://Users//ahuang3//Desktop//test.xlsx')
df1 = pd.DataFrame(10*np.random.randn(5,4),columns=['a','b','c','d'])

iris = pd.DataFrame(load_iris().data)
iris.columns=['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']
iris['Species'] = load_iris().target
#-----------------------------------------------------------------------------------------------------
# 简单散点图
# df1.plot(kind = 'scatter',x = 'a',y='b')


#用sns 散点图+直方图

# iris.plot(kind="scatter", x="SepalLengthCm", y="SepalWidthCm")
# sns.jointplot(x="SepalLengthCm", y="SepalWidthCm", data=iris, size=5)
#sns.FacetGrid(iris, hue="Species", size=5).map(plt.scatter, "SepalLengthCm", "SepalWidthCm").add_legend()

#箱线图
# sns.boxplot(x="Species", y="PetalLengthCm", data=iris)

#箱线图上加散点图
# ax = sns.boxplot(x="Species", y="PetalLengthCm", data=iris)
# ax = sns.stripplot(x="Species", y="PetalLengthCm", data=iris, jitter=True, edgecolor="red") # 使振动值jitter=True 使各个散点分开，要不然会是一条直线

#小提琴图
# sns.violinplot(x="Species", y="PetalLengthCm", data=iris, size=6)

#kdeplot
# sns.FacetGrid(iris, hue="Species", size=6).map(sns.kdeplot, "PetalLengthCm").add_legend()

#pairplot
# sns.pairplot(iris, hue="Species", size=3)
# sns.pairplot(iris, hue="Species", size=2, diag_kind="kde") #对角线改成kde

#不同种类的箱线图
# iris.boxplot(by="Species", figsize=(12, 6))

#调和曲线图
# andrews_curves(iris, "Species")


#轮廓图
# parallel_coordinates(iris, "Species")

#radviz
radviz(iris, "Species")


plt.show()