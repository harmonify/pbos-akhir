import json


class Mahasiswa:
    def __init__(self, name, address, nim) -> None:
        self.name = name
        self.address = address
        self.nim = nim

    def __str__(self) -> str:
        return f"Nama: {self.name}, Alamat: {self.address}, NIM: {self.nim}"

    def save(self) -> None:
        data = {
            "name": self.name,
            "address": self.address,
            "nim": self.nim
        }
        with open("mahasiswa.json", "w") as file:
            json.dump(data, file)
        print("Data berhasil disimpan")
