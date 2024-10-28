cities = ["delhi", "gurgaon", "noida", "mumbai"]
heroes = ["thor", "ironman", "captain america"]

def print_list_length(lst):
    print(len(lst))

print_list_length(cities)
print_list_length(heroes)

def print_list(list):
    for item in list:
        print(item,end=" ")
        
print_list(heroes)