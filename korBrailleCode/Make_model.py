from keras import backend as K
from keras import layers as L
from keras.models import Model
from keras.regularizers import l2
from keras.callbacks import ModelCheckpoint,ReduceLROnPlateau,EarlyStopping

def Make_model(train,val):
    K.clear_session()

    model_ckpt = ModelCheckpoint('./korBrailleCode/KorBrailleNet.h5',save_best_only=True)      
    reduce_lr = ReduceLROnPlateau(patience=8,verbose=1)
    early_stop = EarlyStopping(patience=5,verbose=2,monitor='accuracy')

    entry = L.Input(shape=(42, 36, 3))
    x = L.SeparableConv2D(64, (5, 5), activation='relu', padding='same')(entry)
    x = L.MaxPooling2D((2, 2), padding='same')(x)
    # x = L.BatchNormalization()(x)
    # x = L.Dropout(0.5)(x)

    x = L.SeparableConv2D(128, (5, 5), activation='relu',
                          padding='same')(entry)
    x = L.MaxPooling2D((2, 2), padding='same')(x)

    x = L.SeparableConv2D(256, (5, 5), activation='relu', padding='same')(x)
    x = L.MaxPooling2D((2, 2), padding='same')(x)

    x = L.SeparableConv2D(512, (5, 5), activation='relu', padding='same')(x)
    x = L.GlobalMaxPooling2D()(x)

    # x= L.Flatten()

    x = L.Dense(512)(x)
    x = L.BatchNormalization()(x)
    x = L.ReLU()(x)
    x = L.Dropout(0.3)(x)

    x = L.Dense(256)(x)
    x = L.BatchNormalization()(x)
    x = L.ReLU()(x)
    x = L.Dropout(0.3)(x)

    x = L.Dense(128)(x)
    x = L.BatchNormalization()(x)
    x = L.ReLU()(x)
    x = L.Dropout(0.3)(x)

    x = L.Dense(64, activation='softmax')(x)

    model = Model(entry, x)
    model.compile(loss='categorical_crossentropy',
                  optimizer='adam', metrics=['accuracy'])

    model.summary()

    history = model.fit(train, validation_data=val, epochs=20, callbacks=[
                                  model_ckpt, reduce_lr, early_stop], verbose=1)
    return history


def Make_noise_model(train, val):
    K.clear_session()

    model_ckpt = ModelCheckpoint('./korBrailleCode/noiseKorBrailleNet.h5', save_best_only=True)
    reduce_lr = ReduceLROnPlateau(patience=8, verbose=1)
    early_stop = EarlyStopping(patience=5, verbose=2, monitor='accuracy')

    entry = L.Input(shape=(50, 58, 3))
    x = L.SeparableConv2D(64, (5, 5), activation='relu', padding='same')(entry)
    x = L.BatchNormalization()(x)
    x = L.MaxPooling2D((2, 2))(x)
    # x = L.BatchNormalization()(x)
    # x = L.Dropout(0.5)(x)

    x = L.SeparableConv2D(128, (5, 5), activation='relu', padding='same')(entry)
    x = L.BatchNormalization()(x)
    x = L.MaxPooling2D((2, 2))(x)
    # x = L.BatchNormalization()(x)
    # x = L.Dropout(0.5)(x)

    x = L.SeparableConv2D(256, (5, 5), activation='relu', padding='same')(x)
    x = L.BatchNormalization()(x)
    x = L.MaxPooling2D((2, 2))(x)
    # x = L.BatchNormalization()(x)
    # x = L.Dropout(0.5)(x)

    x = L.SeparableConv2D(512, (5, 5), activation='relu', padding='same')(x)
    x = L.BatchNormalization()(x)
    x = L.GlobalMaxPooling2D()(x)
    # x = L.Dropout(0.5)(x)

    x = L.Dense(512)(x)
    x = L.LeakyReLU()(x)
    x = L.Dropout(0.5)(x)
    x = L.Dense(256)(x)
    x = L.ReLU()(x)
    x = L.Dropout(0.5)(x)
    x = L.Dense(128, kernel_regularizer=l2(2e-4))(x)
    x = L.ReLU()(x)
    x = L.Dropout(0.5)(x)
    x = L.Dense(64, activation='softmax')(x)

    model = Model(entry, x)
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    history = model.fit_generator(train, validation_data=val, epochs=100, callbacks=[model_ckpt, reduce_lr, early_stop], verbose=2)
    return history
