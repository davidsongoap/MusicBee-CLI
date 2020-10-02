#----------------------------------------------------------#
#- MusicBeeIPCSDK Py v2.0.0                               -#
#- Copyright © Kerli Low 2014                             -#
#- This file is licensed under the                        -#
#- BSD 2-Clause License                                   -#
#- See LICENSE_MusicBeeIPCSDK for more information.       -#
#----------------------------------------------------------#

import struct
from ctypes import *
from . constants import *
from . structs import *


# --------------------------------------------------------------------------------
# All strings are encoded in UTF-16 little endian
# --------------------------------------------------------------------------------

def pack_i(*int32s):
    """
    -Int32: 32 bit integer
    -Int32: 32 bit integer
    -...
    """
    
    cds = COPYDATASTRUCT()
    cds.dwData = 0
    
    num = len(int32s)
    
    cds.cbData = MBIPC_SIZEOFINT * num
    
    cds.lpData = cast(c_char_p(struct.pack(str(num) + "i", *int32s)), c_void_p)
    
    return cds

def pack_s(*strings):
    """
    -Int32:  Byte count of string
    -byte[]: String data
    -Int32:  Byte count of string
    -byte[]: String data
    -...
    """
    
    cds = COPYDATASTRUCT()
    cds.dwData = 0
    
    num = len(strings)
    
    encoded = [None] * num
    
    cds.cbData = MBIPC_SIZEOFINT * num
    
    for i in range(num):
        encoded[i] = strings[i].encode("UTF-16-LE")
        cds.cbData += len(encoded[i])
    
    data = b""
    for e in encoded:
        data += struct.pack("i", len(e)) + e

    cds.lpData = cast(c_char_p(data), c_void_p)
    
    return cds

def pack_si(string_1, *int32s):
    """
    -Int32:  Byte count of string
    -byte[]: String data
    -Int32:  32 bit integer
    -Int32:  32 bit integer
    -...
    """
    
    cds = COPYDATASTRUCT()
    cds.dwData = 0

    encoded = string_1.encode("UTF-16-LE")
    byte_count = len(encoded)
        
    num = len(int32s)
    
    cds.cbData = MBIPC_SIZEOFINT * (num + 1) + byte_count
    
    data = struct.pack("i", byte_count) + encoded + struct.pack(str(num) + "i", *int32s)

    cds.lpData = cast(c_char_p(data), c_void_p)
    
    return cds

def pack_sb(string_1, *bools):
    """
    -Int32:  Byte count of string
    -byte[]: String data
    -Int32:  bool
    -Int32:  bool
    -...
    """
    
    cds = COPYDATASTRUCT()
    cds.dwData = 0

    encoded = string_1.encode("UTF-16-LE")
    byte_count = len(encoded)
        
    num = len(bools)
    
    cds.cbData = MBIPC_SIZEOFINT * (num + 1) + byte_count
    
    data = struct.pack("i", byte_count) + encoded + struct.pack(str(num) + "i", *bools)

    cds.lpData = cast(c_char_p(data), c_void_p)
    
    return cds

def pack_sd(string_1, *doubles):
    """
    -Int32:  Byte count of string
    -byte[]: String data
    -double: 64-bit floating-point value
    -double: 64-bit floating-point value
    -...
    """
    
    cds = COPYDATASTRUCT()
    cds.dwData = 0

    encoded = string_1.encode("UTF-16-LE")
    byte_count = len(encoded)
        
    num = len(doubles)
    
    cds.cbData = MBIPC_SIZEOFDOUBLE * num + MBIPC_SIZEOFINT + byte_count
    
    data = struct.pack("i", byte_count) + encoded + struct.pack(str(num) + "d", *doubles)

    cds.lpData = cast(c_char_p(data), c_void_p)
    
    return cds

