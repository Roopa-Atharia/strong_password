import string
import random
if __name__=="__main__":
    a1=string.ascii_lowercase
    a2=string.ascii_uppercase
    a3=string.digits
    a4=string.punctuation
    plen=int(input("enter password lenght\n"))
    a=[]
    a.extend(list(a1))
    a.extend(list(a2))
    a.extend(list(a3))
    a.extend(list(a4))
    random.shuffle(a)
    print("".join(a[0:plen]))