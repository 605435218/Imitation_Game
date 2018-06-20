# coding:utf-8
import random
class ReflectorFactory:
    def __init__(self):
        self.Alphabet=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        s1=set(self.Alphabet)
        s2=set(random.sample(self.Alphabet, 13))
        s3=s1-s2
        self.reflector=dict(zip(list(s2),list(s3)))
        self.reflector.update(dict(zip(list(s3),list(s2))))

    def get_reflector(self):
        print self.reflector

if __name__=="__main__":
    ReflectorFactory().get_reflector()