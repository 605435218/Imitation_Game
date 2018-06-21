# coding:utf-8
import random
#转子工厂
class RotorFactory:
    def __init__(self):
        self.input_list="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        tmp=[]
        for i in self.input_list:
            tmp.append(i)
        random.shuffle(tmp)
        self.output_list=""
        for i in tmp:
            self.output_list+=i
    #获得一个转子的内部线路
    def get_rotor(self):
        return self.output_list

if __name__=="__main__":
    print RotorFactory().get_rotor()
