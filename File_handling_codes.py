# creating of file and writing few lines of text in it. and then reading the file and printing the content. 
# then adding (appending) few more lines to the same file and then reading the file afain and printing the content. 

with open("file_name.txt", "w") as file:  
    file.write("this is a line of text")
    file.write("\nthis is another line of text")
    file.write("\nthis is yet another line of text")

with open("file_name.txt", "r") as file:
    content = file.read()
    print(content)

print("\n")

with open("file_name.txt", "a") as file:
    file.write("\nthis is an appended line of text")

with open("file_name.txt", "r") as file:
    content = file.read()
    print(content)