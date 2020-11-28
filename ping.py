import socket;
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# host = '40.76.231.100'
print("Ingrese la Ip o nombre del host:")
Host = input()
print(f"Buscando puertos abiertos en el host:, {Host}")
for puerto in range(0, 65536):
    result = sock.connect_ex((Host,puerto))
    if result == 0:
        print ('El puerto: ', puerto, ' esta abierto en el host: ' + Host)
