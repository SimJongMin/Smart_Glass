from socket import *
from korBrailleCode import korBrailleCNN
from Braille_Translator import translate_braille
from tts import imgTextTrans
from googletrans import Translator


server_socket = socket(AF_INET, SOCK_STREAM)
# IP주소, PORT번호. 이거 데모날에 그쪽 WIFI 주소에 맞춰 바꿔야한다.
server_socket.bind(('192.168.219.106', 9658))
server_socket.listen()

while True:
    print("\n서버: 접속 대기중...")
    client_socket, addr = server_socket.accept()
    print("서버: " + str(addr) + " 에서 접속됨.")

    data = client_socket.recv(4)  # 모드
    prtc = int.from_bytes(data, "little")

    data = client_socket.recv(4)  # 전송받을 이미지의 크기
    img_size = int.from_bytes(data, "little")

    file = open("./demoImage/recieved.jpg", 'wb')
    transfered = 0
    while transfered < img_size:
        data = client_socket.recv(img_size)  # 이미지
        transfered = transfered + len(data)
        file.write(data)
    file.close()
    print("서버: 사진 수신 완료.")

    if prtc == 0:
        print("서버: 1_main 점자 번역 모드.")

        lists = korBrailleCNN.serverAction("./demoImage/recieved.jpg")
        plain_text = translate_braille.trans(lists)

        client_socket.send(plain_text.encode('utf-8'))
        print("서버: 1_main 번역 송신 완료.")

    if prtc == 1:
        print("서버: 2_main 글자 번역 모드.")

        trans = Translator()
        plain_text = imgTextTrans.serverMainStart(trans, "./demoImage/recieved.jpg")

        client_socket.send(plain_text.encode('utf-8'))
        print("서버: 2_main 번역 송신 완료.")

    client_socket.close()

server_socket.close()
