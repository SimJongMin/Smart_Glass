import operator


korAlpha=[
'공백','ㄱ초','ㄱ종','ㄴ종','ㄷ종','ㄹ초',
'ㄹ종','ㅁ종','ㅂ종','ㅅ초','ㅅ종','ㅇ종',
'ㅈ종','ㅊ초','ㅊ종','ㅋ종','ㅌ종','ㅍ종',
'ㅎ종','ㅏ','ㅐ','ㅑ','ㅓ','ㅔ',
'ㅕ','ㅖ','ㅗ','ㅘ','ㅚ','ㅛ','ㅜ',
'ㅝ','ㅠ','ㅡ','ㅢ','ㅣ','가',
'것1','나','다','마','바','붙임,''사',
'수표','억','언','얼','연','열','영',
'옥','온','옹','운','울','은','을',
'인','자','카','타','파','하',
'ㅟ','ㅒ','ㅙ','ㅞ','것','그래서',
'그러나','그러면','그러므로','그런데','그리고','그리하여'
]

class Predic():
    result = []
    single_result=[]
    single_index=[]
    count=0
    
    def Predict_single(self,model,real):
        my_list = model.predict(real)
        index, value = max(enumerate(my_list[0]), key=operator.itemgetter(1))
        #check_acc(my_list,index,value)                #COMMENT : 예측할 사진의 개별 인덱스와 VALUE값을 출력하고 싶으면 주석 해제
        self.single_index.append(self.count)
        self.single_result.append(index)
        self.count+=1
        return self.single_index, self.single_result
    
    def composit(self):
        for x in range(0,len(self.single_result)):
            if(x==0):
                self.result.append(self.single_result[x])
                continue
            else:
                if(self.single_result[x]==20 and self.single_result[x-1]==30):           #COMMENT : ㅟ
                    self.result.remove(self.single_result[x-1])
                    self.result.insert(x-1,100)
                    
                elif(self.single_result[x]==20 and self.single_result[x-1]==21):         #COMMENT : ㅒ
                    self.result.remove(self.single_result[x-1])
                    self.result.insert(x-1,101)
                    
                elif(self.single_result[x]==20 and self.single_result[x-1]==27):         #COMMENT : ㅙ
                    self.result.remove(self.single_result[x-1])
                    self.result.insert(x-1,102)
                    
                elif(self.single_result[x]==20 and self.single_result[x-1]==31):         #COMMENT : ㅞ
                    self.result.remove(self.single_result[x-1])
                    self.result.insert(x-1,103)
                    
                elif(self.single_result[x]==22 and self.single_result[x-1]==37):         #COMMENT : 것
                    self.result.remove(self.single_result[x-1])
                    self.result.insert(x-1,104)
                    
                elif(self.single_result[x]==22 and self.single_result[x-1]==2):          #COMMENT : 그래서
                    self.result.remove(self.single_result[x-1])
                    self.result.insert(x-1,105)
                    
                elif(self.single_result[x]==38 and self.single_result[x-1]==2):          #COMMENT : 그러나 
                    self.result.remove(self.single_result[x-1])
                    self.result.insert(x-1,106)
                    
                elif(self.single_result[x]==3 and self.single_result[x-1]==2):           #COMMENT : 그러면 
                    self.result.remove(self.single_result[x-1])
                    self.result.insert(x-1,107)
                    
                elif(self.single_result[x]==7 and self.single_result[x-1]==2):           #COMMENT : 그러므로
                    self.result.remove(self.single_result[x-1])
                    self.result.insert(x-1,108)
                    
                elif(self.single_result[x]==23 and self.single_result[x-1]==2):          #COMMENT : 그런데 
                    self.result.remove(self.single_result[x-1])
                    self.result.insert(x-1,109)
                    
                elif(self.single_result[x]==26 and self.single_result[x-1]==2):          #COMMENT : 그리고 
                    self.result.remove(self.single_result[x-1])
                    self.result.insert(x-1,110)
                    
                elif(self.single_result[x]==24 and self.single_result[x-1]==2):          #COMMENT : 그리하여 
                    self.result.remove(self.single_result[x-1])
                    self.result.insert(x-1,111)
                    
                else:
                    self.result.append(self.single_result[x])                            #COMMENT : 일반 점자 
        
        return self.result        


    def reset(self):
        self.result = []
        self.count=0
        self.single_index=[]
        self.single_result=[]


#COMMENT : 예측한 사진의 인덱스와 VALUE를 출력하는 함수
def check_acc(my_list,index,value):
    print("----------Predict result----------")
    print(my_list)
    print("----------max accuracy----------")
    print("index : ",end="")
    print(index,end="          ")
    print("value :",end=" ")
    print(value)

#COMMENT : 한글점자의 인식 모델 결과 인덱스 출력
def chk_trans():
    for i in range(0,75):
        print(str(i)+ " : "+korAlpha[i],end=" | ")
        if(i%5 ==4):
            print()