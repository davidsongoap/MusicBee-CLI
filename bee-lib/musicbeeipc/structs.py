#----------------------------------------------------------#
#- MusicBeeIPCSDK Py v2.0.0                               -#
#- Copyright © Kerli Low 2014                             -#
#- This file is licensed under the                        -#
#- BSD 2-Clause License                                   -#
#- See LICENSE_MusicBeeIPCSDK for more information.       -#
#----------------------------------------------------------#

from ctypes import *


class FloatInt(Union):
    _fields_ = [("f", c_float),
                ("i", c_int)]
                
                
class LRUShort(Union):
    class LowHigh(Structure):
        _fields_ = [("low", c_ushort),
                    ("high", c_ushort)]
                    
    _fields_ = [("lr", c_void_p),
                ("s", LowHigh)]
                
                
class COPYDATASTRUCT(Structure):
    _fields_ = [("dwData", c_void_p),
                ("cbData", c_uint),
                ("lpData", c_void_p)]
