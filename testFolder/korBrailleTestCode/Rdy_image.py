from itertools import count
from keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img
import os
from shutil import copyfile


korAlphabet=[
    "ㄱCho","ㄴCho","ㄷCho","ㄹCho","ㅁCho","ㅂCho","ㅅCho","ㅈCho","ㅊCho","ㅋCho","ㅌCho","ㅍCho","ㅎCho","multiCho",
    "ㄱJong","ㄴJong","ㄷJong","ㄹJong","ㅁJong","ㅂJong","ㅅJong","ㅇJong","ㅈJong","ㅋJong","ㅌJong","ㅍJong","ㅎJong",
    "ㅏ","ㅐ","ㅑ","ㅓ","ㅔ","ㅕ","ㅖ","ㅗ","ㅘ","ㅚ","ㅛ","ㅜ","ㅝ","ㅠ","ㅡ","ㅢ","ㅣ",
    "가","나","다","마","바","사","ㅆ","억","언","얼","연","열","영","옥","온","옹","운","울","은","을","인","자","카","타","파","하"
]

datagen = ImageDataGenerator(
        rotation_range=5,
        width_shift_range=0.1,
        height_shift_range=0.1,
        shear_range=0.05,
        zoom_range=0.01,
        fill_mode='nearest'
        )

def mkdir_alphabet():
    for kor in korAlphabet: 
        os.mkdir('E:/22-1/CapstoneDesign/Smart_Glass/testFolder/korBrailleTestCode/PresetData/' + kor)




def all_new():
    count=0
    for kor in korAlphabet:
        img = load_img('E:/22-1/CapstoneDesign/Smart_Glass/testFolder/korBrailleTestCode/korBrailleImage/'+kor+'.jpg')  # PIL 이미지
        x = img_to_array(img)
        x = x.reshape((1,) + x.shape)
        i = 0
        for batch in datagen.flow(x, batch_size=1, save_to_dir='E:/22-1/CapstoneDesign/Smart_Glass/testFolder/korBrailleTestCode/ConvertData/', save_prefix=kor, save_format='jpg'):
            i += 1
            if i > 19:
                count+=1
                break  # 이미지 20장을 생성하고 마칩니다


def split_data():
    rootdir="E:/22-1/CapstoneDesign/Smart_Glass/testFolder/korBrailleTestCode/ConvertData/"
    for file in os.listdir(rootdir):
        fileName_list=file.split("_")
        letter = fileName_list[0]
        copyfile(rootdir+file, 'E:/22-1/CapstoneDesign/Smart_Glass/testFolder/korBrailleTestCode/PresetData/' + letter + '/' + file)
        os.remove(rootdir+file)

def Preset():
    mkdir_alphabet()
    all_new()
    split_data()
    
    
