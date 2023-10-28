import socket # Esta linea importa el modulo de Python llamado socket, que proporciona una interfaz de bajo nivel para la programacion de red y la comunicacion entre procesos.

HOST = '127.0.0.1' # Aqui se define una constante HOST que representa la direccion IP del host al que se va a conectar, en este caso, la direccion IP local.
PORT = 9997 # Esta linea define una constante PORT que representa el numero de puerto al que se va a conectar.

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Esta linea crea un nuevo objeto de socket utilizando la familia de direcciones AF_INET (que representa las direcciones IPv4) y el tipo de socket SOCK_DGRAM (que representa las conexiones UDP).
client.sendto(b'AAABBBCCC', (HOST, PORT)) # Esta linea envia un mensaje UDP al servidor. La cadena que se envia debe estar en formato binario, por lo que se antepone con b.

data, address = client.recvfrom(4096) # Esta linea recibe la respuesta del servidor. El numero 4096 es el tamaño maximo de los datos que se pueden recibir a la vez.
print(data.decode('utf-8')) # Esta linea imprime los datos recibidos del servidor. Como los datos recibidos estan en formato binario, deben ser decodificados a una cadena utilizando 'utf-8'.
print(address.decode('utf-8')) # Esta linea intenta imprimir la direccion del servidor desde donde se recibieron los datos. Sin embargo, esta linea dara un error ya que 'address' es una tupla que contiene una cadena (direccion IP) y un entero (numero de puerto), y las tuplas no pueden ser decodificadas a una cadena.

client.close() # Finalmente, esta linea cierra este codigo.
