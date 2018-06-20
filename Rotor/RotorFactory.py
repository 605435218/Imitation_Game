import random
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

    def get_rotor(self):
        print self.output_list

if __name__=="__main__":
    for i in xrange(3):
        RotorFactory().get_rotor()
