# accept a collection of names and display all common characters in a string

colours = ['red', 'blue', 'green', 'yellow']
chars = set(colours[0])  # Empty set

for n in colours[1:]:
    chars = chars & set(n)
    print(chars)

print(f"Unique characters : {sorted(chars)}")