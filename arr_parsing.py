obj = [{"Name":"Sachin","Age":20,"Place":"Kolar"},{"Name":"Virat","Age":34,"Place":"Delhi"},{"Name":"Anil","Age":23,"Place":"Bangalore"}]


complexArray =[{"Name":"Sachin","Age":20,"Place":"Kolar","Skills":["Batting","Bowling"]},{"Name":"Virat","Age":34,"Place":"Delhi","Skills":["Bowling","WicketKeeping"]},{"Name":"Anil","Age":23,"Place":"Bangalore","Skills":["Umpiring","Batting"]}]


for item  in complexArray:
    if "Bowling" in item["Skills"] :
        print(item["Name"])
            

for item  in obj:
    if item["Age"] > 30 :
        print("Name will be :" ,item["Name"])
    