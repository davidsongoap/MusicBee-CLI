#----------------------------------------------------------#
#- MusicBeeIPCSDK Py v2.0.0                               -#
#- Copyright © Kerli Low 2014                             -#
#- This file is licensed under the                        -#
#- BSD 2-Clause License                                   -#
#- See LICENSE_MusicBeeIPCSDK for more information.       -#
#----------------------------------------------------------#

import mmap
import struct
from . constants import *
from . structs import *
    

def open_mmf(lr):
    if not lr:
        return None
        
    ls = LRUShort(lr)
    
    mmf = mmap.mmap(-1, ls.s.high + MBIPC_SIZEOFLONG, "mbipc_mmf_" + str(ls.s.low), mmap.ACCESS_READ)
    try:
        mmf.seek(ls.s.high)
        capacity = struct.unpack("q", mmf.read(MBIPC_SIZEOFLONG))[0]
    finally:
        mmf.close()
    
    if capacity <= 0:
        return None
    
    mmf = mmap.mmap(-1, ls.s.high + MBIPC_SIZEOFLONG + capacity, "mbipc_mmf_" + str(ls.s.low), mmap.ACCESS_READ)
    mmf.seek(ls.s.high + MBIPC_SIZEOFLONG)
    
    return mmf


# --------------------------------------------------------------------------------
# All strings are encoded in UTF-16 little endian
# --------------------------------------------------------------------------------

def unpack_s(lr):
    """
    -Int32:  Byte count of the string
    -byte[]: String data
    Free lr after use
    
    rtype: str
    """
    
    string_1 = ""

    try:
        mmf = open_mmf(lr)
        if not mmf:
            raise Exception("Failed to open MMF.")
    except:
        return ""
        
    try:
        byte_count = struct.unpack("i", mmf.read(MBIPC_SIZEOFINT))[0]
        
        if byte_count > 0:
            string_1 = mmf.read(byte_count).decode("UTF-16-LE")
    except:
        return ""
    finally:
        mmf.close()
    
    return string_1
    
def unpack_sa(lr):
    """
    -Int32:  Number of strings
    -Int32:  Byte count of 1st string
    -byte[]: 1st string data
    -Int32:  Byte count of 2nd string
    -byte[]: 2nd string data
    -...
    Free lr after use
    
    rtype: list of str
    """
    
    try:
        mmf = open_mmf(lr)
        if not mmf:
            raise Exception("Failed to open MMF.")
    except:
        return []
        
    try:
        str_count = struct.unpack("i", mmf.read(MBIPC_SIZEOFINT))[0]
        
        strings = [None] * str_count
        
        for i in range(str_count):
            byte_count = struct.unpack("i", mmf.read(MBIPC_SIZEOFINT))[0]
            
            if byte_count > 0:
                strings[i] = mmf.read(byte_count).decode("UTF-16-LE")
    except:
        return []
    finally:
        mmf.close()
    
    return strings
    
def unpack_ii(lr):
    """
    -Int32: 1st 32 bit integer
    -Int32: 2nd 32 bit integer
    Free lr after use
    
    rtype: list of 2 int
    """
    
    try:
        mmf = open_mmf(lr)
        if not mmf:
            raise Exception("Failed to open MMF.")
    except:
        return [-1, -1]
        
    try:
        ints = struct.unpack("ii", mmf.read(MBIPC_SIZEOFINT * 2))
    except:
        return [-1, -1]
    finally:
        mmf.close()
    
    return ints
    
def unpack_ia(lr):
    """
    -Int32: Number of integers
    -Int32: 1st 32 bit integer
    -Int32: 2nd 32 bit integer
    -...
    Free lr after use
    
    rtype: list of int
    """
    
    try:
        mmf = open_mmf(lr)
        if not mmf:
            raise Exception("Failed to open MMF.")
    except:
        return []
        
    try:
        int_count = struct.unpack("i", mmf.read(MBIPC_SIZEOFINT))[0]
        
        ints = struct.unpack(str(int_count) + "i", mmf.read(MBIPC_SIZEOFINT * int_count))
    except:
        return []
    finally:
        mmf.close()
    
    return ints
