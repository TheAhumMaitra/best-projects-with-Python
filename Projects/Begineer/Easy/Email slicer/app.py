# Email slicer program using Python
email = list(input("Enter your email : "))
sign = email.index("@")

username = email [ : sign ]
domain = email [ sign + 1 : ]
print(f"Your username \'{''.join(username)}\' and your domain is \'{''.join(domain)}\'")
