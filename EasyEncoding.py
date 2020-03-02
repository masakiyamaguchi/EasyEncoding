#encoding:utf-8
import sys

TYPE_ERROR_MSG = "Unexpected object type {}\nExpected object type str, unicode, list, dict"
LIST_TYPE = type(list())
DICT_TYPE = type(dict())
UNICODE_TYPE = type(unicode())
STR_TYPE = type(str())

def to_str(obj, encoding=None):
    # str, unicode, list, dictオブジェクトを受け取り, strオブジェクトに変換して返す関数
    # 返り値は引数のオブジェクトを引き継ぐものとする.
    return _to_str_func(obj)(obj, encoding=encoding)

def to_unicode(obj, encoding=None):
    # str, unicode, list, dictオブジェクトを受け取り, unicodeオブジェクトに変換して返す関数
    # 返り値は引数のオブジェクトを引き継ぐものとする.
    return _to_unicode_func(obj)(obj, encoding=encoding)

def _element_to_str(obj, encoding=None):
    for i, e in enumerate(obj):
        obj[i] = _to_str_func(e)(e, encoding=encoding)
    return obj
    
def _element_to_unicode(obj, encoding=None):
    for i, e in enumerate(obj):
        obj[i] = _to_unicode_func(e)(e, encoding)
    return obj
    
def _key_value_to_str(obj, encoding=None):
    new_dict = {}
    for k, v in obj.items():
        new_key = _to_str_func(k)(k, encoding=encoding)
        new_value = _to_str_func(v)(v, encoding=encoding)
        new_dict[new_key] = new_value
    return new_dict
        
def _key_value_to_unicode(obj, encoding=None):
    new_dict = {}
    for k, v in obj.items():
        new_key = _to_unicode_func(k)(k, encoding=encoding)
        new_value = _to_unicode_func(v)(v, encoding=encoding)
        new_dict[new_key] = new_value
    return new_dict
    
def _str_to_str(obj, encoding=None):
    return obj
    
def _str_to_unicode(obj, encoding=None):
    if encoding is None:
        encoding = sys.getdefaultencoding()
    return obj.decode(encoding=encoding)
    
def _unicode_to_str(obj, encoding=None):
    if encoding is None:
        encoding = sys.getdefaultencoding()
    return obj.encode(encoding=encoding)

def _unicode_to_unicode(obj, encoding=None):
    return obj

def _to_str_func(obj):
    e_type = type(obj)
    if e_type == LIST_TYPE:
        return _element_to_str
    elif e_type == DICT_TYPE:
        return _key_value_to_str
    elif e_type == UNICODE_TYPE:
        return _unicode_to_str
    elif e_type == STR_TYPE:
        return _str_to_str
    else:
        raise TypeError(TYPE_ERROR_MSG.format(e_type))

def _to_unicode_func(obj):
    e_type = type(obj)
    if e_type == LIST_TYPE:
        return _element_to_unicode
    elif e_type == DICT_TYPE:
        return _key_value_to_unicode
    elif e_type == UNICODE_TYPE:
        return _unicode_to_unicode
    elif e_type == STR_TYPE:
        return _str_to_unicode
    else:
        raise TypeError(TYPE_ERROR_MSG.format(e_type))