import json

students = {
    1: "Julia",
    2: 12,
    3: "Form 1"
}

print(students[3])

# print(school["user_id2"]["Profession"])


# print(school["user_id1"].values())


#for key, value in school.items():
#    for x, y in value.items():
#        print(f"{x} and value {y}")
    # print(f"{key} and value {value}")

school = {}
for i in range(4):
    name = input("Your name: ")
    prof = input("Your profession: ")
    exp = input("Years of Experience: ")
    more_details = {
                    "hello": "world",
                    "Anime": "Dr Stone"
                }

    school[f"user_id{i}"] = {
            "Name": name,
            "Profession": prof,
            "years_of_exp": int(exp),
            "more_details": more_details
        }


print(school)

with open("database.json", "w") as file:
    json.dump(school, file, indent=4)
    file.close()

    
for key, value in school.items():
    print(f"Key: {key}\n")
    for x, y in value.items():
        print(f"Outer Key: {key}\n => Inner Key {x} = Outer Value {y}")









    
