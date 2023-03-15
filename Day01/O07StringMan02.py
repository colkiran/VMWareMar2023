
print("find".center(40, "-"))
# returns the index

st1 = "hello world"
st2 = "the quick brown fox jumps over the lazy dog"

print(f"st1 :{st1}")
res1 = st1.find("w")
print(f"res1 :{res1}")

res2 = st1.find("l")
print(f"res2 :{res2}")

res3 = st1.find("l", 6)
print(f"res3 :{res3}")

res4 = st1.find("l", st1.find("l", st1.find("l")+1)+1)
print(f"res4 :{res4}")

print(f"st2 :{st2}")

res1 = st2.find("fox")
print(f"res1 :{res1}")

res2 = st2.find("the")
print(f"res2 :{res2}")

res2 = st2.find("the", st2.find("the")+1)
print(f"res2 :{res2}")

print("replace".center(40, "-"))

st1 = "hello world"
print(f"st1 :{st1}")

res1 = st1.replace("h", "H")
print(f"res1 :{res1}")

res2 = st1.replace("l", "L")
print(f"res2 :{res2}")

res2 = st1.replace("l", "L", 2)
print(f"res2 :{res2}")

res2 = st1.replace("l", "L", 1)
print(f"res2 :{res2}")

st2 = "the quick brown fox jumps over the lazy dog"

res1 = st2.replace("brown fox", "white tiger")
print(f"res1 :{res1}")

res2 = st2.replace("the", "The")
print(f"res2 :{res2}")

res2 = st2.replace("the", "The", 1)
print(f"res2 :{res2}")

print("maketrans".center(40, "-"))
st = "hello world"
a = 'helowrd'
b = 'HELOWRD'
# length of a and b should be the same
print(f"st :{st}")

resTbl = st.maketrans(a, b)
print(f"resTbl :{resTbl}")

print("Translate".center(40, "-"))
res = st.translate(resTbl)
print(f"res :{res}")
