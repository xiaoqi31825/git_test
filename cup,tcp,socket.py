""""
网络传输的分层:
    应用层-socket-传输层---网络层---网络接口层
"""""

# with语句可自动释放资源


"""
UDP:
    传输数据无法保证数据的完整性，正确性和可靠性,双方两端在传输完成数据结束后不再传输数据，需要释放连接（即过程为四次挥手）
    TCP的传输速度相对于UDP来说慢一点,双方传输数据通讯时，当收到数据的一方需要给发数据的一方应答回复收到数据的信号，传输的数据能够保证数据完整，正确，可靠。
"""
# UDP接收数据
import socket
# 创建UDP套接字            IPV4            UDP 用户数据报协议
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    # 使用
    data = input("请输入你要发送的数据:")
    # 发送数据需要送到的 目的地址(IP, port)
    dest_address = ('192.168.20.132', 8080)
    udp_socket.sendto(data.encode(), dest_address)
    # 接收数据(b'hahahahha', ('192.168.20.132', 8080))
    # 是bytes类型的数据       远程地址(IP PORT)
    data, remote_address = udp_socket.recvfrom(4096)
    print("收到来自%s的数据:%s" % (str(remote_address), data))
    # 记得关闭 10000个 10001一个进程所能打开的文件等系统资源是有限制的
    # 使用系统资源  关闭套接字
    udp_socket.close()

# UDP发送数据
import socket
#echo 回射
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 将本地端口８８８８占用　　放置操作系统随机分配
udp_socket.bind(('', 8888))
while True:
    data, remote_address = udp_socket.recvfrom(4096)
    print("收到来自%s的数据:%s" % (str(remote_address), data))
    # udp_socket.sendto("1234567890".encode(), ("192.168.20.132", 8080))
    udp_socket.sendto(data, remote_address)
    udp_socket.close()



"""
TCP:
    称为传输控制协议,
    面向连接,两端在收发传输数据之前必须先建立连接，tcp通信过程是创建连接，数据传送，终止连接共三个步骤
"""
# tcp客户端
import socket
import time
# 创建ＴＣＰ套接字
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 拨号　－－　连接服务器
tcp_socket.connect(('192.168.20.133', 8888))
# 开始说话 --- 发数据
# send就是发送数据使用的 返回值就是成功发送的字节数<了解>
data = input("data:")
tcp_socket.send(data.encode())
# 听别人说话　－－　收数据
# 参数是本次收数据的最大长度　返回值就是收到的ｂｙｔｅｓ类型的数据
# 如果没有收到数据　就会一直阻塞等待
# 如果对方关掉该socket  那么我们recv收到一个0字节的数据
recv_data = tcp_socket.recv(4096)
if recv_data:
    print("收到数据：%s" % recv_data.decode())
else:
    print("对方已经关闭连接")
# 关掉ＴＣＰ　套接字　－－　挂电话
tcp_socket.close()


# tcp服务器
import socket
# 创建本地套接字 -- 总机
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定本地地址   -- 10086
tcp_socket.bind(('', 8010))
# 讲套接字变为被动-- 安装一个前台 客户服务系统 并且设置 等待服务区的大小
tcp_socket.listen(128)
# 从等待服务区中取出一个客户套接字
# client_socket是客户端套接字 使用这个套接字和客户进行通信
# client_addr  是客户端地址   可以表示客户
while True:
    client_socket, client_addr = tcp_socket.accept()
    print("接受到来自%s的连接请求 " % str(client_addr))
    # echo 回射服务器
    recv_data = client_socket.recv(4096)
    if recv_data:
        print("收到来自%s的数据：%s" % (str(client_addr), recv_data))
        client_socket.send(recv_data)
    else:
        print("收到来自%s的断开请求" % str(client_addr))
        client_socket.close()
        tcp_socket.close()


""""""


"""
相同点:
    UDP和TCP都是传输层协议，不同传输协议的socket 可以占用同一个端口
    两个UDP的socket 或两个TCP的socket 不能使用共用一个端口
"""







