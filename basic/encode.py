import base64

r = base64.b64encode(b'fuyongde')
print(r)
s = base64.b64decode(r)
print(s)