import csv
from connect import connect_db

def insert_from_csv():
    conn = connect_db()
    cur = conn.cursor()

    with open("/Users/aidanatn/Desktop/PP2/practice 7/contacts.csv", 'r') as file:
        reader = csv.reader(file)

        for row in reader:
            name = row[0]
            phone = row[1]

            cur.execute(
                "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
                (name, phone)
            )

    conn.commit()
    cur.close()
    conn.close()

def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    conn = connect_db()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
        (name, phone)
    )

    conn.commit()
    cur.close()
    conn.close()

def update_contact():
    old_name = input("Enter name to update: ")
    new_name = input("New name: ")
    new_phone = input("New phone: ")

    conn = connect_db()
    cur = conn.cursor()

    if new_name:
        cur.execute(
            "UPDATE phonebook SET name = %s WHERE name = %s",
            (new_name, old_name)
        )

    if new_phone:
        cur.execute(
            "UPDATE phonebook SET phone = %s WHERE name = %s",
            (new_phone, old_name)
        )

    conn.commit()
    cur.close()
    conn.close()

def search_contacts():
    name = input("Search by name: ")
    phone = input("Search by phone: ")

    conn = connect_db()
    cur = conn.cursor()

    if name:
        cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s", (f"%{name}%",))
    elif phone:
        cur.execute("SELECT * FROM phonebook WHERE phone LIKE %s", (f"{phone}%",))
    else:
        cur.execute("SELECT * FROM phonebook")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()

def delete_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    conn = connect_db()
    cur = conn.cursor()

    if name:
        cur.execute("DELETE FROM phonebook WHERE name = %s", (name,))
    elif phone:
        cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))

    conn.commit()
    cur.close()
    conn.close()

def main():
    while True:
        print("\n1 - Insert from CSV")
        print("2 - Insert from console")
        print("3 - Update")
        print("4 - Search")
        print("5 - Delete")
        print("0 - Exit")

        choice = input("Choose: ")

        if choice == "1":
            insert_from_csv()
        elif choice == "2":
            insert_from_console()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            search_contacts()
        elif choice == "5":
            delete_contact()
        elif choice == "0":
            break


if __name__ == "__main__":
    main()