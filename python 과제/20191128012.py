# 2019112801
# 2 tongue twister 문장 분석

message = "Peter Piper picked a peck of pickled peppers. A peck of pickled peppers Peter Piper picked."
print("Original String:",  message)
msg_list_comma = message.split('.')
msg_list = []
for i in msg_list_comma:
    msg_list += i.split()
msg_list = sorted(msg_list)
print("Split String:", msg_list)
print()

print("<<< Convert List to Dictionary >>>")
msg_list_copy = list(msg_list)
msg_dict = {}
for i in range(len(msg_list_copy)):
    number = 0
    for j in range(i, len(msg_list_copy)):
        if msg_list_copy[i] == msg_list_copy[j]:
            number +=1
            if i != j:
                msg_list_copy[j] = " "
    if msg_list_copy[i] != " ":
        msg_dict[msg_list_copy[i]] = number
print("List to Dict:", msg_dict)
print("단어 반복 회수 분석:")
for i in msg_dict:
    print("{0}: {1}".format(i, msg_dict.get(i)))
print()

print("<<< Convert List -> Set -> Dictionary >>>")
msg_set = set(msg_list)
print("List to Set:", msg_set)
msg_set_dict = {}
for x in msg_set:
    msg_set_dict[x] = 1
print("Set to Dict:", msg_set_dict)
