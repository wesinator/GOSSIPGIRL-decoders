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


def decryptstring(enc_pointer):
    decoded = ""
    rindex = 0
    index = 0
    while True:
        indata = idc.GetManyBytes(enc_pointer + index, 4)
        eax = index & 80000001

        teax = struct.unpack('<I', indata)[0]
        if rindex % 2 == 1:
            eax = teax ^ 0xBF97BF97
        else:
            eax = teax ^ 0xFFFFE068

        decoded += struct.pack('<I', eax)
        if eax & 0xFFFF0000 == 0:
            break
        rindex += 1
        index += 4
    return clean_str
