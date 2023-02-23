def email_split():
    email = input("Please enter your email:")
    (username,domain) = email.split("@")
    (domain,other) = domain.split(".")

    print("Username :"+username)
    print("domain :" +domain)
    print("other :"+other)

email_split()