import operator
import numpy as np
import cv2

class Predic():
    result = []
    single_result=[]
    single_index=[]
    count=0
    
    def Predict_single(self,model,real):
        my_list = model.predict(real)
        index, value = max(enumerate(my_list[0]), key=operator.itemgetter(1))
        # check_acc(my_list,index,value)                #COMMENT : 예측할 사진의 개별 인덱스와 VALUE값을 출력하고 싶으면 주석 해제
        self.single_index.append(self.count)
        self.single_result.append(index)
        self.count+=1
        return self.single_index, self.single_result
    
    def composit(self):
        for x in range(0,len(self.single_result)):
            if(self.single_result[x]==19 and self.single_result[x-1]==29):           #COMMENT : ㅟ
                self.result.remove(self.single_result[x-1])
                self.result.insert(x-1,100)
            elif(self.single_result[x]==19 and self.single_result[x-1]==20):         #COMMENT : ㅒ
                self.result.remove(self.single_result[x-1])
                self.result.insert(x-1,101)
            elif(self.single_result[x]==19 and self.single_result[x-1]==26):         #COMMENT : ㅙ
                self.result.remove(self.single_result[x-1])
                self.result.insert(x-1,102)
            elif(self.single_result[x]==19 and self.single_result[x-1]==30):         #COMMENT : ㅞ
                self.result.remove(self.single_result[x-1])
                self.result.insert(x-1,103)
            elif(self.single_result[x]==21 and self.single_result[x-1]==36):         #COMMENT : 것 
                self.result.remove(self.single_result[x-1])
                self.result.insert(x-1,104)
            elif(self.single_result[x]==21 and self.single_result[x-1]==2):          #COMMENT : 그래서
                self.result.remove(self.single_result[x-1])
                self.result.insert(x-1,105)
            elif(self.single_result[x]==37 and self.single_result[x-1]==2):          #COMMENT : 그러나 
                self.result.remove(self.single_result[x-1])
                self.result.insert(x-1,106)
            elif(self.single_result[x]==3 and self.single_result[x-1]==2):           #COMMENT : 그러면 
                self.result.remove(self.single_result[x-1])
                self.result.insert(x-1,107)
            elif(self.single_result[x]==7 and self.single_result[x-1]==2):           #COMMENT : 그러므로
                self.result.remove(self.single_result[x-1])
                self.result.insert(x-1,108)
            elif(self.single_result[x]==22 and self.single_result[x-1]==2):          #COMMENT : 그런데 
                self.result.remove(self.single_result[x-1])
                self.result.insert(x-1,109)
            elif(self.single_result[x]==25 and self.single_result[x-1]==2):          #COMMENT : 그리고 
                self.result.remove(self.single_result[x-1])
                self.result.insert(x-1,110)
            elif(self.single_result[x]==23 and self.single_result[x-1]==2):          #COMMENT : 그리하여 
                self.result.remove(self.single_result[x-1])
                self.result.insert(x-1,111)
            else:
                self.result.append(self.single_result[x])                            #COMMENT : 일반 점자 
        return self.result        


    def reset(self):
        self.result = []
        self.count=0


#COMMENT : 예측한 사진의 인덱스와 VALUE를 출력하는 함수
def check_acc(my_list,index,value):
    print("----------Predict result----------")
    print(my_list)
    print("----------max accuracy----------")
    print("index : ",end="")
    print(index,end="          ")
    print("value :",end=" ")
    print(value)
