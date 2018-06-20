# -*- coding:utf8 -*-
class Rotor:
    def __init__(self,out_list):
        self.input_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.output_list=out_list
        self.index=0

    def turn(self):
        self.index=(self.index+1)%26
        #转完一圈
        if self.index==0:
            return True
        return False

    def turn_rotor(self,character):
        self.index=self.input_list.find(character)


    def encode(self,input):
        input=input.upper()
        local=self.input_list.find(input)
        local=(local+self.index)%26
        return self.output_list[local]

    def reverse_encode(self,input):
        input = input.upper()
        local = self.output_list.find(input)
        local=(local-self.index)%26
        return self.input_list[local]