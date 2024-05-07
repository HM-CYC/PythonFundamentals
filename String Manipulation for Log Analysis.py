#Write a Python program that manipulates strings to extract relevant information from log entries.

log_entry = "2024-05-04 10:20:00 | Iraq , Alshaab Univ | User 'محسن' logged in successfully ."

timestamp = log_entry[:19]

log_level_start = log_entry.find("|") + 2
log_level_end = log_entry.find("|", log_level_start)
log_level = log_entry[log_level_start:log_level_end]

username_start = log_entry.find("'") + 1
username_end = log_entry.find("'", username_start)
username = log_entry[username_start:username_end]

print("Timestamp:", timestamp)
print("Location:", log_level)
print("Username:", username)
