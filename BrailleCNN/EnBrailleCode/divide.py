from PIL import Image
import os

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
            os.mkdir('E:/22-1/CapstoneDesign/Smart_Glass/BrailleCNN/EnBrailleCode/testDataset/a/')
            print('create new dir')
        except:
            print('already exist')
            pass
        self.path = 'E:/22-1/CapstoneDesign/Smart_Glass/BrailleCNN/EnBrailleCode/testDataset/a/'

    def devide_img(self):
        self.img = Image.open(self.img_path)
        area = (0+self.call_num*self.height,0,self.width/self.lengh*(self.call_num+1),self.height)
        cropped_img = self.img.crop(area)
        cropped_img.save(self.path + '/'+str(self.call_num)+'.jpg')
        self.call_num+=1


    def set_image(self):
        self.img = Image.open(self.img_path)
        self.width = self.img.size[0]
        self.height = self.img.size[1]
        self.lengh = int(self.width / self.height)

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