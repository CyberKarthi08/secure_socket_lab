import socket
import select as select_la

HOST = ""
PORT = 65534
user_name_0 = []
SOCKETS_LIST = []


def broadcast(server_sockets_0, team_member, param):
    pass


class team_member_sockets:

    def __init__(self=None, server_sockets_0=None, name_0=None):
        self.server_sockets_0 = None
        print("hello") # logo
        # TODO :  When implement to logo designs
        name_0 = input("Who are you : ")
        user_name_0.append(name_0)

    def setup_server_socket(self=None):
        self.server_sockets_0 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_sockets_0.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        self.server_sockets_0.bind((HOST, PORT))
        self.server_sockets_0.listen()
        SOCKETS_LIST.append(self.server_sockets_0)
        print(f"Hey! Hi {user_name_0} Welcome to our Termi_Lab")

    def set_users_details(self=None):
        while True:
            r_data, w_date, e_data = select_la.select(SOCKETS_LIST, [], [], 2)
            for accept_data in r_data:
                if accept_data == self.server_sockets_0:
                    team_member, addr = self.server_sockets_0.accept()
                    SOCKETS_LIST.append(team_member)
                    print("{} connection established {}:{}".format( user, addr[0], addr[1]))
                    print(self.server_sockets_0, team_member, "{}@{} Lets get started".format(user_name_0, addr[0]))
                else:
                    exit()




demo = team_member_sockets()
demo.setup_server_socket()
