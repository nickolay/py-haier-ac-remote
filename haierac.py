from haierlib.types import *
from haierlib.parsers import *
from haierlib.commands import Commands
import socket
import sys
import select

class HaierAC:
    def __init__(self, ip, mac, port = 56800, timeout = 500) -> None:
        self._ip = ip
        self._port = port
        self._mac = mac
        self._timeout = timeout
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._seq = 0

    def test_recv_loop(self):
        self._sock.connect((self._ip, self._port))
        self._sock.setblocking(False)
        while True:
            input_ready, _, _ = select.select([self._sock.fileno(),
                                               sys.stdin.fileno()], [], [])
            for fd in input_ready:
                if fd == self._sock.fileno():
                    recv_data = self._sock.recv(1000)
                    if recv_data:
                        print("-- Has Data --")
                        import hexdump
                        hexdump.hexdump(recv_data)
                        print(parse_resp(recv_data))
                elif fd == sys.stdin.fileno():
                    cmd = sys.stdin.readline().strip()
                    if cmd == "on":
                        self.send_on()
                    elif cmd == "off":
                        self.send_off()
                    else:
                        print(f"Unknown cmd {cmd}")
                else:
                    assert False, f"Unexpected fd = {fd}"

    # TODO complete socket functions

    # TODO complete send behavior functions
    def send_hello(self):
        pass

    def send_init(self):
        pass

    def send_on(self):
        d = Commands.build_request(mac=self._mac, seq=1, cmd_data=Commands.on)
        self._sock.send(d)

    def send_off(self):
        d = Commands.build_request(mac=self._mac, seq=1, cmd_data=Commands.off)
        self._sock.send(d)

    def change_State(self):
        pass
