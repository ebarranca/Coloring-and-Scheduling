


def main():
    H = [1,3,7]
    L = [4,6]
    Li = [1,4,6]
    Z = [1,2,5]
    N = [2,7]

    #goal: set up the graph for when pilots are free without hard coding to dummy data 
    # \come up with a data structure to store pilot's last flight --maybe a pilot is an object 

lists = {
    "H": [1,3,7],
    "L": [4,6],
    "Li": [1,4,6],
    "Z": [1,2,5],
    "N": [2,7]
}

# STEP 1: figure out the full “universe” of numbers used across all lists.
# Basically, I want one master set that contains every number that appears anywhere.
universe = set()  # empty set for now

# .values() goes through only the values listed.
for nums in lists.values():
    # .update() adds all the elements from that list into my set.
    # Since sets only keep unique items, I don’t have to worry about duplicates.
    universe.update(nums)

# STEP 2: build the complementary lists. (basically whats not in each list but in the 1-7 universe)
complements = {}  # empty list to store the new “opposite” lists

for key, nums in lists.items():  # .items() lets me loop through both the key and its list together
    # I use set(nums) to turn the list into a set so I can do set math.
    # universe - set(nums) means “everything in universe except what’s in nums.”
    complement = sorted(list(universe - set(nums)))  # sorted() just makes the output look neat
    complements[key] = complement  # save the complement under the same letter key

# Print out the new lists so I can check that they make sense
print("Complement lists (new lists):")
for k, v in complements.items():  # k = key, v = the list of numbers
    print(f"{k} = {v}")

# STEP 3: Build a “graph” which is basically a mapping that shows which labels connect to each number.
# for each number, I want to know which of the list is in this category.
graph = {}

for num in sorted(universe):  # go through each number in order
    graph[num] = []  # start with an empty list of connections
    for name, nums in complements.items():
        if num in nums:  # if this number shows up in that list...
            # make a string like “H2” or “Z6” to represent that connection
            graph[num].append(f"{name}{num}")

# Print the graph.
print("\nGraph:")
for num, edges in graph.items():
    print(f"{num} = {edges}")


E=[]
for number in graph:
    for V1 in graph[number]:
        for V2 in graph[number]:
            if V1 != V2:
                if {V1,V2} not in E:
                    E.append({V1,V2})
print(E)