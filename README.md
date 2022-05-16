# Smart_Glass

## 1. Install need libraries

    * Recommended Raspberry Pi Specs
        * os : Raspberry Pi OS(64-bit)
        * python : 3.9.x

___

#### 1-0. Upgrade & Update
   * Upgrade & Update code

       ```bash
         $ sudo apt-get update
         $ sudo apt-get upgrade
         $ sudo pip install --upgrade pip
       ```

#### 1-1. Raspberry Pi Korean
   * Korean Code
    
       ```bash
       $ sudo apt-get install fonts-unfonts-core
       
       (recommend reboot Raspberry Pi)
       ```

#### 1-2. Install tensorflow
   * Install Tensorflow Code
       
       ```bash
       $ sudo apt-get install -y libhdf5-dev libc-ares-dev libeigen3-dev gcc gfortran libgfortran5 libatlas3-base libatlas-base-dev libopenblas-dev libopenblas-base libblas-dev liblapack-dev cython3 libatlas-base-dev openmpi-bin libopenmpi-dev python3-dev

       $ sudo apt-get install -y libhdf5-dev libc-ares-dev libeigen3-dev gcc gfortran libgfortran5 libatlas3-base libatlas-base-dev libopenblas-dev libopenblas-base
       libblas-dev liblapack-dev cython3 libatlas-base-dev openmpi-bin libopenmpi-dev python3-dev build-essential cmake pkg-config libjpeg-dev libtiff5-dev libpng-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libfontconfig1-dev libcairo2-dev libgdk-pixbuf2.0-dev libpango1.0-dev libgtk2.0-dev libgtk-3-dev libhdf5-serial-dev libhdf5-103 libqt5gui5 libqt5webkit5 libqt5test5

       $ sudo pip3 install pip --upgrade
       $ sudo pip3 install keras_applications==1.0.8 --no-deps
       $ sudo pip3 install keras_preprocessing==1.1.0 --no-deps
       $ sudo pip3 install numpy==1.22.1
       $ sudo pip3 install h5py==3.1.0
       $ sudo pip3 install pybind11
       $ pip3 install -U --user six wheel mock
       $ wget "https://raw.githubusercontent.com/PINTO0309/Tensorflow-bin/main/tensorflow-2.8.0-cp39-none-linux_aarch64_numpy1221_download.sh"
       $ sudo chmod +x tensorflow-2.8.0-cp39-none-linux_aarch64_numpy1221_download.sh
       $ ./tensorflow-2.8.0-cp39-none-linux_aarch64_numpy1221_download.sh
       $ sudo pip3 uninstall tensorflow
       $ sudo -H pip3 install tensorflow-2.8.0-cp39-none-linux_aarch64.whl

       【Required】 Restart the terminal.
       ```
      [출처 Github](https://github.com/PINTO0309/Tensorflow-bin)

#### 1-3. Install OpenCV
   * Install OpenCV Code
   
       ```bash
       $ python3 -m pip install opencv-python
       or
       $ pip install opencv-contrib-python (more libraries and customization)
       ```

#### 1-4. Install Google Translation
   * Install Google Translation api Code
   
       ```bash
       $ pip install googletrans==4.0.0-rc1
       ```

### 1-5. Install GTTS / pandas / preferredsoundplayer
   * Install GTTS / pandas / prefferedsoundplayer Code
   
       ```bash
       $ pip install gtts
       $ pip install pandas
       $ pip install preferredsoundplayer
       ```

#### 1-6. Install Google Vision
   * Install Google Vision Code

       ```bash
       $ sudo apt install libjpeg8-dev python-picamera
       $ sudo pip install --upgrade google-api-python-client google-cloud google-cloud-vision
       $ sudo pip install --upgrade Pillow
       $ sudo pip uninstall requests
       $ sudo pip install --upgrade requests
       $ sudo pip install --upgrade urllib3
       $ sudo pip install --upgrade chardet
       $ sudo apt-get install python-pip python-requests python-pycurl
       $ sudo pip install google-api-python-client
       $ cd
       $ vi ~/.bashrc
       $ export GOOGLE_APPLICATION_CREDENTIALS="input own api path"
       :wq
       $ source ~/.bashrc
       ```
      
      [Google 공식 문서](https://cloud.google.com/vision/docs/setup#linux-or-macos)

#### 1-7. Install pytesseract
   * Install pytesseract Code
   
       ```bash
       $ sudo apt-get  install  tesseract-ocr  libtesseract-dev libleptonica-dev 
       $ sudo apt-get install autoconf automake libtool pkg-config libpng12-dev libjpeg8-dev libtiff5-dev zlib1g-dev
       $ sudo apt-get install libleptonica-dev
       $ sudo apt install tesseract-ocr tesseract-ocr-kor
       $ sudo apt install tesseract-ocr-script-hang tesseract-ocr-script-hang-vert
       $ sudo pip3 install pytesseract
       ```

___

## 2. Set Raspberry Pi pwd
   * Set pwd
   
       ```bash
       $ cd ~./Smart_Glass
       ```

___

## 3. Add omission file

* Add "sound" folder    (start at pwd ~./Smart_Glass)
    * path : ./tts/sound
      
        ```bash
        $ cd tts
        $ mkdir sound
        ```

* Add "testDataset" adn "a" folder     (start at pwd ~./Smart_Glass)
    * path : ./korBrailleCode/testDataset/a

        ```bash
        $ cd korBrailleCode
        $ mkdir testDataset
        $ mkdir PresetData
        $ cd testDataset   
        $ mkdir a
        ```

    * path : ./EnBrailleCode/testDataset/a

        ```bash
        $ cd EnBrailleCode
        $ mkdir testDataset
        $ mkdir PresetData
        $ cd testDataset
        $ mkdir a
        ```

___

## 2022 Hansung University Capstone Design
