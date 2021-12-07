# coding=utf-8
# Programa basado en el ejemplo de https://pythontic.com/modules/socket/udp-client-server-example
# Cliente UDP que envía mensajes de texto al servidor y los recibe en mayúsculas.

import socket
import time
import sys

# Declaro la dirección IP del servidor y el puerto del socket.
serverAddressPort = ("127.0.0.1", 20001)
bufferSize = 1024

# Lista de caracteres para transmitir.
caracteres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
              'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w']

# Creo un socket para el cliente.
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

transmitting = True
i = 0
# Usar el socket UDP para transmitir constantemente.
while transmitting:
    try:
        # Mensaje por enviar.
        bytesToSend = str.encode('Mensaje: ' + caracteres[i])
        print(sys.getsizeof(bytesToSend))
        # Uso sendto() para enviar a direccion del servidor.
        UDPClientSocket.sendto(bytesToSend, serverAddressPort)

        # Uso recvfrom() para recibir respuesta del servidor
        msgFromServer = UDPClientSocket.recvfrom(bufferSize)
        print("Mensaje enviado {}".format(str(bytesToSend, 'utf-8')))
        print("Mensaje recibido {}".format((msgFromServer[0])))

        # Progresar por la lista de caracteres
        i = i+1
        if i == len(caracteres):
            i = 0
        print("CTRL+C para terminar transmisión de datos.")
        time.sleep(1)  # Retardo para poder observar datos enviados
    except KeyboardInterrupt:
        # Se detiene la transmision y termina el programa.
        transmitting = False
        break
