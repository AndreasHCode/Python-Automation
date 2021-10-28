import pprint

message = "This ia message with a lot of characters"
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] += 1

print(count.keys())
print(count.values())
pprint.pprint(count)
