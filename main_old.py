import sys
from stats import get_count
from stats import character_count
from stats import sort_dic


def get_book_text(text_path):
    with open(text_path) as f:
        file_contents = f.read()

        return file_contents



def main():
    char_count = {}
    count = 0

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]



file_contents = get_book_text(book_path)                                      
count = get_count( file_contents)
char_count = character_count(file_contents)


    
sorted_dic = sort_dic(char_count)


    

print("============ BOOKBOT ============")
print("Analyzing book found at {book_path}...")
print("----------- Word Count ----------")
print(f"Found {count} total words")
print("--------- Character Count -------")
    
for key, value in sorted_dic.items():
     if key.isalpha():
        print(f"{key}: {value}")
       
print("============= END ===============")

main()
