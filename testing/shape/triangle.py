
def triangleType (a, b, c) :
    if a+b>=c and b+c>=a and c+a>=b:
        if a == b == c:
            return ("Equilateral Triangle")
        elif a == b or b == c or c == a:
            return ("Isosceles Triangle")
        else:
            return ("Scalene Triangle")
    else:
        return "Invalid Triangle"
