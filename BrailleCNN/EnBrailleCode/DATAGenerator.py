from keras.preprocessing.image import ImageDataGenerator


def data_ready():
    images_dir = 'E:/22-1/CapstoneDesign/Smart_Glass/BrailleCNN/EnBrailleCode/PresetData/'

    datagen = ImageDataGenerator(
                                rotation_range=5,
                                shear_range=5,
                                validation_split=0.2
    ) #20%를 검증모델로 사용.

    train_generator = datagen.flow_from_directory(images_dir,
                                                  target_size=(36,36),
                                                  subset='training')

    val_generator = datagen.flow_from_directory(images_dir,
                                                target_size=(36,36),
                                                subset='validation')
    return train_generator, val_generator

def load_image(img_path):
    images_dir = img_path
    datagen = ImageDataGenerator()
    real_generator = datagen.flow_from_directory(images_dir,
                                                 target_size=(36, 36))

    return real_generator