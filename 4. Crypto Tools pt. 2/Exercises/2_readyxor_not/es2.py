import base64

data="El Psy Congroo"
b64_data="IFhiPhZNYi0KWiUcCls="
b64_flag="I3gDKVh1Lh4EVyMDBFo="

def base64tostring(m):
    return base64.b64decode(m).decode('utf-8',errors='ignore')

string_data=base64tostring(b64_data)
string_flag=base64tostring(b64_flag)

print(len(data),len(string_data))

def string_xor(string1,string2):
    return ''.join([chr(ord(x) ^ ord(y)) for x, y in zip(string1, string2)])

key=string_xor(string_data,data)

print(key)

flag=string_xor(key,string_flag)

print(flag)