#!/usr/bin/env python3                                    #
# -.- coding: utf-8 -.-                                   #
# Author mahamdi amine                                    #
# Github https://github.com/MahamdiAmine                  #
###########################################################

class Object:
    #this class represents the item proprieties: id,weight,value,packed or not
    def __init__(self,id,weight,value):
        self._id=id
        self._weight=weight
        self._value=value
        self._packed=0

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def packed(self):
        return self._packed

    @packed.setter
    def packed(self, value):
        self._packed = value

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


    def printObject(self):
        print(self._id,self._weight,self._value,self._packed)

    def set_packed(self,v):
        self._packed=v