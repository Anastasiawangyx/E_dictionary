import json


class EDictionary:
    e_dic = {}

    def __init__(self):
        try:
            a = open('package_edic//edic.json', 'r')
        except IOError:
            print("Can't open file!")
        else:
            print("file open success!")
            e_dic = json.load(a)
            self.e_dic = e_dic

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



