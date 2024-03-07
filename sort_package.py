def sort_package(width, height, length, mass):
    volume = width * height * length
    is_bulky = volume >= 1000000 or width >= 150 or height >= 150 or length >= 150
    is_heavy = mass >= 20

    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"

if __name__ == "__main__":
    print(sort_package(90, 90, 90, 10))  # STANDARD
    print(sort_package(200, 200, 200, 10))  # SPECIAL
    print(sort_package(200, 200, 200, 30))  # REJECTED
