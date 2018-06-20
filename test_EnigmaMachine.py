# coding:utf-8
from EnigmaMachine import EnigmaMachine
from Rotor.Rotor import Rotor
from Rotor.RotorFactory import RotorFactory
from PatchBoard.PatchBoardFactory import PatchBoardFactory
from Reflector.ReflectorFactory import ReflectorFactory
import random
import unittest
class test_EnigmaMachine(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_encode(self):
        characters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789,.!?'
        for n in xrange(1000):
            #随机生成一个密钥
            key=''.join(random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ',3))
            #随机生成一个插线板排序
            patch_board = PatchBoardFactory().get_patchboard()
            #随机生成3个转子
            Rotor1=RotorFactory().get_rotor()
            Rotor2=RotorFactory().get_rotor()
            Rotor3=RotorFactory().get_rotor()
            #随机生成一个反射器
            reflector=ReflectorFactory().get_reflector()
            #生成一台恩格玛机用于编码
            e1 = EnigmaMachine([Rotor(Rotor1),Rotor(Rotor2),Rotor(Rotor3)], key, patch_board,reflector)
            #生成一台恩格玛机用于解码
            e2 = EnigmaMachine([Rotor(Rotor1),Rotor(Rotor2),Rotor(Rotor3)], key, patch_board,reflector)
            for i in xrange(1000):
                #生成一个随机字符串
                ran_str = ''.join(random.sample(characters, random.randint(1, 67)))
                #初始位置相同，将编码结果输入能得到原码
                encode = e1.encode(ran_str)
                decode = e2.encode(encode)
                if decode != ran_str.upper():
                    print ran_str
                    print [Rotor1,Rotor2,Rotor3],
                    print key
                    print patch_board
                    print reflector
                self.assertEqual(ran_str.upper(),decode)

if __name__=="__main__":
    unittest.main()
