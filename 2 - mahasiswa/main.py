from Mahasiswa import Mahasiswa


def main(args=None) -> None:
    name = input("Nama: ")
    address = input("Alamat: ")
    nim = input("NIM: ")
    mhs = Mahasiswa(name, address, nim)
    print()
    print(mhs)
    print()
    if input("Simpan data mahasiswa? (y/n)\n") == "y":
        mhs.save()


if __name__ == '__main__':
    main()
