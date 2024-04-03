f = open("C:\workspace\man.txt",'r')
yeterday_iyric = f.readlines()
f.close()
print("dd")

contents =""
for line in yeterday_iyric:
    contents = contents + line.strip() + "\n"

n_of_yesterday = contents.upper().count("mission")
print("Number of word 'yesterday'" , n_of_yesterday)