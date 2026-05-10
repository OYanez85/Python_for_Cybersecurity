# Access a text file in Python
with open("login_attempts.txt", "r") as file:
    content = file.read()
    print(content)
    
# Open, read and split a text file
with open("login_attempts.txt", "r") as file:
    file_text = file.read()
    print(file_text.split())

# list to be reused in another code by creating a variable
usernames = file_text.split()

# .spli()
approved_users = "elarson,bmoreno,tshah,sgilmore,eraab"
print("before .split():", approved_users)
approved_users = approved_users.split(",")
print("after .split():", approved_users)

# how a string of usernames that are separated by space can be split into a list through the .split() method
removed_users = "wjaffrey jsoto abernard jhill awilliam"
print("before .split():", removed_users)
removed_users = removed_users.split()
print("after .split():", removed_users)

# Applying .split() to files
with open("update_log.txt", "r") as file:
    updates = file.read()
updates = updates.split()

# .join()
approved_users = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]
print("before .join():", approved_users)
approved_users = ",".join(approved_users)
print("after .join():", approved_users)

# Applying .join() to files
with open("update_log.txt", "r") as file:
    updates = file.read()
updates = updates.split()

# Joining a list of strings into a single string
updates = " ".join(updates)
with open("update_log.txt", "w") as file:
    file.write(updates)