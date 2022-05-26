from keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img
import os
from shutil import copyfile

korAlphabet=[
    "ㄱCho","ㄹCho","ㅅCho","ㅊCho","ㅊJong","space",
    "ㄱJong","ㄴJong","ㄷJong","ㄹJong","ㅁJong","ㅂJong","ㅅJong","ㅇJong","ㅈJong","ㅋJong","ㅌJong","ㅍJong","ㅎJong","붙임","것1","수표",
    "ㅏ","ㅐ","ㅑ","ㅓ","ㅔ","ㅕ","ㅖ","ㅗ","ㅘ","ㅚ","ㅛ","ㅜ","ㅝ","ㅠ","ㅡ","ㅢ","ㅣ",
    "가","나","다","마","바","사","억","언","얼","연","열","영","옥","온","옹","운","울","은","을","인","자","카","타","파","하"
]

nonSpaceKorAlphabet=[
    "ㄱCho","ㄹCho","ㅅCho","ㅊCho","ㅊJong",
    "ㄱJong","ㄴJong","ㄷJong","ㄹJong","ㅁJong","ㅂJong","ㅅJong","ㅇJong","ㅈJong","ㅋJong","ㅌJong","ㅍJong","ㅎJong","붙임","것1","수표",
    "ㅏ","ㅐ","ㅑ","ㅓ","ㅔ","ㅕ","ㅖ","ㅗ","ㅘ","ㅚ","ㅛ","ㅜ","ㅝ","ㅠ","ㅡ","ㅢ","ㅣ",
    "가","나","다","마","바","사","억","언","얼","연","열","영","옥","온","옹","운","울","은","을","인","자","카","타","파","하"
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
        try:
            os.mkdir('./korBrailleCode/PresetData/' + kor)      
        except:
            print("already exist")
            pass


def mkdir_noise_alphabet():
    for kor in korAlphabet:
        try:
            os.mkdir('./korBrailleCode/noisePresetData/' + kor)
        except:
            print("already exist")
            pass


def mkdir_capture_alphabet():
    for kor in korAlphabet:
        try:
            os.mkdir('./korBrailleCode/totalPresetData/' + kor)
        except:
            print("already exist")
            pass


def mkdir_total_alphabet():
    for kor in korAlphabet:
        try:
            os.mkdir('./korBrailleCode/totalPresetData/' + kor)
        except:
            print("already exist")
            pass

def all_new():
    count=0
    for kor in korAlphabet:
        #COMMENT : PIL이미지
        img = load_img('./korBrailleCode/korBrailleImage/'+kor+'.jpg')         
        x = img_to_array(img)
        x = x.reshape((1,) + x.shape)
        i = 0
        for batch in datagen.flow(x, batch_size=1, save_to_dir='./korBrailleCode/ConvertData/', save_prefix=kor, save_format='jpg'):        
            i += 1
            if i > 99:
                count+=1
                break  #COMMENT: 이미지 100장을 생성하고 마칩니다


def all_noise_new():
    count = 0
    for kor in korAlphabet:
        #COMMENT : PIL이미지
        img = load_img('./korBrailleCode/noiseAdded_images/'+kor+'_noiseadded.jpg')
        x = img_to_array(img)
        x = x.reshape((1,) + x.shape)
        i = 0
        for batch in datagen.flow(x, batch_size=1, save_to_dir='./korBrailleCode/ConvertData/', save_prefix=kor, save_format='jpg'):
            i += 1
            if i > 99:
                count += 1
                break  # COMMENT: 이미지 100장을 생성하고 마칩니다


def all_capture_new():
    count = 0
    for kor in korAlphabet:
        #COMMENT : PIL이미지
        img = load_img('./korBrailleCode/camera_capture_images/' + kor+'_captured.jpg')
        x = img_to_array(img)
        x = x.reshape((1,) + x.shape)
        i = 0
        for batch in datagen.flow(x, batch_size=1, save_to_dir='./korBrailleCode/ConvertData/', save_prefix=kor, save_format='jpg'):
            i += 1
            if i > 99:
                count += 1
                break  # COMMENT: 이미지 100장을 생성하고 마칩니다


def split_data():
    rootdir="./korBrailleCode/ConvertData/"     
    for file in os.listdir(rootdir):
        fileName_list=file.split("_")
        letter = fileName_list[0]
        copyfile(rootdir+file, './korBrailleCode/PresetData/' + letter + '/' + file)        
        os.remove(rootdir+file)


def split_noise_data():
    rootdir = "./korBrailleCode/ConvertData/"
    for file in os.listdir(rootdir):
        fileName_list = file.split("_")
        letter = fileName_list[0]
        copyfile(rootdir+file, './korBrailleCode/noisePresetData/' + letter + '/' + file)
        os.remove(rootdir+file)


def split_capture_data():
    rootdir = "./korBrailleCode/ConvertData/"
    for file in os.listdir(rootdir):
        fileName_list = file.split("_")
        letter = fileName_list[0]
        copyfile(rootdir+file, './korBrailleCode/capturePresetData/' + letter + '/' + file)
        os.remove(rootdir+file)


def collect_all_data():
    for alpha in korAlphabet:
        path="./korBrailleCode/PresetData/"+alpha+"/"
        for file in os.listdir(path):
            fileName_list = file.split("_")
            letter = fileName_list[0]
            copyfile(path+file, './korBrailleCode/totalPresetData/' + letter + '/' + file)
            
    for alpha in korAlphabet:
        path = "./korBrailleCode/noisePresetData/"+alpha+"/"
        for file in os.listdir(path):
            fileName_list = file.split("_")
            letter = fileName_list[0]
            copyfile(path+file, './korBrailleCode/totalPresetData/' + letter + '/' + file)
    
    for alpha in nonSpaceKorAlphabet:
        path = "./korBrailleCode/capturePresetData/"+alpha+"/"
        for file in os.listdir(path):
            fileName_list = file.split("_")
            letter = fileName_list[0]
            copyfile(path+file, './korBrailleCode/totalPresetData/' + letter + '/' + file)

def Preset():
    mkdir_alphabet()
    all_new()
    split_data()


def noise_Preset():
    mkdir_noise_alphabet()
    all_noise_new()
    split_noise_data()


def capture_Preset():
    mkdir_capture_alphabet()
    all_capture_new()
    split_capture_data()