import json
import os

# Path to the file where book records are stored
FILE_PATH = "books.txt"

# 📂 Load books from file if it exists
def load_books():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as f:
            return json.load(f)
    return []

# 💾 Save updated book list to file
def save_books(book_list):
    with open(FILE_PATH, 'w') as f:
        json.dump(book_list, f, indent=4)

# ➕ Add a new book to the collection
def add_new_book(book_list):
    print("\n📚 Add a New Book")
    title = input("Title: ")
    author = input("Author: ")
    year = input("Year of Publication: ")
    genre = input("Genre: ")
    read_input = input("Have you read it? (yes/no): ").strip().lower()
    read_status = read_input == 'yes'

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read_status
    }

    book_list.append(book)
    save_books(book_list)
    print(f'✅ "{title}" has been added successfully!')

# 🗑️ Delete a book by its title
def delete_book(book_list):
    print("\n🗑️ Remove a Book")
    to_remove = input("Enter the book title to delete: ").strip().lower()
    original_count = len(book_list)

    # Filter out the book to be removed
    book_list[:] = [b for b in book_list if b['title'].lower() != to_remove]

    if len(book_list) < original_count:
        save_books(book_list)
        print(f'✅ "{to_remove.title()}" has been removed.')
    else:
        print(f'❌ Book titled "{to_remove.title()}" was not found.')

# 🔍 Search books by title or author
def search_books(book_list):
    print("\n🔍 Search Book")
    mode = input("Search by (title/author): ").strip().lower()
    if mode not in ['title', 'author']:
        print("⚠️ Invalid search mode. Try 'title' or 'author'.")
        return

    keyword = input(f"Enter {mode}: ").strip().lower()
    matches = [b for b in book_list if keyword in b[mode].lower()]

    if matches:
        print(f"\n🔎 Found {len(matches)} result(s):")
        for b in matches:
            status = "Read" if b['read'] else "Unread"
            print(f'{b["title"]} by {b["author"]} ({b["year"]}) - {b["genre"]} - {status}')
    else:
        print("❌ No matches found.")

# 📋 Show all books in the library
def show_all_books(book_list):
    print("\n📖 Book Collection")
    if not book_list:
        print("No books found.")
        return

    for b in book_list:
        status = "Read" if b['read'] else "Unread"
        print(f'{b["title"]} by {b["author"]} ({b["year"]}) - {b["genre"]} - {status}')

# 📊 Show stats (total and read %)
def show_stats(book_list):
    print("\n📊 Library Statistics")
    total = len(book_list)
    read_count = sum(1 for b in book_list if b['read'])

    print(f"Total Books: {total}")
    if total > 0:
        percentage = (read_count / total) * 100
        print(f"Books Read: {read_count} ({percentage:.1f}%)")
    else:
        print("Books Read: 0")

# 🎛️ Main menu loop
def main():
    library = load_books()

    while True:
        print("\n========= 📚 Library Manager =========")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. Show All Books")
        print("5. View Statistics")
        print("6. Exit")

        option = input("Choose an option (1-6): ").strip()

        if option == '1':
            add_new_book(library)
        elif option == '2':
            delete_book(library)
        elif option == '3':
            search_books(library)
        elif option == '4':
            show_all_books(library)
        elif option == '5':
            show_stats(library)
        elif option == '6':
            print("👋 Exiting... Thank you for using Library Manager.")
            break
        else:
            print("❌ Invalid selection. Please try again.")

# 🚀 Run the program
if __name__ == "__main__":
    main()
