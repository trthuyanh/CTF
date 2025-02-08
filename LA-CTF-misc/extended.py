with open("chall.txt", "rb") as f:
	data = f.read()
print(data)
de_data = data.decode("iso8859-1")
print(de_data)
flag = ""
for c in de_data:
    # Chuyển ký tự về dạng nhị phân
    o = bin(ord(c))[2:].zfill(8)
    
    # Đổi bit `1` đầu tiên thành `0`
    for i in range(8):
        if o[i] == "1":
            o = o[:i] + "0" + o[i + 1:]
            break

    # Chuyển nhị phân về ký tự ASCII
    flag += chr(int(o, 2))
print(flag)
