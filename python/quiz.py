
f = open("man.txt", 'r')
yeterday_iyric = f.readlines()
f.close()

contents =""
for line in yeterday_iyric:
    contents = contents + line.strip() + "\n"


n_of_mission = contents.upper().count("MISSION")
print("mission'" , n_of_mission)
n_of_man = contents.upper().count("MAN")
print("man'" , n_of_man)
n_of_won = contents.upper().count("WON")
print("won'" , n_of_won)



