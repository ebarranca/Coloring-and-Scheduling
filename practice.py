"""
some activities for olivia to practice loops, conditionals, lists, strings 
I highly encourage you to add print statements when you run your code 
I'm a big fan of print debugging to figure out what's going on 

There are two demos with some background/info dump 
Then there are some activities to try 

Can add TODO comments with any questions you have 
Feel free to google, but make sure you can explain what the code is doing 
"""
from random import *

def main():
    ############################################################################################
    ############################################################################################
    ## review of strings and string formatting
    # a string is a sequence of characters
    s1 = "Harry" 
    s2 = "1D"
    s3 = "olivia styles"
    s4 = "Olivia Styles"

    #we can test if strings are equal, add strings, remove characters, etc
    print(s3 == s4)
    print(s3.upper() == s4.upper())
    s5 = s1 + s2
    s6 = s1 + " loves " + s4
    print(s5, s6)

    #there's some stuff we can do with string formatting to build a big string without all the +'s 
    # \n means newline 
    # %d means to expect an int, %f means to expect a float, %s means to expect a string 
    # %s is a placeholder. it means inster the corresponding variable into the string 
    a = 18
    b = 4 
    c = "is a one direction"
    d = "song"
    e = "album"

    print("%d %s %s \n%d %s %s" %(a,c,d,b,c,e))
    print("%d is not on the %s %d" % (a,e,b))

    # Note: the following line throws an error 
    # new_string = a + c + d

    #but it would work if we first force a to be a string not an int
    new_string = str(a) + c + d
    print(new_string) #note the spacing on the print 

    #TODO you should play around with strings a bit! 
    #you can do that here or run a python shell in your terminal 
    #(just type in python3 and then you can run python commands)

    ############################################################################################
    ############################################################################################

    ##review of conditional: if, elif, else
    # if statements are boolean, so if (condition) == True, will execute the code block 
    #elif is short for else if so hyou can specify another (as many as you want) 
    #BUT the first conditional to run will then jump to the end of the code block 
    ## uncomment each of the values of x, run the code, and see what happens
    x = 13
    # x = 2
    # x = 5 

    if x > 5:
        print("%d is greater than 5" %x)
    elif x < 5:
        print("%d is less than 5" %x)
    elif 3 <= 5:
        print("poop")
    else: 
        print("%d is equal to 5" %x)

    ############################################################################################
    ############################################################################################

    #using a for loop, build a list of n random numbers using python's random function 
    #first set n so that your loop depends on the variable and isn't hard coded for a specific n
    #n = 

    #then create a new list that is all of the elements from your above list that are multiples of 3
    
    #print the number of multiples of 3 and the number of non multiples of 3 from the original n

    #change the original list so that there are no multiples of 3


    ############################################################################################
    ############################################################################################

    #create a string of n random vowels then m random consonants 
    #your string cannot have double letters (every letter must be distinct from adjacent letters)
    #n= 
    #m=

    #then split the string you made into "vowel consonant space"
    #for whichever of m or n is smaller, loop through the letters again 
    #example: n = 4 m=11 string could be: "aoiurmspgwkrnlq"
    #then would want "ar om is up ag ow ik ur an ol iq"

    ############################################################################################
    ############################################################################################

    #pick a graph -- MAYBE start with a complete graph or a complete bipartite graph 
    #create a list (or set) of vertices in the graph
    #build a set of pairs to represent the edges of a graph 
    # I want you to start thinking about how you might represent this data 

    ## think about: 
    ## --> should edges be ordered pairs? 
    ## --> should vertices and edges be two different data structures? 
    ## --> with the data structures you've chosen, can we check if two graphs are equal? 
    ## --> what questions do you have? 


   #using a for loop, build a list of n random numbers using python's random function 
    #first set n so that your loop depends on the variable and isn't hard coded for a specific n
    #n = 

    #then create a new list that is all of the elements from your above list that are multiples of 3
    
    #print the number of multiples of 3 and the number of non multiples of 3 from the original n

    #change the original list so that there are no multiples of 3

import random
n=20
og_list=[] ##creating a new list
for i in range(n):
     og_list.append(random.randint(1, 100)) ##adding random numbers between 1 and 100 to the back of the list using append
print(f"Original list: {og_list}") ##prints out the list that we have created 

mult_of_3=[] ##new list again
for num in og_list: ##specifying that we want to use the numbers from the previous list
    if num % 3 == 0: ##if the number has a remainder of 0 when divided by 3 then it is a multiple of 3
        mult_of_3.append(num) ## if it is a multiple of 3, add to the back of new list
print(f"multiples of 3: {mult_of_3}") ##print new list

num_mult_of_3 = len(mult_of_3) ##this is telling us that the number of multiples of 3 is the length of the previous list
num_non_mult_of_3 = n-num_mult_of_3 # this is saying that the number of non multiples of 3 is the total number of elements in the list minus the list of multiples of 3
print(f"Number of multiples of 3: {num_mult_of_3}") #print the number of multiples of 3
print(f"Number of non multiples: {num_non_mult_of_3}") #print the number of non multiples of 3


    #create a string of n random vowels then m random consonants 
    #your string cannot have double letters (every letter must be distinct from adjacent letters)
    #n= 
    #m=

    #then split the string you made into "vowel consonant space"
    #for whichever of m or n is smaller, loop through the letters again 
    #example: n = 4 m=11 string could be: "aoiurmspgwkrnlq"
    #then would want "ar om is up ag ow ik ur an ol iq"



 #pick a graph -- MAYBE start with a complete graph or a complete bipartite graph 
    #create a list (or set) of vertices in the graph
    #build a set of pairs to represent the edges of a graph 
    # I want you to start thinking about how you might represent this data 

    ## think about: 
    ## --> should edges be ordered pairs? 
    ## --> should vertices and edges be two different data structures? 
    ## --> with the data structures you've chosen, can we check if two graphs are equal? 
    ## --> what questions do you have? 



#V={0,1,2,3}
#E=[{0,1}, {0,2}, {1,2}, {1,3}]
#E.append({0,3})
#G=(V,E)
#E.append({0,3})
#len(E)
#print(f"{G}")
#print(f"{len(E)}")

V={0,1,2,3,4}
E=[{0,1}, {0,2}, {1,2}, {1,3}, {0,3},{2,3},{0,4}, {1,4}, {2,4}, {3,4}]
G=(V,E)

x=0
for i in V:
    for j in V:
        if i<j:
            if {i,j} not in E:
                x+=1
                #print(f"Not complete")
if x==0:
    print(f"complete")               
else:
    print(f"not complete")
main()