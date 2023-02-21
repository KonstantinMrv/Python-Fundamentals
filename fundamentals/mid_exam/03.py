books = input().split("&")

command = input()
while command != "Done":
    command_args = command.split(" | ")
    command = command_args[0]
    book_name = command_args[1]
    if command == "Add Book":
        if book_name in books:
            command = input()
            continue
        else:
            books.insert(0, book_name)
    elif command == "Take Book":
        if book_name in books:
            books.remove(book_name)
        else:
            command = input()
            continue
    elif command == "Swap Books":
        second_book = command_args[2]
        if book_name in books and second_book in books:
            first_book_index = books.index(book_name)
            second_book_index = books.index(second_book)
            books.pop(first_book_index)
            books.insert(first_book_index, second_book)
            books.pop(second_book_index)
            books.insert(second_book_index, book_name)
        else:
            command = input()
            continue
    elif command == "Insert Book":
        if book_name in books:
            command = input()
            continue
        else:
            books.append(book_name)
    elif command == "Check Book":
        index = int(book_name)
        if index < 0 or index > len(books):
            command = input()
            continue
        else:
            print(books[index])

    command = input()

print(", ".join(books))