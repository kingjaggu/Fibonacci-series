print("FIBBONACCI SERIES")
input("enter the range at which series are required",range)
first=0; 
second=1;
next=1:
print(first," ", second)
while(next<range)
   next=first+second
   print(next," ")
   first=second;
   second=next;
