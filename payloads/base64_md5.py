import hashlib, base64

with open("note.txt", "r") as file:
    payloadpw = file.read()
listpw = payloadpw.split('\n')
payload = []

for i in listpw:
    payload.append(hashlib.md5(str(i).encode("utf-8")).hexdigest())

with open("base64_md5.txt", "w") as file:
    for item in payload:
        addstr="carlos:" + item
        strtobyte = addstr.encode("ascii")
        base64_bytes = base64.b64encode(strtobyte)
        base64_string = base64_bytes.decode("ascii")
        print(base64_string)
        file.write("\n" + base64_string)
