import urllib.request

blue = 'http://192.168.2.101/?r7g0b255&'
red = 'http://192.168.2.101/?r255g2b29&'
green = 'http://192.168.2.101/?r20g97b0&'
purple = 'http://192.168.2.101/?r142g38b169&'

a = ()

payload = urllib.request.urlopen(a)

print(payload.status)
print(payload.url)
