def is_leap_year(year):
    a=year%4
    b=year%100
    c=year%400

    if a==0 and b!=0 and c==0:
        return True
    elif a==0 and b==0 and c == 0:
        return True
    elif a==0 and b!=0 and c!=0:
        return True
    else:
        return False

print(is_leap_year(int(input("Enter a year to check if it's a leap year: "))))