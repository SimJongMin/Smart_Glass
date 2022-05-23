from keras.preprocessing.image import ImageDataGenerator


def data_ready():
    images_dir = './korBrailleCode/PresetData/'

    datagen = ImageDataGenerator(
                                rotation_range=5,
                                shear_range=5,
                                validation_split=0.2
    )#COMMENT : 20%를 검증모델로 사용.

    train_generator = datagen.flow_from_directory(images_dir,
                                                target_size=(36,42),
                                                subset='training')

    val_generator = datagen.flow_from_directory(images_dir,
                                                target_size=(36,42),
                                                subset='validation')
    return train_generator, val_generator


def noise_data_ready():
    images_dir = './korBrailleCode/noisePresetData/'

    datagen = ImageDataGenerator(
        rotation_range=5,
        shear_range=5,
        validation_split=0.2
    )  # COMMENT : 20%를 검증모델로 사용.

    train_generator = datagen.flow_from_directory(images_dir,
                                                  target_size=(36, 42),
                                                  subset='training')

    val_generator = datagen.flow_from_directory(images_dir,
                                                target_size=(36, 42),
                                                subset='validation')
    return train_generator, val_generator


def capture_data_ready():
    images_dir = './korBrailleCode/capturePresetData/'

    datagen = ImageDataGenerator(
        rotation_range=5,
        shear_range=5,
        validation_split=0.2
    )  # COMMENT : 20%를 검증모델로 사용.

    train_generator = datagen.flow_from_directory(images_dir,
                                                  target_size=(36, 42),
                                                  subset='training')

    val_generator = datagen.flow_from_directory(images_dir,
                                                target_size=(36, 42),
                                                subset='validation')
    return train_generator, val_generator


def total_data_ready():
    images_dir = './korBrailleCode/totalPresetData/'

    datagen = ImageDataGenerator(
        rotation_range=5,
        shear_range=5,
        validation_split=0.2
    )  # COMMENT : 20%를 검증모델로 사용.

    train_generator = datagen.flow_from_directory(images_dir,
                                                  target_size=(36, 42),
                                                  subset='training')

    val_generator = datagen.flow_from_directory(images_dir,
                                                target_size=(36, 42),
                                                subset='validation')
    return train_generator, val_generator

def load_image_single(img_path):
    images_dir = img_path
    datagen = ImageDataGenerator()
    real_generator = datagen.flow_from_directory(images_dir,
                                                target_size=(36, 42))

    return real_generator
