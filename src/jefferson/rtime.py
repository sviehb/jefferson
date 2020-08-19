def decompress(data_in, destlen):
    positions = [0] * 256
    cpage_out = bytearray([0] * destlen)
    outpos = 0
    pos = 0
    while outpos < destlen:
        value = ord(data_in[pos])
        pos += 1
        cpage_out[outpos] = value
        outpos += 1
        repeat = ord(data_in[pos])
        pos += 1

        backoffs = positions[value]
        positions[value] = outpos
        if repeat:
            if backoffs + repeat >= outpos:
                while repeat:
                    cpage_out[outpos] = cpage_out[backoffs]
                    outpos += 1
                    backoffs += 1
                    repeat -= 1
            else:
                cpage_out[outpos : outpos + repeat] = cpage_out[
                    backoffs : backoffs + repeat
                ]
                outpos += repeat
    return str(cpage_out)
