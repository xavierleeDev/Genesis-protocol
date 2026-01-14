# 1. Messy Input
company = "legacy safety & consulting"

# 2. Clean it up
print(company.title())  # Capitalizes first letter of each word
print(company.upper())  # YELLS IT (Good for codes/IDs)

# 1. The "Dirty" Variable (Notice the spaces)
well_id = "  H2S-004  "

# 2. The problem (Python sees the spaces)
print(f"'{well_id}'")

# 3. The Fix (Strip removes whitespace from both ends)
clean_id = well_id.strip()
print(f"'{clean_id}'")

print("Languages:\n\tPython\n\tC\n\tJavaScript")

username = "Xavier"
print(f"Welcome back {username}")