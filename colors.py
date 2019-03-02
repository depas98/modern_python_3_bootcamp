from termcolor import colored

# print("*** dir about of module ***")
# print(dir(termcolor))
#
# # help about of module
# import termcolor
# help(termcolor)

text = colored("HI THERE!", color="cyan", on_color="on_yellow", attrs=["blink"])
print(text)

