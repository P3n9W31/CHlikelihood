# CHlikelihood
[![PyPI version](https://badge.fury.io/py/Chlikelihood.svg)](https://badge.fury.io/py/Chlikelihood)
[![license](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/ZhanPwBibiBibi/CHlikelihood/blob/master/LICENSE.md)

一个用于比较两个中文句子相似度的工具

## 安装方法
```python
pip install Chlikelihood
```

## 使用方法

```python
from CHlikelihood.likelihood import Likelihood

a = Likelihood()
a.likelihood('很高兴见到你','我也很高兴见到你')
>>>0.8164965809277261
```

## 原理
### 分词

很高兴见到你,我也很高兴见到你

划分为

很/高兴/见到/你,我/也/很/高兴/见到/你

### 汇总所有出现过的词

['高兴', '也', '你', '我', '很', '见到']
### 计算两个句子的词频

句子1: 高兴：1，也：0，你：1，我：0，很：1，见到：1
句子2: 高兴：1，也：1，你：1，我：1，很：1，见到：1
### 完成句子到向量的转化

句子1:[1，0，1，0，1，1]
句子2:[1，1，1，1，1，1]
### 计算余弦相似度

```python
>>>0.8164965809277261
```








