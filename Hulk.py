Hulk={
"Real Name":"Robert Bruce Banner",
"Creators":"Stan Lee & Jack Kirby",
"Powers":["Superhuman Strength, Superhuman Durability, Superhuman Stamina, Superhuman Speed, Accelerated Healing Factor"],
"Paraphernalia":"None",
"Personality":["Angry, hot-tempered, powerful, strong, tough, loud, comical, brave, good-hearted"]
}
# print(Hulk)

Hulk["fav-food"] = "Taco"
print(Hulk.keys())
choice = input("Choose your key: ")
print(Hulk[choice])

# Deadpool={'Real Name':'Wade Winston Wilson',
# 'Alias':'Deadpool',
# 'First Appearance':'New Mutants (Vol. 1) #98 (February, 1991)',
# 'Creators':['Fabian Nicieza',' Rob Liefeld'],
# 'Base of Operations':'Nomadic'}

# print(Deadpool["Real Name"])

# print(f"Deadpool aka {Deadpool['Real Name']}, aka {Deadpool['Alias'] }, was created by {Deadpool['Creators']}, he made his first apperence in {Deadpool['First Appearance']}, His base of operation is {Deadpool['Base of Operations']}")