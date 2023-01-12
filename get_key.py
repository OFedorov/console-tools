import ctypes
import os

gk = ctypes.CDLL(os.path.dirname(os.path.realpath(__file__))+'/libget_key.so')
gk.get_key.restype = ctypes.c_char_p


class KEY:
    ESC       = b'\x1b'
    ENTER     = b'\n'
    TAB       = b'\t'
    BACKSPACE = b'\x7f'
    DELETE    = b'\x1b[3~'
    BACK      = b'\x1b[D'
    FORWARD   = b'\x1b[C'
    UP        = b'\x1b[A'
    DOWN      = b'\x1b[B'

    C_BACKSPACE = b'\x08'
    C_DELETE    = b'\x1b[3;5~'
    C_BACK      = b'\x1b[1;5D'
    C_FORWARD   = b'\x1b[1;5C'
    C_UP        = b'\x1b[1;5A'
    C_DOWN      = b'\x1b[1;5B'

    S_TAB       = b'\x1b[Z'
    S_BACKSPACE = b'\x7f'
    S_DELETE    = b'\x1b[3;5~'
    S_BACK      = b'\x1b[1;2D'
    S_FORWARD   = b'\x1b[1;2C'
    S_UP        = b'\x1b[1;2A'
    S_DOWN      = b'\x1b[1;2B'


def get_key():
    return gk.get_key()
