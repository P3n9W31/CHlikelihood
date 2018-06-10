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

```

