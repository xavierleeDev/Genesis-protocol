# 1. The Input (Messy Data)
first_name = "xavier"
last_name = "lee"

# 2. The Logic (F-strings & Methods)
# f"{}" acts like a glue gun, sticking variables together.
full_name = f"{first_name} {last_name}"

# 3. The Output (Clean Data)
print(f"Raw Data: {full_name}")
print(f"Formatted: {full_name.title()}") # Capitalizes first letters 
print(f"Official: {full_name.upper()}") # ALL CAPS for emphasis 

# 4. Whitespace (Formatting)
print("\n\t* Founder\n\t* Developer\n\t* Father")