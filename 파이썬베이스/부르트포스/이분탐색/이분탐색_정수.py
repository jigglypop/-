import math

x, y, c = 30, 40, 10
left, right = 0, min(x, y)
while abs(right-left) > 1e-6:
    mid = (left + right) / 2.0
    d = mid
    h1 = math.sqrt(x*x-d*d)
    h2 = math.sqrt(y*y-d*d)
    h = (h1*h2)/(h1+h2)
    if h > c:
        left = mid
    else:
        right = mid
print("%.3f" % round(mid, 3))
