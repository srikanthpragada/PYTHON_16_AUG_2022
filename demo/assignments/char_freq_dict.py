# program to accept a string and create a dictionary that contains
# character and its count

st = "How are you"
chars = {c: st.count(c) for c in sorted(set(st))}
print(chars)