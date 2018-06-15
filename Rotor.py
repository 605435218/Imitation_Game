import random
class Rotor:
    def __init__(self):
        self.input_list="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        tmp=[]
        for i in self.input_list:
            tmp.append(i)
        random.shuffle(tmp)
        self.output_list=""
        for i in tmp:
            self.output_list+=i

    def encode(self,input):
        local=self.input_list.find(input)
        return self.output_list[local]

if __name__=="__main__":
    r=Rotor()
    print r.input_list
    print r.output_list
    print r.encode("A")