# for num in range(10):
#     print(num)

# for num in range(10,20,2):
#     print(num)
#
# x = 0
# for num in range(11,20,2):
#     print(f"Nxt number is {num}")
#     x+=num
#     print(x)

# num_times = input("How many time do I have to tell you? ")
# try:
#     num_times = int(num_times)
#     for num in range(num_times):
#         print(f"time {num+1}: CLEAN UP YOUR ROOm!")
# except ValueError:
#     print("Invalid value, enter an integer")

# for x in range(1,21):
#     if x == 4 or x == 13:
#         state = "unlucky"
#     elif x % 2 == 0:
#         state = "even"
#     else:
#         state = "odd"
#
#     print(f"{x} is {state}")

emoji = "\U0001f600"
for x in range(1, 11):
    print(emoji * x)

limit = 1
emoji = "\U0001f600"
while limit < 11:
    print(emoji * limit)
    limit += 1

while True:
    entry = input("Type 'exit' to exit: ")
    if entry == "exit":
        break
