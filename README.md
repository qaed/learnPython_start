# learnPython_start

## 《“笨办法”学Python》（learn python the hard way 3th）

### ex1 第一个程序
使用 `print()` 简单输出一些东西<br>
Python3 中取消了 `print "xxxxx"` 这样的用法<br>
改为使用 `print()` 函数,如： `print("xxxx")`

### ex2 注释和井号
`#`号后面的就是注释

### ex3 数字和数学计算
```python
# + plus 加号
# - minus 减号
# / slash 斜杠
# * asterisk 星号
# % percent 百分号
# < less-than 小于号
# > greater-than 大于号
# <= less-than-equal 小于等于号
# >= greater-than-equal 大于等于号
```
### ex4 变量(variable)和命名
```python
cars = 100
space_in_a_car = 4.0
```

| 格式化符号        | 说明           | 
| ------------- |-------------:|
|%c | 转换成字符（ASCII 码值，或者长度为一的字符串） |
|%r | 优先用repr()函数进行字符串转换（Python2.0新增）|
|%s | 优先用str()函数进行字符串转换| 
|%d / %i | 转成有符号十进制数| 
|%u | 转成无符号十进制数| 
|%o | 转成无符号八进制数| 
|%x / %X | (Unsigned)转成无符号十六进制数（x / X 代表转换后的十六进制字符的大小写）| 
|%e / %E | 转成科学计数法（e / E控制输出e / E）| 
|%f / %F | 转成浮点数（小数部分自然截断）| 
|%g / %G | %e和%f / %E和%F 的简写| 
|%%| 输出%| 

### ex5 更多的变量和打印
```python
my_name = 'Zed A. Shaw'
print("Let's talk about %s." % my_name)
```
### ex6 字符串(string)和文本
```python
x = "There are %d types of people." % 10
y = "Those who know %s and those who %s." % (binary,do_not)
# %r保存原本格式输出，x是字符串。自带双引号
print("I said : %r." % x)
# %s输出字符串，y是字符串，相当于“+”操作
print("I also said : '%s'." % y)
```
### ex7 更多打印
```python
# 输出10次"."
print("." * 10) 
print("hello", end = " ")# 输出不换行
print("world")
```
### ex8 打印，打印
```python
formatter = "%r %r %r %r"
print(formatter % (1, 2, 3, 4))
print(formatter % ("one", "tow", "three", "four"))
print(formatter % (True, False, False, True))
print(formatter % (formatter, formatter, formatter, formatter))
print(formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
))# 这一行输出既有单引号又有双引号

# 输出
# 1 2 3 4
# 'one' 'two' 'three' 'four'
# True False False True
# '%r %r %r %r' '%r %r %r %r' '%r %r %r %r' '%r %r %r %r'
# 'I had this thing.' 'That you could type up right.' "But it didn't sing." 'So I said goodnight.'
```

### ex9 打印，打印，打印
```python
print("""
xxx
xxx
xxx
输出多行字符串
""")
```
### ex10 那是什么？

| 转义字符        | 说明           | 
| ------------- |-------------:|
|\' |单引号 |
|\" |双引号 |
|\a |发出系统响铃声 | 
|\b |退格符| 
|\n |换行符 | 
|\t |横向制表符 | 
|\v |纵向制表符 | 
|\r|回车符 | 
|\f|换页符| 
|\o|八进制数代表的字符 | 
|\x|十六进制数代表的字符 | 
|\000| 终止符，\000后的字符串全部忽略|
### ex11 提问
```python
print("xxx",end="") # 输出不换行
```

### ex12 提示别人
```python
age = input("How old are you?")
```
### ex13 参数、解包、变量
```python
from sys import argv # 模组(modules)
# 获取运行参数
script, first, second, third = argv
```
### ex14 提示和传递

### ex15 读取文件
```python
# 获取文件
txt = open(filename)
print("Here's your file %r:" % filename)
# 输出文件内容
print(txt.read())
# 关闭，释放内存
txt.close()
```
### ex16 读写文件

- close – 关闭文件。跟你编辑器的 `文件->保存..` 一个意思。
- read – 读取文件内容。你可以把结果赋给一个变量。
- readline – 读取文本文件中的一行。
- truncate – 清空文件，请小心使用该命令。
- write(stuff) – 将stuff写入文件。

```python
# 只有特别制定参数后，才可以进行写入操作
target = open(filename,'w')
# 清空文件
target.truncate()
# 最后需要关闭，类似文件->保存。。的操作
target.close()
```
### ex17 更多文件操作
```python
from os.path import exists
exists(filename)#判断文件是否存在
```
### ex18 命名、变量、代码、函数
```python
def print_two(*args):
    arg1, arg2 = args
    print("arg1: %r, arg2: %r" % (arg1, arg2))
def print_two_again(arg1, arg2):
    print("arg1: %r, arg2: %r" % (arg1, arg2))
    
# 运行函数(run)’、‘调用函数(call)’、和 ‘使用函数(use)’是同一个意思
```
### ex19 函数和变量

### ex20 函数和文件
```python
file.seek() #移动文件读取指针到指定位置。
```
### ex21 函数可以返回东西

