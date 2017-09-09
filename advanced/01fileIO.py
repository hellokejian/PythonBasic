# text = "this is my first text\nthis is next line\nthis is the last line"
#
# my_file = open('d:/my file.txt', 'w')
# my_file.write(text)
# my_file.close()

append_text = '\nthis is appended text'
my_file = open('d:/my file.txt', 'a')
my_file.write(append_text)
my_file.close()
