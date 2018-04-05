# -*- coding: utf-8 -*-
# @Time    : 2018/4/5 12:22
# @Author  : Andywei
# @Email   : andycfa2@163.com
# @File    : numpy 1.py
# @Software: PyCharm

import numpy as np

#生成【0,1）之间浮点数
x = np.random.random_sample(size=(2,2))
# np.random.random(size=None)
# np.random.ranf(size=None)
# np.random.sample(size=None

#设置相同的seed，每次生成的随机数相同
y = np.random.seed(1)
y = np.random.rand(5)

# range and arange
z = np.arange(1,5)  #1,2,3,4
m = range(1,5) #range对象


