#For Loop with Multiple List
names = ['Ankit', 'Jhon', 'Joe']
email_domains = ['gmail', 'outlook', 'iCloud']

for name, email_domain in zip(names, email_domains):
    print("Name:", name, "Email Domain:", email_domain)