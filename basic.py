# lists store sequences 
print("\n\n********************list in python **************** \n \n  ")
li =[]
print("empty list",li)
li.append(1)
li.append(2)
li.append(4)
li.append(3)
print("after appending/added item --",li)
# Remove from the end with pop
li.pop()
print("after pop/deleted last item --",li)
print(f"Access a list like you would any array {li[0]},last element:{li[-1]} \n")
print(f" Return list from index (The start index is included, the end index is not) :{li[0:2]}")

print("""list Methods
      Remove arbitrary elements from a list with "del"
      Remove first occurrence of a value  (remove) 
      Insert an element at a specific index (insert)
      Get the index of the first item found matching the argument (index)
      Examine the length with "len()"
      Check for existence in a list with "in"
      """)

print("\n*******************list --end*********************** \n\n\n")
#> Primitive dataTypes and operators
print(3)
print(1+1)
print(8-1)
print(10*2)
print(35/7)

# floor division rounds towards negative infinity
print(5//3) #=>1
print(-5//3) #=>-2
print(5.0//3.0) #=> 1.0 # work on floats too 
print (-5.0//3.0) #-> -2.0


# modules operation
print(7%3) #=>1
print(-7%3) # -> 2

print("I'm python, Nice to meet you")


# Single line comments start with a number symbol 

""" 
   Multiline strings can be written 
   using three "s, and are often used 
   as documentation.
"""

