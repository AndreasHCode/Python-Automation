#Collatz: even == n/2, uneven n*3 + 1

def collatz(entry, step):
    print("Current number: " + str(entry))
    if entry < 1:
        print("Number must be at least 1")
        return None
    if entry == 1:
        print("Reached One after " + str(step) + " steps.")
    elif (entry % 2) == 0:
        collatz(int(entry / 2), step + 1)
    else:
        collatz(entry * 3 + 1, step + 1)
    
print("Enter a Number for Sequence")
try:
    entry = int(input())
    collatz(entry, 1)
except ValueError:
    print("Not a number")
print("Ending Program")
