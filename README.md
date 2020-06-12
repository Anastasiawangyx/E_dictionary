# E_dictionary
软件工程上机作业——电子词典

## 一、实验要求

1. 开发一个机器可读的英汉词典，能获得给定英文词条的多方面信息（读音、词性、每个词义、例句等，能提供的信息越多越好），并在其他软件系统（桌面或在线词典、机器翻译系统、其他自然语言处理系统等）中使用；
2. 根据常见纸质英汉词典（如牛津高阶英汉词典等）的内容和结构，给出详细的机器可读英汉词典的功能需求；
3. 设计机器可读英汉词典的存储结构（词典需要存储在磁盘中和内存中）；
4. 设计机器可读英汉词典的接口；
5. 采用熟悉的语言（OOP优先）进行实现；
6. 采用测试驱动的开发方法进行开发；
7. 采用重构完善设计和实现；



## 二、实验内容

使用python3.8、pycharm作为IDE开发，符合OOP开发的要求。

### 1. 功能需求

开发出的此款电子词典需要能够在支持python内核的软件中使用，在用户在界面端输入需要查询的单词后，单词数据将由前端传递到后段内核中（此功能不在此次试验的考察范围内，故使用直接输入代替）。在接收到单词输入后，软件需要在存储的电子词典中找到该单词的音标、词义、英文例句和对应的中文翻译，并通过接口传递给前端，显示在用户的屏幕上。

### 2. 字典存储

将电子词典以<code>json</code>文件的形式存储，并使用python的<code>json.load()</code>函数，将电子词典以**字典**的形式实现查找。

下为json文件中的一个单词存储的例子。

```json
{
  ...
  
  "air": ["[er]",
          "n. 空气，大气；天空；样子；曲调\nvt. 使通风，晾干；夸耀\nvi. 通风",
          "Keith opened the window and leaned out into the cold air.\n\n基斯打开窗户，探出身到冷风中。"],
  
  ...
}
```



### 3. 具体实现

首先初始化一个电子词典类。

```python
edic=edictionary.EDictionary()
```

在EDictionary类的初始化过程中，已经将json文件中的内容以字典的形式存储在了内存中，方便用户查找。

```python
    def __init__(self):
        try:
            a = open('package_edic//edic.json', 'r')
        except IOError:
            print("Can't open file!")
        else:
            print("file open success!")
            e_dic = json.load(a)
            self.e_dic = e_dic
```

得到用户的输入后，程序在<code>e_dic</code>字典中查找对应的key，若存在，则打印它的value，若不存在，则出现错误。

```python
    def show(self):
        word = input("请输入你想要查询的单词:")
        try:
            name = self.e_dic[word]
        except:
            print("你想要查询的单词不在我们的词库中哦～")
        else:
            pronunciation = name[0]
            meaning = name[1]
            example = name[2]
            print("单词:" + word)
            print("发音:" + pronunciation)
            print("词义:\n" + meaning)
            print("例句:\n" + example)
```



每一个单词的音标、词义、双语例句都以列表的形式存储在key对应的value中，在显示时可以直接调用。

### 4. 模块化

python提供的包机制可以很好的实现模块化 。

将json文件和edictionary.py打包放入package_edic中，加入<code>__ _init_ _ _.py</code>文件来表示这是一个包。调用此电子词典时，只需要导入包，实例化一个对象后调用对应的方法即可。

```python
# test.py

from package_edic import edictionary

edic=edictionary.EDictionary()
edic.show()

'''
/usr/local/bin/python3.8 /Users/wangyixian/Desktop/软工上机3/test.py
file open success!
请输入你想要查询的单词:air
单词:air
发音:[er]
词义:
n. 空气，大气；天空；样子；曲调
vt. 使通风，晾干；夸耀
vi. 通风
例句:
Keith opened the window and leaned out into the cold air.

基斯打开窗户，探出身到冷风中。

Process finished with exit code 0
'''
```

