colours={"apple":"red",
         "mango":"Yellow",
         }
print(colours["apple"])
colours["pear"]= "green"
print(colours)

empty={}


#wipe an existing dictionary:
# colours={}
# print(colours)

colours["pear"]="brown"           #update
print(colours)

#loop through a dictionary
for fruit in colours:
    print(fruit)
    print(colours[fruit])

travel_log= {
    "France": ["Paris","Lille","Dijon"],
    "India": {"num_times_visited": "4",
              "cities_visited": ["Hp","Up","uk"]
              }
}
print(travel_log["France"][1])

nested_list = ["a","b",["c","d"]]
print(nested_list[2][1])

print(travel_log["India"]["cities_visited"][1] )