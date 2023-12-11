from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)

        if not str(value).isdigit() or len(str(value)) != 10:
            raise ValueError("Invalid phone number format 10 digits.")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        self.remove_phone(old_phone)
        self.add_phone(new_phone)

    def find_phone(self, phone):
        return next((p for p in self.phones if p.value == phone), None)

    def __str__(self):
        return f"Contact name: {self.name}, phones: {', '.join(str(p) for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def __str__(self):
        return '\n'.join(str(record) for record in self.data.values())



if __name__ == "__main__":
    record1 = Record("John Doe")
    record1.add_phone("1234567890")
    record1.add_phone("9876543210")

    record2 = Record("Jane Doe")
    record2.add_phone("5551112233")

    address_book = AddressBook()
    address_book.add_record(record1)
    address_book.add_record(record2)

    print("Book:")
    print(address_book)

    result = address_book.find("John Doe")
    print("\nSearch Result:", result)

    address_book.delete("Jane Doe")
    print("\nAddress Book after Deletion:")
    print(address_book)

    record1.edit_phone("1234567890", "9990001111")
    print("\nAddress Book after Editing Phone Number:")
    print(address_book)
