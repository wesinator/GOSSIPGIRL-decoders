# https://storage.googleapis.com/chronicle-research/DuQu%201.5%20A%20Ghost%20in%20the%20Wires.pdf
def DecodeString(indata):
    key = 0x2230
    floatKey = 0
    decoded = ""
    for index in range(0, len(indata), 2):
        tmp = key ^ floatKey ^ struct.unpack('<h', indata[index:index+2])[0]
        decoded += struct.pack('<h', tmp)
        floatKey = tmp
        if indata[index:index+2] == "\x00\x00":
            break
    return decoded
