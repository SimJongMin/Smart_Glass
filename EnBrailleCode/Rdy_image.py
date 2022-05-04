from keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img
import os
from shutil import copyfile

datagen = ImageDataGenerator(
        rotation_range=5,
        width_shift_range=0.1,
        height_shift_range=0.1,
        shear_range=0.05,
        zoom_range=0.01,
        fill_mode='nearest'
        )

def mkdir_alphabet():
    alpha = 'a'
    for i in range(0, 26): 
        os.mkdir('E:/22-1/CapstoneDesign/Smart_Glass/BrailleCNN/EnBrailleCode/PresetData/' + alpha)
        alpha = chr(ord(alpha) + 1)
    os.mkdir('E:/22-1/CapstoneDesign/Smart_Glass/BrailleCNN/EnBrailleCode/PresetData/zz')




def all_new():
    alpha = 'a'
    for j in range (0,26):

        img = load_img('E:/22-1/CapstoneDesign/Smart_Glass/BrailleCNN/EnBrailleCode/Braille Dataset2/'+alpha+'.png')  # PIL 이미지
        x = img_to_array(img)
        x = x.reshape((1,) + x.shape)


        i = 0
        for batch in datagen.flow(x, batch_size=1, save_to_dir='E:/22-1/CapstoneDesign/Smart_Glass/BrailleCNN/EnBrailleCode/ConvertData/', save_prefix=alpha, save_format='jpg'):
            i += 1
            if i > 20:
                break  # 이미지 20장을 생성하고 마칩니다

        alpha = chr(ord(alpha) + 1)

def single_new(alpha):
    img = load_img('E:/22-1/CapstoneDesign/Smart_Glass/BrailleCNN/EnBrailleCode/Braille Dataset2/'+alpha+'.png')  # PIL 이미지
    x = img_to_array(img)
    x = x.reshape((1,) + x.shape)

    i = 0
    for batch in datagen.flow(x, batch_size=1, save_to_dir='E:/22-1/CapstoneDesign/Smart_Glass/BrailleCNN/EnBrailleCode/ConvertData/', save_prefix=alpha, save_format='jpg'):
        i += 1
        if i > 10:
         break  # 이미지 20장을 생성하고 마칩니다

def split_data():
    rootdir="E:/22-1/CapstoneDesign/Smart_Glass/BrailleCNN/EnBrailleCode/ConvertData/"
    for file in os.listdir(rootdir):
        letter = file[0]
        str=file[0]+file[1]
        if(str=="zz"):
            copyfile(rootdir+file, 'E:/22-1/CapstoneDesign/Smart_Glass/BrailleCNN/EnBrailleCode/PresetData/' + str + '/' + file)
            os.remove(rootdir+file)
        else:   
            copyfile(rootdir+file, 'E:/22-1/CapstoneDesign/Smart_Glass/BrailleCNN/EnBrailleCode/PresetData/' + letter + '/' + file)
            os.remove(rootdir+file)


def Preset():
    mkdir_alphabet()
    all_new()
    single_new("zz")
    split_data()
    
