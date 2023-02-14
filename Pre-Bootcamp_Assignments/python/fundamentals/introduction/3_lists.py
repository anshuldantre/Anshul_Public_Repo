# Lists are comparable to arrays in Javascripts
# indexed at 0 # built in methods # defined with square brackets # can store any data we want inside # Length can change, mutuable

list_of_char = ['Hi', 'My', 'Name', 'is', 'Anshul', 'Dantre']
print(list_of_char)
list_of_int = [1,2,3,4,5,6]
print(list_of_int)
empty_list = []
print(empty_list)
mixed_list = ["Anshul", "dantre", 39, 1]
print(mixed_list)

list_within_a_list = [123,456,[234,'ABC',456,'567'],789]
print(list_within_a_list)

# --------------------------------------------------------------------------------------------------------------------------------------
# Combining lists or multiplying lists by a number
print(list_of_char + list_of_int + empty_list + mixed_list + list_within_a_list)
print(list_of_int * 3)

# --------------------------------------------------------------------------------------------------------------------------------------
# Assigning & printing values
drawers = ["documents", "envelopes", "pens"]
print(drawers[0])
print(drawers[1])
print(drawers[2])

drawers[0] = "tchotchkes"
print(drawers)

top_contents = drawers[0]
print(top_contents)

drawers[0]= drawers[1]
print(drawers)
print(len(list_of_char))

drawers = ["documents", "envelopes", "pens"]
for i in drawers:
    print(i)
for x in range(0,len(drawers)-1):
    print(drawers[x])

# --------------------------------------------------------------------------------------------------------------------------------------
# Appending values to a list
drawers = ["documents", "envelopes", "pens"]
# drawers[3] = "pencils" Does not work this way
drawers.append('pencils')
print(drawers)
drawers.insert(0,'erasers')
print(drawers)
new_list = ["New Item"]
new_list.extend(drawers)
print(new_list)

# removing values from a list
new_list.pop(2)
print(new_list)
new_list.pop()
print(new_list)

# --------------------------------------------------------------------------------------------------------------------------------------
# slicing a list
words = ["start","going","till","the","end"]
print(words[1:])    # ['going', 'till', 'the', 'end']
print(words[:3])    # ['start', 'going', 'till']
print(words[:])     # ['start', 'going', 'till', 'the', 'end']
print(words[2:4])   # ['till', 'the']

# --------------------------------------------------------------------------------------------------------------------------------------
# Built in functions for a list (Common across all sequences)
words = ["start","going","till","the","end"]
print(len(words))
numbers = [11,2,3,343,5656,23232,4454,232]
print(max(numbers))
print(min(numbers))
print(sorted(numbers))
print(sorted(words))

# --------------------------------------------------------------------------------------------------------------------------------------
# Built in functions for a list (Specific to list)
words = ["start","going","till","the","end"]
numbers = [11,2,3,343,5656,23232,4454,232]
print(words.index('till'))
numbers.reverse() # returns a None value print(numbers.reverse())
words.reverse()   # returns a None value print(words.reverse())
print(numbers)
print(words)