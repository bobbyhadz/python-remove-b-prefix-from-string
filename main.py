# Remove the 'b' prefix from a string in Python

my_bytes = 'bobbyhadz.com'.encode('utf-8')
print(my_bytes)  # 👉️ b'bobbyhadz.com'
print(type(my_bytes))  # 👉️ <class 'bytes'>


string = my_bytes.decode('utf-8')
print(string)  # 👉️ bobbyhadz.com
print(type(string))  # 👉️ <class 'str'>