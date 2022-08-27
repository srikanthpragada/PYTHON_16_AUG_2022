# accept a collection of names and display all unique characters in a string

colours = ['red', 'blue', 'green', 'yellow']
chars = set()  # Empty set

for n in colours:
    chars = chars | set(n)

print(f"Unique characters : {sorted(chars)}")