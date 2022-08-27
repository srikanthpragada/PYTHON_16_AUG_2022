# char frequency

st = "A word of advice"
for c in sorted(set(st)):
    print(c, st.count(c))
