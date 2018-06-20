# coding:utf-8
import random
#插线板工厂
class PatchBoardFactory:
    def __init__(self):
        self.Alphabet=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.num=random.randint(0, 13)
    #获取一个插线板
    def get_patchboard(self):
        if self.num == 0:
            return None
        keys = random.sample(self.Alphabet,self.num)
        for key in keys:
            self.Alphabet.remove(key)
        values=random.sample(self.Alphabet,self.num)
        self.PatchBoard = dict(zip(keys, values))
        self.PatchBoard.update(dict(zip(values, keys)))
        return self.PatchBoard


if __name__=="__main__":
    print PatchBoardFactory().get_patchboard()