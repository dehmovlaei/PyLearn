s1 = input("please Enter One By One 3 Side To Cheack Validity Of Triangle\n")
s2 = input()
s3 = input()
if ((s1 + s2) < s3) and ((s1+s3) < s2) and ((s2+s3) < s1):
    print("this Is Valid Triangle")
else:
    print("NOT VALID")