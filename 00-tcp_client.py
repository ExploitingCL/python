import socket # Esta linea importa el modulo de Python llamado socket, que proporciona una interfaz de bajo nivel para la programacion de red y la comunicacion entre procesos.

HOST = 'www.google.com' # Aqui se define una constante HOST que representa el nombre del host al que se va a conectar, en este caso, el sitio web Google.
PORT = 80 # Esta linea define una constante PORT que representa el numero de puerto al que se va a conectar. El puerto 80 es el puerto estandar para las conexiones HTTP.

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Esta linea crea un nuevo objeto de socket utilizando la familia de direcciones AF_INET (que representa las direcciones IPv4) y el tipo de socket SOCK_STREAM (que representa las conexiones TCP).
client.connect((HOST, PORT)) # Esta linea intenta establecer una conexion TCP con el host y puerto especificados.

client.send(b'GET / HTTP/1.1\r\nHost: google.com\r\n\r\n') # Esta linea envia una solicitud HTTP GET al servidor. La cadena que se envia debe estar en formato binario, por lo que se antepone con b.
response = client.recv(4096) # Esta linea recibe la respuesta del servidor. El numero 4096 es el tamaño maximo de los datos que se pueden recibir a la vez.
print(response.decode('utf-8')) # Esta linea imprime la respuesta del servidor. Como los datos recibidos estan en formato binario, deben ser decodificados a una cadena utilizando 'utf-8'.

client.close() # Finalmente, esta linea cierra la conexion al servidor.
