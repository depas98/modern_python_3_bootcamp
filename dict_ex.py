donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)

total_donations = 0
for donation in donations.values():
    total_donations += donation

print(f"total donations = {total_donations}")

total_donations = sum(donation for donation in donations.values())
print(f"total donations = {total_donations}")

total_donations = sum(donations.values())
print(f"total donations = {total_donations}")

print("sam" in donations)

if "sam" in donations:
    print(f"the value is {donations['sam']}")
else:
    print("it doesn't exist")
