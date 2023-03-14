import base64
import sys
def url_decode(s):
    result = ""
    i = 0
    while i < len(s):
        if s[i] == "_":
            result += s[i+1].upper()
            i += 2
        else:
            result += s[i]
            i += 1
    result = result.replace("-","=")
    print(result)
    bytes_string = result.encode('utf-8')
    # 进行 base64 解码
    decoded_bytes = base64.b64decode(bytes_string)
    # 将 bytes 类型转换为字符串类型
    return decoded_bytes.decode('utf-8')

print(url_decode(sys.argv[1]))