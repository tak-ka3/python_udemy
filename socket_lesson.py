import socket

# TCP/IP通信
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #IPv4, TCPプロトコルを利用することを指定している
#   s.bind(('127.0.0.1', 50007)) # ホスト名とポート番号を指定する
#   s.listen(1) # ここで指定した数だけ並列的にリクエストを処理することができる
#   while True:
#     conn,addr = s.accept() # 接続の受信を行う
#     with conn:
#       while True:
#         data = conn.recv(1024)
#         if not data:
#           break
#         print('data: {}, addr: {}'.format(data, addr))
#         conn.sendall(b'Received: '+ data)


# UDP通信
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
  s.bind(('127.0.0.1', 50007))
  while True:
    data, addr = s.recvfrom(1024)
    print('data: {}, addr: {}'.format(data, addr))