def Make_capture_model(train, val):
    K.clear_session()

    model_ckpt = ModelCheckpoint(
        './korBrailleCode/captureKorBrailleNet.h5', save_best_only=True)
    reduce_lr = ReduceLROnPlateau(patience=8, verbose=1)
    early_stop = EarlyStopping(patience=5, verbose=2, monitor='accuracy')

    entry = L.Input(shape=(50, 58, 3))
    x = L.SeparableConv2D(64, (5, 5), activation='relu', padding='same')(entry)
    x = L.BatchNormalization()(x)
    x = L.MaxPooling2D((2, 2))(x)
    # x = L.BatchNormalization()(x)
    # x = L.Dropout(0.5)(x)

    x = L.SeparableConv2D(128, (5, 5), activation='relu',
                          padding='same')(entry)
    x = L.BatchNormalization()(x)
    x = L.MaxPooling2D((2, 2))(x)
    # x = L.BatchNormalization()(x)
    # x = L.Dropout(0.5)(x)

    x = L.SeparableConv2D(256, (5, 5), activation='relu', padding='same')(x)
    x = L.BatchNormalization()(x)
    x = L.MaxPooling2D((2, 2))(x)
    # x = L.BatchNormalization()(x)
    # x = L.Dropout(0.5)(x)

    x = L.SeparableConv2D(512, (5, 5), activation='relu', padding='same')(x)
    x = L.BatchNormalization()(x)
    x = L.GlobalMaxPooling2D()(x)
    # x = L.Dropout(0.5)(x)

    x = L.Dense(512)(x)
    x = L.LeakyReLU()(x)
    x = L.Dropout(0.5)(x)
    x = L.Dense(256)(x)
    x = L.ReLU()(x)
    x = L.Dropout(0.5)(x)
    x = L.Dense(128, kernel_regularizer=l2(2e-4))(x)
    x = L.ReLU()(x)
    x = L.Dropout(0.5)(x)
    x = L.Dense(64, activation='softmax')(x)

    model = Model(entry, x)
    model.compile(loss='categorical_crossentropy',
                  optimizer='adam', metrics=['accuracy'])

    history = model.fit_generator(train, validation_data=val, epochs=100, callbacks=[
                                  model_ckpt, reduce_lr, early_stop], verbose=2)
    return history


def Make_total_model(train, val):
    K.clear_session()

    model_ckpt = ModelCheckpoint(
        './korBrailleCode/totalKorBrailleNet.h5', save_best_only=True)
    reduce_lr = ReduceLROnPlateau(patience=8, verbose=1)
    early_stop = EarlyStopping(patience=5, verbose=2, monitor='accuracy')

    entry = L.Input(shape=(42, 36, 3))
    x = L.SeparableConv2D(64, (5, 5), activation='relu', padding='same')(entry)
    x = L.MaxPooling2D((2, 2), padding='same')(x)
    # x = L.BatchNormalization()(x)
    # x = L.Dropout(0.5)(x)

    x = L.SeparableConv2D(128, (5, 5), activation='relu', padding='same')(entry)
    x = L.MaxPooling2D((2, 2), padding='same')(x)


    x = L.SeparableConv2D(256, (5, 5), activation='relu', padding='same')(x)
    x = L.MaxPooling2D((2, 2), padding='same')(x)

    x = L.SeparableConv2D(512, (5, 5), activation='relu', padding='same')(x)
    x = L.GlobalMaxPooling2D()(x)

    # x= L.Flatten()

    x = L.Dense(512)(x)
    x = L.BatchNormalization()(x)
    x = L.ReLU()(x)
    x = L.Dropout(0.3)(x)
    
    x = L.Dense(512)(x)
    x = L.BatchNormalization()(x)
    x = L.ReLU()(x)
    x = L.Dropout(0.3)(x)
    
    x = L.Dense(256)(x)
    x = L.BatchNormalization()(x)
    x = L.ReLU()(x)
    x = L.Dropout(0.3)(x)

    x = L.Dense(128)(x)
    x = L.BatchNormalization()(x)
    x = L.ReLU()(x)
    x = L.Dropout(0.3)(x)
    
    x = L.Dense(64, activation='softmax')(x)

    model = Model(entry, x)
    model.compile(loss='categorical_crossentropy',
                  optimizer='adam', metrics=['accuracy'])

    model.summary()

    history = model.fit_generator(train, validation_data=val, epochs=30, callbacks=[
                                  model_ckpt, reduce_lr, early_stop], verbose=1)
    return history


def print_acc_loss(history):
    #COMMENT : 평가 결과 도식화
    import matplotlib.pyplot as plt
    fig, loss_ax = plt.subplots(figsize=(10, 5))
    acc_ax = loss_ax.twinx()
    loss_ax.plot(history.history['loss'], 'y', label='train loss')
    loss_ax.plot(history.history['val_loss'], 'r', label='val loss')
    acc_ax.plot(history.history['accuracy'], 'b', label='train acc')
    acc_ax.plot(history.history['val_accuracy'], 'g', label='val acc')
    loss_ax.set_xlabel('epoch')
    loss_ax.set_ylabel('loss')
    acc_ax.set_ylabel('accuray')
    loss_ax.legend(loc='upper left')
    acc_ax.legend(loc='lower left')

    plt.show()