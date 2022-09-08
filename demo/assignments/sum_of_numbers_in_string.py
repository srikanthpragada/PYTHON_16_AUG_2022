st = "90,44,50,34,89,abc,98"

# total = 0
# for v in st.split(","):
#     total += int(v)
#
# print(total)

print('Total = ', sum(map(int, st.split(","))))