def pack_ssa(string_1, strings):
    """
    -Int32:  Byte count of string
    -byte[]: String data
    -Int32:  Number of strings in string array
    -Int32:  Byte count of string in string array
    -byte[]: String data in string array
    -Int32:  Byte count of string in string array
    -byte[]: String data in string array
    -...
    """
    
    cds = COPYDATASTRUCT()
    cds.dwData = 0
    
    encoded_1 = string_1.encode("UTF-16-LE")
    byte_count_1 = len(encoded_1)
    
    num = len(strings)
    
    encoded = [None] * num
    
    cds.cbData = MBIPC_SIZEOFINT * (num + 2) + byte_count_1
    
    for i in range(num):
        encoded[i] = strings[i].encode("UTF-16-LE")
        cds.cbData += len(encoded[i])
    
    data = struct.pack("i", byte_count_1) + encoded_1 + struct.pack("i", num)
    for e in encoded:
        data += struct.pack("i", len(e)) + e

    cds.lpData = cast(c_char_p(data), c_void_p)
    
    return cds

def pack_sssa(string_1, string_2, strings):
    """
    -Int32:  Byte count of string
    -byte[]: String data
    -Int32:  Byte count of string
    -byte[]: String data
    -Int32:  Number of strings in string array
    -Int32:  Byte count of string in string array
    -byte[]: String data in string array
    -Int32:  Byte count of string in string array
    -byte[]: String data in string array
    -...
    """
    
    cds = COPYDATASTRUCT()
    cds.dwData = 0
    
    encoded_1 = string_1.encode("UTF-16-LE")
    byte_count_1 = len(encoded_1)
    
    encoded_2 = string_2.encode("UTF-16-LE")
    byte_count_2 = len(encoded_2)
    
    num = len(strings)
    
    encoded = [None] * num
    
    cds.cbData = MBIPC_SIZEOFINT * (num + 3) + byte_count_1 + byte_count_2
    
    for i in range(num):
        encoded[i] = strings[i].encode("UTF-16-LE")
        cds.cbData += len(encoded[i])
    
    data = struct.pack("i", byte_count_1) + encoded_1 + \
           struct.pack("i", byte_count_2) + encoded_2 + struct.pack("i", num)
    for e in encoded:
        data += struct.pack("i", len(e)) + e
        
    cds.lpData = cast(c_char_p(data), c_void_p)
    
    return cds

def pack_sis(string_1, int32_1, string_2):
    """
    -Int32:  Byte count of string
    -byte[]: String data
    -Int32:  32 bit integer
    -Int32:  Byte count of string
    -byte[]: String data
    """
    
    cds = COPYDATASTRUCT()
    cds.dwData = 0
    
    encoded_1 = string_1.encode("UTF-16-LE")
    byte_count_1 = len(encoded_1)
    
    encoded_2 = string_2.encode("UTF-16-LE")
    byte_count_2 = len(encoded_2)
    
    cds.cbData = MBIPC_SIZEOFINT * 3 + byte_count_1 + byte_count_2
    
    data = struct.pack("i", byte_count_1) + encoded_1 + \
           struct.pack("ii", int32_1, byte_count_2) + encoded_2

    cds.lpData = cast(c_char_p(data), c_void_p)
    
    return cds

def pack_iai(int32s, int32_1):
    """
    -Int32: Number of integers in integer array
    -Int32: 32 bit integer
    -Int32: 32 bit integer
    -...
    -Int32: 32 bit integer
    """
    
    cds = COPYDATASTRUCT()
    cds.dwData = 0
    
    num = len(int32s)
    
    cds.cbData = MBIPC_SIZEOFINT * (num + 2)
    
    cds.lpData = cast(c_char_p(struct.pack(str(num + 2) + "i", num, *(int32s + [int32_1]))), c_void_p)
    
    return cds

def pack_siai(string_1, int32s, int32_1):
    """
    -Int32:  Byte count of string
    -byte[]: String data
    -Int32:  Number of integers in integer array
    -Int32:  32 bit integer
    -Int32:  32 bit integer
    -...
    -Int32:  32 bit integer
    """
    
    cds = COPYDATASTRUCT()
    cds.dwData = 0

    encoded = string_1.encode("UTF-16-LE")
    byte_count = len(encoded)
    
    num = len(int32s)
    
    cds.cbData = MBIPC_SIZEOFINT * (num + 3) + byte_count
    
    cds.lpData = cast(c_char_p(
                          struct.pack("i", byte_count) + encoded +
                          struct.pack(str(num + 2) + "i", num, *(int32s + [int32_1]))
                      ),
                      c_void_p)
    
    return cds
