""" strs = ["dog","racecar","car"]

prefix = strs[0]

for s in strs[1:]:
    while not s.startswith(prefix):
        prefix = prefix[:-1]
        if prefix == "":
            break

print(f"Common prefix is: {prefix}") """