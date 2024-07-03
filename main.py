import socket
import select
import threading as th

HOST = ""
PORT = 5658
SOCKETS_LIST = []


class team_member_sockets:

	def __init__(self=None, server_sockets_0=None):
		self.server_sockets_0 = server_sockets_0
		print("hello")  # logo

	# TODO :  When implement to logo designs

	def setup_server_socket(self=None,):
		server_sockets_0 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server_sockets_0.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
		server_sockets_0.bind((HOST, PORT))
		server_sockets_0.listen(2)
		print(f"Listening on {HOST}:{PORT}")
		SOCKETS_LIST.append(server_sockets_0)
		print(SOCKETS_LIST)


	def connection_handling(self):
		while True:
			r_data, _, _ = select.select(SOCKETS_LIST, [], [])
			for accept_data in r_data:
				if accept_data == self.server_sockets_0:
					team_member, addr = self.server_sockets_0.accept()
					SOCKETS_LIST.append(team_member)
					print(f"Connection established {addr[0]}:{addr[1]}")
				# print(self.server_sockets_0, team_member, "{}@{} Lets get started".format(user_name_0, addr[0]))
				# Incoming message from a client
				else:
					try:
						# Receive data from the client
						data = accept_data.recv(1024)
						if data:
							# Broadcast the message to all clients
							message = data.decode("utf-8")
							print(f"Received message: {message}")

							# Echo back to the client
							accept_data.send(bytes(message, "utf-8"))

						else:
							# Remove the socket that's broken
							if accept_data in SOCKETS_LIST:
								SOCKETS_LIST.remove(accept_data)

					except Exception as e:
						print(f"Exception: {e}")
						continue


if __name__ == "__main__":
	team_socket = team_member_sockets()
	team_socket.setup_server_socket()
	team_socket.connection_handling()
