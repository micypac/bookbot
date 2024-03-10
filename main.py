def main():  
  with open("./books/frankenstein.txt") as f:
    file_contents = f.read()
    
  word_count = count_words(file_contents)
  
  letter_count = count_letters(file_contents)
  
  sorted_letter_cnt = sorted(letter_count.items(), key=lambda x:x[1], reverse=True)
  
  print("--- Begin report of books/frankenstein.txt ---")
  print(f"{word_count} words found in the document")
  print()
  for item in sorted_letter_cnt:
    print(f"The {item[0]} character was found {item[1]} times")
  print("--- End report ---")
  

def count_words(words):
  word_list = words.split()
  return len(word_list)


def count_letters(word):
  my_map = {}
  for char in word.lower():
    if char in "abcdefghijklmnopqrstuvwxyz":
      my_map[char] = my_map.get(char, 0) + 1
    
  return my_map
      

main()
