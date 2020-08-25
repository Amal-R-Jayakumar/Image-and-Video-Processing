s1=input().lower()
s3=[i for i in list('aeiou'.strip()) if s1.find(i)==-1]
print("Accepted\nAll vowels are present") if len(s3)==0 else print(f"Not Accepted \n\'{','.join(s3)}\' are not present")  