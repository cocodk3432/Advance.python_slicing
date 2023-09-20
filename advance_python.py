
print("Slicing a data\nAdvance slicing ( used in apis and data scraping)")

raw_data = input("Enter your email: ")

(username , domain) = raw_data.split("@")


print('username:'+username)
print('domain:'+domain)


raw = input("Enter your data: ")

(rr , rt) = raw.split("@" or ".")

print(rr,'and',rt)


