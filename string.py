text = "Hello world"

print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())

email = "ravi@hotel.com"

print(email.startswith("ravi"))
print(email.endswith(".com"))
print("hotel" in email)
print(email.find("@"))


name = "  Ravi  "

print(name.strip())
print(name.lstrip())
print(name.rstrip())

address = "Bengaluru, Karnataka, India"

print(address.replace("Bengaluru", "Mumbai"))


guest_name = "  ravi sharma  "
print(guest_name)
cn=guest_name.strip().title()
print(cn)


# Clean and format
clean_name = guest_name.strip().title()
print(f"Welcome {clean_name}!")







