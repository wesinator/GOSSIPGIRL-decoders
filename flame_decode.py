# https://storage.googleapis.com/chronicle-research/Flame%202.0%20Risen%20from%20the%20Ashes.pdf


def DecodeMethod1(indata, r_start, r_length):
    dec_data = ""
    enc_data = indata[r_start:]
    dec_len = ord(indata[r_length])

    for index, byte in enumerate(enc_data[:dec_len]):
            eax = (
                    (((dec_len - index) -1) ^ 0x1D) * ((dec_len - index) + 0x10)
                    ) & 0xFFFFFFFF
            eax += 0x1000193
            cl = ( ((eax >> 0x18) & 0xFF) ^ ((eax >> 0x10) & 0xFF) )
            cl = ( cl ^ ((eax >> 0x8) & 0xFF) )
            cl = ( cl ^ ord(byte)) & 0xFF
            cl = ( cl ^ (eax & 0xFF) )
            dec_data += chr(cl)

    return dec_data


def DecodeMethod2(indata, key, r_start, r_length):
    enc_data = indata[r_start:]
    dec_length = ord(indata[r_length])
    dec_data = ""
    for index, byte in enumerate(enc_data[:dec_length]):
        if ord(enc_data[index]) == 0 and ord(enc_data[index+1]) == 0: break
        dec_data += chr( ord(byte) ^ ord(key[index % len(key)]) )

    return dec_data
