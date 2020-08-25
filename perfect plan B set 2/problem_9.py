n=['perfect',"plan","b","e-learning",'Platform']
if 'perfect' in n:
    print("found")
for i in n:
    if i=="perfect":
        print("found")
try:
    n.index("notjh")
    print("found")
except Exception:
    pass