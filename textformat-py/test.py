from src.textformat import Text

print("Foreground color test")
print(Text.red("test"))
print(Text.green("test"))
print(Text.yellow("test"))
print(Text.blue("test"))
print(Text.magenta("test"))
print(Text.cyan("test"))
print(Text.white("test"))
print(Text.black("test"))
print("")

print("Background color test")
print(Text.red_bg("test"))
print(Text.green_bg("test"))
print(Text.yellow_bg("test"))
print(Text.blue_bg("test"))
print(Text.magenta_bg("test"))
print(Text.cyan_bg("test"))
print(Text.white_bg(Text.black("test")))
print(Text.black_bg("test"))
print("")

print(Text.red("Error message:", True))
print("Error 1 at line 2")
print("Error 2 at line 40")
print(Text.disable_multiline()) 

print("normal")

print(Text.green(Text.bold(Text.underline("Success message:", True), True), True))
print("All tests succeed:")
print("program runs as expected" + Text.disable_multiline())

print("normal")
