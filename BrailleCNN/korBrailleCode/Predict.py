import operator
import numpy as np
import cv2

# def alpha(num):
#     if num == 26:
#         return  ' '
#     else:
#         num_tr = num+97
#         return chr(num_tr)

class Predic():
    result = []
    single_result=[]
    single_index=[]
    count=0
    
    def Predict_single(self,model,real):
        my_list = model.predict(real)
        index, value = max(enumerate(my_list[0]), key=operator.itemgetter(1))
        check_acc(my_list,index,value)
        self.single_index.append(self.count)
        self.single_result.append(index)
        self.count+=1
        return self.single_index, self.single_result
    
    def composit(self):
        for x in range(0,len(self.single_result)):
            if(self.single_result[x]==19 and self.single_result[x-1]==29):
                self.result.remove(self.single_result[x-1])
                self.result.insert(x-1,100)
            elif(self.single_result[x]==19 and self.single_result[x-1]==20):
                self.result.remove(self.single_result[x-1])
                self.result.insert(x-1,101)
            elif(self.single_result[x]==19 and self.single_result[x-1]==26):
                self.result.remove(self.single_result[x-1])
                self.result.insert(x-1,102)
            elif(self.single_result[x]==19 and self.single_result[x-1]==30):
                self.result.remove(self.single_result[x-1])
                self.result.insert(x-1,103)
            elif(self.single_result[x]==21 and self.single_result[x-1]==36):
                self.result.remove(self.single_result[x-1])
                self.result.insert(x-1,104)
            else:
                self.result.append(self.single_result[x])
        return self.result        


    def reset(self):
        self.result = []
        self.count=0


def check_acc(my_list,index,value):
    print("----------Predict result----------")
    print(my_list)
    print("----------max accuracy----------")
    print("index : ",end="")
    print(index,end="          ")
    print("value :",end=" ")
    print(value)


# def chk_trans():
#     for i in range(0,70):
#         print(str(i) + ':' + korAlphabet[i],end='  ')
#         if i%5 ==4 :
#             print()
