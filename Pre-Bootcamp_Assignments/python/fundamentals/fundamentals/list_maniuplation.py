drawers = ['documents', 'envelopes', 'pens']
print(drawers[0])
print(drawers[1])
print(drawers[2])

drawers[0] = 'tchotchkes'
print(drawers)

temp_var = drawers[0]
print(temp_var)

drawers[1] = drawers[0]
print(drawers)


nums = [1,2,3,4,5]
nums.append(99)
print(nums)

words = ['start','going','till','the','end']
print(words[1:])
print(words[:4])
print(words[2:4])

copy_of_words = words[:]
copy_of_words.append("DoJo")
print(copy_of_words)
print(words)