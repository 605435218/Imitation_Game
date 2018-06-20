# coding:utf-8
from Rotor import Rotor
import copy
class EnigmaMachine:
    def __init__(self,Rotors,key,patch_board):
        #串联转子
        self.Rotors=copy.copy(Rotors)
        #经过反射器后会逆序经过转子
        Rotors.reverse()
        self.reserver_Rotors=Rotors
        #根据密钥拨动转子
        for i in range(len(key)):
            self.Rotors[i].turn_rotor(key[i])
        #反射器
        self.reflector={'A': 'C', 'C': 'A', 'B': 'E', 'E': 'B', 'D': 'F', 'G': 'H', 'F': 'D', 'I': 'L', 'H': 'G', 'K': 'O', 'J': 'N', 'M': 'P', 'L': 'I', 'O': 'K', 'N': 'J', 'Q': 'S', 'P': 'M', 'S': 'Q', 'R': 'U', 'U': 'R', 'T': 'V', 'W': 'X', 'V': 'T', 'Y': 'Z', 'X': 'W', 'Z': 'Y'}
        #插线板
        self.patch_board={}
        #最多交换13对字母
        for i in patch_board[0:13]:
            self.patch_board[i[0]]=i[1]
            self.patch_board[i[1]]=i[0]

    def encode(self,input):
        print "编码： %s " % input
        output=""
        for i in input:
            #只对26个字母编码
            if i not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
                output += i
                continue
            #正向通过转子
            for Rotor in self.Rotors:
                i=Rotor.encode(i)
            #经过反射器
            i=self.reflector[i]
            #反向通过转子
            for Rotor in self.reserver_Rotors:
                i = Rotor.reverse_encode(i)
            #输出
            output+=i
            #一次加密完成，转子转动,转过一圈带动下一位
            turn_next=self.Rotors[0].turn()
            for Rotor in self.Rotors[1:]:
                if turn_next:
                    turn_next=Rotor.turn()
        print output
        return output


if __name__=="__main__":
    Rotors=[]
    Rotors.append(Rotor.Rotor("ARYPJVWZBQUONSHCXLTIDEGKMF"))
    Rotors.append(Rotor.Rotor("GYFZNCLQDTOBARUWKJSXMPIEHV"))
    Rotors.append(Rotor.Rotor("WYCEOGIKTDANUMVFRXJSQPZHLB"))
    patch_board=[('A','B'),('E','F')]
    e1=EnigmaMachine(Rotors,"ABC",patch_board)
    o = e1.encode("ABCDEFGHIJKLMNOPQRSTUVWXYZ "*5)
    Rotors = []
    Rotors.append(Rotor.Rotor("ARYPJVWZBQUONSHCXLTIDEGKMF"))
    Rotors.append(Rotor.Rotor("GYFZNCLQDTOBARUWKJSXMPIEHV"))
    Rotors.append(Rotor.Rotor("WYCEOGIKTDANUMVFRXJSQPZHLB"))
    patch_board = [('A', 'B'), ('E', 'F')]
    e2=EnigmaMachine(Rotors, "ABC", patch_board)
    e2.encode(o)