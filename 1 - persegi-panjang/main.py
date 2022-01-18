from Rectangle import Rectangle


def main(args=None):
    length = int(input("Input Panjang: "))
    width = int(input("Input Lebar: "))
    rect = Rectangle(width, length)

    print(f"Keliling: {rect.calculate_perimeter()}")
    print(f"Luas: {rect.calculate_area()}")


if __name__ == '__main__':
    main()
