import socket
import os
import sys
import time


header = "maxsize:1048576:sender:localhsot"


server_conf ={
    "host":"127.0.0.1",
    "port":6500
    }


filepath = sys.argv[1]
print("file name is ",filepath)
if not filepath:
    print("file path is not provided")

file_format = filepath.split(".")[-1:][0]
print("file name is ",file_format)



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((server_conf["host"], server_conf["port"]))

    server.listen()

    conn ,addr = server.accept()

    print(" connected to {} with address {} ".format(conn,addr))



    with open(filepath,"rb") as image:
        header+=":filesize:"+str(os.path.getsize(filepath))
        header+=":fileformat:"+str(file_format)
        conn.send(header.encode("utf-8"))
        counter = 0
        while True:
            image.seek(counter)
            data = image.read(1048576)
            if (not data):
                print("file successfuly transfered",counter)
                break
                
            counter+=1048576
            conn.send(data)

            

