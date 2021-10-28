def spam():
    eggs = "Local spam"
    print(eggs)

def bacon():
    eggs = "Local Bacon"
    print(eggs)
    spam()
    print(eggs)

eggs = "Global"
bacon()
print(eggs)
