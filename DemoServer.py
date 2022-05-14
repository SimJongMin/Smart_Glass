from socket import *
from korBrailleCode import korBrailleCNN
from Braille_Translator import main

# =====================================================================================================
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('192.168.219.103', 9658))  # IP주소, PORT번호. 이거 데모날에 그쪽 WIFI 주소에 맞춰 바꿔야한다.
server_socket.listen()
# =====================================================================================================
while True:
# =====================================================================================================
    print("\n서버: 접속 대기중...")
    client_socket, addr = server_socket.accept()
    print("서버: " + str(addr) + " 에서 접속됨.")
# =====================================================================================================
    data = client_socket.recv(4)
    img_size = int.from_bytes(data, "little");
# =====================================================================================================
    data = client_socket.recv(img_size)
    file = open("recieved.jpg", 'wb')
    file.write(data)
    file.close()
    print("서버: 사진 수신 완료.")
# =====================================================================================================
    lists = korBrailleCNN.serverAction("recieved.jpg")
    plain_text = main.trans(lists)
# =====================================================================================================
    client_socket.send(plain_text.encode('utf-8'))
    print("서버: 번역 송신 완료.")
# =====================================================================================================
    client_socket.close()

server_socket.close()
