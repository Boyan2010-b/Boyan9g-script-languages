import math

def area(a, b, gamma_deg):
    gamma_rad = math.radians(gamma_deg)
    c_squared = a**2 + b**2 - 2 * a * b * math.cos(gamma_rad)
    c = math.sqrt(c_squared)
    triangle_area = 0.5 * a * b * math.sin(gamma_rad)
    perimeter = a + b + c

    return triangle_area, perimeter

if __name__ == "__main__":
    try:
        a = float(input("int lenght of a: "))
        b = float(input("int lenght of b: "))
        gamma = float(input("int angle of c: "))

        if a <= 0 or b <= 0 or gamma <= 0 or gamma >= 180:
            print("not valid")
        else:
            face, peri = area(a, b, gamma)
            print(f"S triangle: {face:.2f}")
            print(f"Peremeter triangle: {peri:.2f}")

    except ValueError:
        print("Please enter a numeric value for the side and angle lengths")

