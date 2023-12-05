x=int(input("enter number of year"))
total=0
i=0
y=x*12
while(i<=y):
    a=int(input("the average high temperature for each month"))
    total=total+a
    i=i+1

average_yearly=total/x
average_monthly=total/y

print("average yearly high temperature:",average_yearly)
print("average monthly high temperature:",average_monthly)

   
    