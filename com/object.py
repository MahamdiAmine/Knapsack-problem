#!/usr/bin/env python3                                    #
# -.- coding: utf-8 -.-                                   #
# Author mahamdi amine                                    #
# Github https://github.com/MahamdiAmine                  #
###########################################################

class Object:
    packed=0
    def __init__(self,id,weight,value):
        self.id=id
        self.weight=weight
        self.value=value
        packed=0
    def is_packed(picked):
        packed=picked
    def get_weight(self):
        return self.weight
    def get_value(self):
        return self.value
    def get_id(self):
        return self.id
    def printObject(self):
        print(self.id,self.weight,self.value)

