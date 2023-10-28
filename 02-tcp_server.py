import socket # Este modulo en Python proporciona acceso ala interfaz de sockets BSD.
import threading # Este modulo constituye interfaces de threading de alto nivel sobre el modulo _thread de nivel inferior.

IP = '0.0.0.0' # Esta es la direccion IP en la que el servidor estara escuchando. '0.0.0.0' significa que el servidor estara escuvhando en todas las direcciones IP de la maquina actual.
PORT = 9998 # Este es el puerto en el que el servidor estara escuchando.

def main(): # Esta es la funcion principal que se ejecutara cuando se inicie el script.
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Esto crea un nuevo objeto socket utilizando la familia de direcciones AF_INET (IPv4) y el tipo de socket SOCK_STREAM (TCP).
    server.bind((IP, PORT)) # Esto vincula el socket al IP y puerto especificados.
    server.listen(5) # Esto hace que el servidor comience a escuchar conexiones entrantes, con una cola maxima de 5 conexiones.
    print(f'[*] Listening on {IP}:{PORT}') # Esto imprime un mensaje indicando que el servidor esta escuchando.

    while True: # Este es un bucle infinito para aceptar multiples conexiones.
        client, address = server.accept() # Esto acepta una nueva conexion y devuelve un nuevo socket y la direccion del cliente.
        print(f'[*] Accepted connection from {address[0]}:{address[1]}') # Esto imprime un mensaje indicando que se ha aceptado una nueva conexion.
        client_handler = threading.Thread(target=handle_client, args=(client,)) # Esto crea un nuevo objeto Thread que apunta a la funcion handle_client y pasa al cliente como argumento.
        client_handler.start() # Esto inicia el nuevo Thread y comienza a ejecutar la funcion handle_client.

def handle_client(client_socket): # Esta es la funcion que maneja la comunicacion con cada cliente conectado.
    with client_socket as sock: # Esto asegura que el socket se limpie correctamente despues de ser utilizado.
        request = sock.recv(1024) # Esto recibe datos del cliente hasta un maximo de 1024 bytes.
        print(f'[*] Received: {request.decode("utf-8")}') # Esto imprime los datos recibidos del cliente.
        sock.send(b'ACKKK') # Esto envia una respuesta al cliente.

if __name__ == '__main__': # Esto asegura que la funcion principal se ejecute solo cuando este script se ejecute directamente (no cuando se importe como un modulo).
    main() # Crea un objeto de socket y lo vincula a una dirección IP y puerto específicos. Comienza a escuchar conexiones entrantes en esa dirección IP y puerto. Cuando se acepta una nueva conexión, imprime un mensaje y luego inicia un nuevo hilo para manejar la conexión del cliente. Por lo tanto, cuando llamas a main() al final de tu código, estás iniciando el servidor y permitiéndole aceptar y manejar conexiones entrantes.
