#!/usr/bin/env python3                                    #
# -.- coding: utf-8 -.-                                   #
# Author mahamdi amine                                    #
# Github https://github.com/MahamdiAmine                  #
###########################################################


from knapsac_problem import *
from object import *

max=18
def main1():
    k = Knapsac()
    # objects = [[4, 7, 8, 9], [1, 5, 8, 4]]
    # print(np.matrix(k.knapSack(8, objects[1], objects[0])))
    # """read the params max_weight , the weight and the value of the n objects"""
    while True:
        try:
            # max_weight = int(input("Enter the value of the Max weight :"))
            # n = int(input("Enter the number of objects : "))
            # objects = [[0 for x in range(n)] for y in range(2)]
            objects = [ [4, 7, 8, 9],[1, 5, 8, 4]]
            w=objects[0]
            v=objects[1]
            # for i in range(n):
            #     objects[0][i] = int(input("Enter the value of object number " + str(i) + "  "))
            #     objects[1][i] = int(input("Enter the weight of object number " + str(i) + "  "))
            print(np.matrix(k.knapSack(max, w, v)))
            print(k.check_items(objects[0], k.knapSack(max, objects[0], objects[1]), max))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")


# begin()
def main2():
    k=Knapsac()
    obj=[]
    obj.insert(0,Object(0,4,1))
    obj.insert(1,Object(1,7,5))
    obj.insert(2,Object(2,8,8))
    obj.insert(3,Object(3,9,4))
    w=[]
    v=[]
    for i in  range(len(obj)):
        w.insert(i,obj[i].get_weight())
        v.insert(i,obj[i].get_value())
    print(w,v)
    print(np.matrix(k.knapSack(max, w, v)))
    print(k.check_items(w, k.knapSack(max, w, v), max))
main2()
# main1()