import construct
from hexdump import dehex
request_struct = construct.Struct(
    construct.Const(dehex("00 00 27 14 00 00 00 00")),  # request
    construct.Padding(16), # bytes
    construct.Padding(16), # bytes
    'mac' / construct.PaddedString(16, "ascii"),
    construct.Padding(16), # bytes
    'seq' / construct.Int32ub  # unsigned/big-endian (i.e. 00 00 00 01)
    #'cmdLen' / construct.Int32ub
    # TODO: command
)

class Commands:
    on = dehex('ff ff 0a 00 00 00 00 00 00 01 4d 02 5a')

def command_req(mac, seq, cmd_data):
    return request_struct.build({"mac": mac, 'seq': seq}) + \
        construct.Int32ub.build(len(cmd_data)) + \
            cmd_data

