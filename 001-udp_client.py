import socket

HOST = '127.0.0.1'
PORT = 9997

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto(b'AAABBBCCC', (HOST, PORT))

data, address = client.recvfrom(4096)
print(data.decode('utf-8'))
print(address.decode('utf-8'))

client.close()

'''
import socket # Esta línea importa el módulo de Python llamado socket,
              # que proporciona una interfaz de bajo nivel para la 
              # programación de red y la comunicación entre procesos.

HOST = '127.0.0.1' # Aquí se define una constante HOST que representa 
                   # la dirección IP del host al que se va a conectar, 
                   # en este caso, la dirección IP local.

PORT = 9997 # Esta línea define una constante PORT que representa el 
            # número de puerto al que se va a conectar.

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Esta línea crea un nuevo objeto de socket utilizando la 
                                                          # familia de direcciones AF_INET (que representa las 
                                                          # direcciones IPv4) y el tipo de socket SOCK_DGRAM 
                                                          # (que representa las conexiones UDP).

client.sendto(b'AAABBBCCC', (HOST, PORT)) # Esta línea envía un mensaje UDP al servidor.
                                          # La cadena que se envía debe estar en formato 
                                          # binario, por lo que se antepone con b.

data, address = client.recvfrom(4096) #Esta línea recibe la respuesta del servidor. 
                                      # El número 4096 es el tamaño máximo de los 
                                      # datos que se pueden recibir a la vez.

print(data.decode('utf-8')) # Esta línea imprime los datos recibidos del servidor. 
                            # Como los datos recibidos están en formato binario, 
                            # deben ser decodificados a una cadena utilizando ‘utf-8’.

print(address.decode('utf-8')) # Esta línea intenta imprimir la dirección del servidor 
                               # desde donde se recibieron los datos. 
                               # Sin embargo, esta línea dará un error ya que ‘address’ 
                               # es una tupla que contiene una cadena (dirección IP) y 
                               # un entero (número de puerto), y las tuplas no pueden 
                               # ser decodificadas a una cadena.

client.close() # Finalmente, esta línea cierra el socket.
'''