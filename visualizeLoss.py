#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

#new.txt文本只包含loss值，
#格式为：冒号前面的数字代表迭代次数，后面的值为loss.
#1: 876.919922
#2: 4082.414795
#3: 439.612305
#4: 16130.901367

#为了更加清楚的观测loss值，隔10步画出该值。
result = pd.read_csv('/home/ld/desktop/shell/new.txt', skiprows=[x for x in range(100000) if x%10!=9] ,error_bad_lines=False, names=['loss'])
result['loss'] = result['loss'].str.split(' ').str.get(1)
result.head()
result.tail()

result['loss'] = result['loss'].convert_objects(convert_numeric=True)
result.dtypes
result['loss'].plot()
plt.savefig('loss')
plt.show()

