# https://storage.googleapis.com/chronicle-research/STUXSHOP%20Stuxnet%20Dials%20In%20.pdf page 6
key = "BA3750CF0DD6086B046B1F0BDBB3DF2A1F9D0DDDFE94764FB9A4C2F474BCC2".decode('hex')
for index, byte in enumerate(reg_data):
    out += chr(ord(byte) ^ (ord(key[index % len(key)])))
