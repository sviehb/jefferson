import lzma
import struct

LZMA_BEST_LC = 0
LZMA_BEST_LP = 0
LZMA_BEST_PB = 0

pb = LZMA_BEST_PB
lp = LZMA_BEST_LP
lc = LZMA_BEST_LC
PROPERTIES = (pb * 5 + lp) * 9 + lc

DICT_SIZE = 0x2000


def decompress(data, outlen):
    lzma_header = struct.pack("<BIQ", PROPERTIES, DICT_SIZE, outlen)
    lzma_data = lzma_header + data
    decompressed = lzma.decompress(lzma_data)
    return decompressed
