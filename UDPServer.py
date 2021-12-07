# Programa basado en el ejemplo de https://pythontic.com/modules/socket/udp-client-server-example
# Servidor UDP que recibe mensajes de texto del cliente y los retorna en mayúsculas.
# coding=utf-8
import socket  # Biblioteca que permite hacer objetos de tipo socket.


# Dirección de LocalHost. Conexión IP a la computadora siendo utilizada.
localIP = "127.0.0.1"

# Registered para UDP. No esta reservado como un well-known port.
localPort = 20001

# Tamaño del buffer mientras se verifica si el dato llegó correctamente.
bufferSize = 1024

# Se declara un socket.
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Se asocia el socket con el puerto.
UDPServerSocket.bind((localIP, localPort))
# Mensaje para verificar que el servidor está funcionando.
print("Servidor UDP activado")

# Constantemente revisar por nuevos datagramas
while(True):
    # Se utiliza recfrom para leer el dato del cliente
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    # recvfrom retorna un arreglo. [0] contiene el mensaje
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]  # [1] contiene la dirección del cliente

    clientMsg = "Mensaje del cliente: {}".format(
        str(message, 'utf-8'))  # Se formatea el mensaje del cliente
    clientIP = "Dirección IP del cliente: {}".format(
        address)  # Se formatea la dirección IP del cliente

    # upper() capitaliza el mensaje del cliente.
    bytesToSend = str.encode(format(message.upper()))

    # Se imprimen los mensajes para verificar funcionamiento.
    print(clientMsg)
    print(clientIP)

    # Se envía mensaje en mayúsculas al cliente.
    UDPServerSocket.sendto(bytesToSend, address)


# Explicar como se hace con solo una compu: LocalHost
# Explicar conceptos de como hacer programa: Como funciona el UDP client y server
# Explicara cada instrucci[on de los programas, explicar las instrucciones utilizadas y hacer un diagrama de bloques del programa
# Cuantas conexiones cliente servidor son posibles
# Tamano maximo del datagrama
