import socket
import datetime


server_conf ={
    "host":"127.0.0.1",
    "port":6500
    }

filename = input(">> enter name of the new file :") or "default"



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.connect((server_conf["host"], server_conf["port"]))
    header = server.recv(1024)
    max_size = header.decode("utf-8").split(":")[1]
    sender_machine = header.decode("utf-8").split(":")[3]
    filesize = header.decode("utf-8").split(":")[5]
    fileformat = header.decode("utf-8").split(":")[7]

    print("data are receving from {} with maximum size of {}".format(sender_machine, max_size))


    start = datetime.datetime.now()
    with open(filename+"."+fileformat, "wb") as image:
        counter = 0
        print("please wait ...")
        while True:
            data = server.recv(int(max_size))
            image.write(data)
            counter+=int(max_size)
            
            
            if not data:
                print("scssfly transfered",end = " ")
                break
    end = datetime.datetime.now()

    print("in ",(end - start))

