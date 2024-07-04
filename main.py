import socket as socket_0
import select
import threading as th

HOST = ''
PORT = 58761
SOCKETS_LIST = []


class team_member_sockets:

	def __init__(self):
		self.server_sockets_0 = None
		print("\n[+] Termi lab_server let's running......\n")

	def setup_server_socket(self):
		self.server_sockets_0 = socket_0.socket(socket_0.AF_INET, socket_0.SOCK_STREAM)
		self.server_sockets_0.setsockopt(socket_0.SOL_SOCKET, socket_0.SO_REUSEADDR, True)
		self.server_sockets_0.bind((HOST, PORT))
		self.server_sockets_0.listen(10)
		SOCKETS_LIST.append(self.server_sockets_0)
		print(f"[+] Listening on {HOST}: {PORT}\n")
		print("[>]", self.server_sockets_0, "\n")

	def connection_handling(self):
		while True:
			# r_data, _, _ = select.select(SOCKETS_LIST, [], [],2)
			# for accept_data in SOCKETS_LIST:
			# 	if SOCKETS_LIST == self.server_sockets_0:
			client_socket_data, client_socket_addr = self.server_sockets_0.accept()
			SOCKETS_LIST.append(client_socket_addr)
			while True:
				first_user_data_0 = client_socket_data.recv(1024)
				first_user_data_0 = first_user_data_0.decode("utf-8")
				print("[@] Hey, Hi ", format(first_user_data_0))
				print(f"\t[->]Your connection established {client_socket_addr[0]}:{client_socket_addr[1]}")

# print(self.server_sockets_0, team_member, "{}@{} Lets get started".format(user_name_0, addr[0]))
# Incoming message from a client

if __name__ == "__main__":
	team_socket = team_member_sockets()
	team_socket.setup_server_socket()
	team_socket.connection_handling()
