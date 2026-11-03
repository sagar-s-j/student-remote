print("== Student Login ==")
user = input("Username: ")
pwd = input("Password: ")
print("Login successful" if user == "admin" and pwd == "1234" else "Invalid login")