# -*- coding: utf-8 -*-
# @Time    : 2018/4/5 18:45
# @Author  : Andywei
# @Email   : andycfa2@163.com
# @File    : matplotlib 2.py
# @Software: PyCharm


import matplotlib.pyplot as plt #显示图片
import pandas as pd
import numpy as np
from pylab import mpl #解决中文显示乱码
import seaborn as sns
from sklearn.datasets import load_iris #导入数据集




#设置中文字体
mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei'] # 指定默认字体：解决plot不能显示中文问题
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题



#复杂图像
'''
t = np.arange(-1, 2, .01)
s = np.sin(2 * np.pi * t)

plt.plot(t,s)

l = plt.axhline(linewidth=4, color='r')    #y=0的水平线 颜色红色
l = plt.axhline(y=1, color='b')       #y=1的水平线
l = plt.axvline(x=0, ymin=0, linewidth=4, color='b') #x=0的垂直线
l = plt.axhline(y=.5, xmin=0.25, xmax=0.75)  #y=0.5的水平线
p = plt.axhspan(0.25, 0.75, facecolor='0.5', alpha=0.5) #条状图
p = plt.axvspan(1.25, 1.55, facecolor='g', alpha=0.5)
plt.axis([-1, 2, -1, 2])
plt.show()
'''

# n = np.array([0,1,2,3,4,5])
# x = np.linspace(-0.75, 1., 100)
#
# fig, axes = plt.subplots(1, 4, figsize=(12,3))
#
# axes[0].scatter(x, x + 0.25*np.random.randn(len(x)))
#
# axes[1].step(n, n**2, lw=2)
#
# axes[2].bar(n, n**2, align="center", width=0.5, alpha=0.5)
#
# axes[3].fill_between(x, x**2, x**3, color="green", alpha=0.5)




#subplots创建多个子图方法 四种
#---------------------#方法一  用axes--------------------------------------------------

# x = np.arange(0, 100)
# fig,axes=plt.subplots(2,2)
# ax1=axes[0,0]
# ax2=axes[0,1]
# ax3=axes[1,0]
# ax4=axes[1,1]
#
# #作图1
# ax1.plot(x, x)
# #作图2
# ax2.plot(x, -x)
#  #作图3
# ax3.plot(x, x ** 2)
# ax3.grid(color='r', linestyle='--', linewidth=1,alpha=0.3)
# #作图4
# ax4.plot(x, np.log(x))
#-----------------------#方法2  用subplot（121）---------------------------------------
# x = np.arange(1, 100)
# #作图1
# plt.subplot(221)
# plt.plot(x, x)
# #作图2
# plt.subplot(222)
# plt.plot(x, -x)
#  #作图3
# plt.subplot(223)
# plt.plot(x, x ** 2)
# plt.grid(color='r', linestyle='--', linewidth=1,alpha=0.3)
# #作图4
# plt.subplot(224)
# plt.plot(x, np.log(x))
#------------------------------方法3 add_subplot新增子图 面向figure------------------------
x = np.arange(0, 100)
#新建figure对象
fig=plt.figure()
#新建子图1
ax1=fig.add_subplot(2,2,1)
ax1.plot(x, x)
#新建子图3
ax3=fig.add_subplot(2,2,3)
ax3.plot(x, x ** 2)
ax3.grid(color='r', linestyle='--', linewidth=1,alpha=0.3)
#新建子图4
ax4=fig.add_subplot(2,2,4)
ax4.plot(x, np.log(x))

#------------------------------方法4  add_axes新增子区域------------------------------------

# #新建figure
# fig = plt.figure()
# # 定义数据
# x = [1, 2, 3, 4, 5, 6, 7]
# y = [1, 3, 4, 2, 5, 8, 6]
# #新建区域ax1
# #figure的百分比,从figure 10%的位置开始绘制, 宽高是figure的80%
# left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
# # 获得绘制的句柄
# ax1 = fig.add_axes([left, bottom, width, height])
# ax1.plot(x, y, 'r')
# ax1.set_title('区域1')
#
# #新增区域ax2,嵌套在ax1内
# left, bottom, width, height = 0.2, 0.6, 0.25, 0.25
# # 获得绘制的句柄
# ax2 = fig.add_axes([left, bottom, width, height])
# ax2.plot(x,y, 'b')
# ax2.set_title('区域2')


plt.show()