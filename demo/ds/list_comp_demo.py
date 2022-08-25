
s = "Hello"

codes = []
for c in s:
    codes.append(ord(c))

print(codes)

# List Comprehension
codes = [ord(c) for c in s]
print(codes)

codes = [ord(c) for c in s if c.islower()]
print(codes)