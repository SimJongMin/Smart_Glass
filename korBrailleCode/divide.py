from PIL import Image
import os


import math
class img_devide():
    def __init__(self,img_path):
        self.img_path = img_path
        self.path = ''
        self.call_num = 0
        self.lengh = 0
        self.width = 0
        self.height = 0
        self.img = ''


    def create_dir(self):
        try:
            os.mkdir('./korBrailleCode/testDataset/a/')  
            print('create new dir')
        except:
            print('already exist')
            pass     
        self.path = './korBrailleCode/testDataset/a'

    def devide_img(self):
        self.img = Image.open(self.img_path)
        area = (0+(self.call_num*(self.width/self.lengh)),0,(self.width/self.lengh)*(self.call_num+1),self.height)
        cropped_img = self.img.crop(area)
        cropped_img.save(self.path + '/'+str(self.call_num)+'.jpg')
        self.call_num+=1
    
    #COMMENT : 전체 길이와 높이로 개별 넓이를 구하는 방법
    def set_image(self):            
        self.img = Image.open(self.img_path)
        self.width = self.img.size[0]
        self.height = self.img.size[1]
        #COMMENT : 점자가 175개 단위로 width/175한 몫을 더해주어야 한다. 
        self.lengh = math.ceil(self.width / (float(self.height)/1.16))
        if(self.width>=6300):
            m=int(int((float(self.height)/1.16)*175)/100)*100
            i=int(self.width/m)
            self.lengh+=i

    def remove_file(self):
        try:
            os.remove(self.path+'/'+str(self.call_num-1)+'.jpg')
        except:
            pass

    def remove_dir(self) :
        try:
            os.rmdir(self.path)
        except :
            print('fail')
