def computepay(h, r):
    print("In computepay")
    if h>40:
        pay = 40 * r + (h - 40) * 1.5 * r
    else:
        pay = h * r
    return pay


hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
pay = computepay(h,r)

print(pay)
