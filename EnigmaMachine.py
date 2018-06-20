# coding:utf-8
from Rotor.Rotor import Rotor
import copy

import random
from Rotor.RotorFactory import RotorFactory
from PatchBoard.PatchBoardFactory import PatchBoardFactory
from Reflector.ReflectorFactory import ReflectorFactory

class EnigmaMachine:
    def __init__(self,Rotors,key,patch_board,reflector):
        #串联转子
        self.Rotors=copy.copy(Rotors)
        #经过反射器后会逆序经过转子
        Rotors.reverse()
        self.reserver_Rotors=Rotors
        #根据密钥拨动转子
        for i in range(len(key)):
            self.Rotors[i].turn_rotor(key[i])
        #反射器
        self.reflector=reflector
        #插线板
        self.patch_board=patch_board


    def encode(self,input):
        #print input
        output=""
        for i in input:
            #只对26个字母编码
            if i not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
                output += i
                continue
            i=i.upper()
            #经过插线板
            if self.patch_board and i in self.patch_board.keys():
                i=self.patch_board[i]
            #正向通过转子
            for Rotor in self.Rotors:
                i=Rotor.encode(i)
            #经过反射器
            i=self.reflector[i]
            #反向通过转子
            for Rotor in self.reserver_Rotors:
                i = Rotor.reverse_encode(i)
            # 经过插线板
            if self.patch_board and i in self.patch_board.keys():
                i = self.patch_board[i]
            #输出
            output+=i
            #一次加密完成，转子转动,转过一圈带动下一位
            turn_next=self.Rotors[0].turn()
            for Rotor in self.Rotors[1:]:
                if turn_next:
                    turn_next=Rotor.turn()
        return output


if __name__=="__main__":
    # 随机生成一个密钥
    key = ''.join(random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 3))
    # 随机生成一个插线板排序
    patch_board = PatchBoardFactory().get_patchboard()
    # 随机生成3个转子
    Rotor1 = RotorFactory().get_rotor()
    Rotor2 = RotorFactory().get_rotor()
    Rotor3 = RotorFactory().get_rotor()
    # 随机生成一个反射器
    reflector = ReflectorFactory().get_reflector()
    # 生成一台恩格玛机用于编码
    e1 = EnigmaMachine([Rotor(Rotor1), Rotor(Rotor2), Rotor(Rotor3)], key, patch_board, reflector)
    # 生成一台恩格玛机用于解码
    e2 = EnigmaMachine([Rotor(Rotor1), Rotor(Rotor2), Rotor(Rotor3)], key, patch_board, reflector)
    encode = e1.encode("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "*5)
    decode = e2.encode(encode)
    print decode