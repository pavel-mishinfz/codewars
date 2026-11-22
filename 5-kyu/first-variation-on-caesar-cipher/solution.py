import string
import math


NUM_RUNNERS = 5
LEN_ALPHABET = len(string.ascii_lowercase)
ALPHABET_DICT = {i: string.ascii_lowercase[i] for i in range(LEN_ALPHABET)}


def moving_shift(s, shift):
    encode_str = ''
    for ch in s:
        if ch.lower() not in ALPHABET_DICT.values():
            encode_str += ch
            shift += 1
            continue
        encode_ch_id = (ord(ch.lower()) - ord('a') + shift) % LEN_ALPHABET
        encode_ch = ALPHABET_DICT[encode_ch_id]
        encode_str += encode_ch.upper() if ch.isupper() else encode_ch
        shift += 1
    n = math.ceil(len(encode_str) / NUM_RUNNERS)
    return [encode_str[i:i + n] for i in range(0, n*NUM_RUNNERS, n)]

def demoving_shift(s, shift):
    decode_str = ''
    encode_str = ''.join(s)
    for encode_ch in encode_str:
        if encode_ch.lower() not in ALPHABET_DICT.values():
            decode_str += encode_ch
            shift += 1
            continue
        decode_ch_id = (ord(encode_ch.lower()) - ord('a') - shift)
        m = 1
        if abs(shift) > LEN_ALPHABET:
            m = math.ceil(abs(shift) / LEN_ALPHABET)
        decode_ch_id = (decode_ch_id + m*LEN_ALPHABET) % LEN_ALPHABET if decode_ch_id < 0 else decode_ch_id % LEN_ALPHABET
        decode_ch = ALPHABET_DICT[decode_ch_id]
        decode_str += decode_ch.upper() if encode_ch.isupper() else decode_ch
        shift += 1
    return decode_str