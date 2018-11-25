# cli-textformat-py

Textformat-py is a lightweight python module to write colored and formated code onto the linux terminal/cli.<br>
It is capusled as good as possible to has no overhead for the library user and uses the 'Text' class as namespace.

## Motivation
I was inspired by this [stackoverflow post](https://stackoverflow.com/questions/2616906/how-do-i-output-coloured-text-to-a-linux-terminal)
to make a good color/simple format library for Ruby error and test messages on linux terminal. 

## Features
* Coloring text (black, red, green, yellow, blue, magenta, cyan, white)
    * foreground and background support
* bold, underline and inverse text
* multiline support 

## Installation
* Copy <code>src/textformat.py</code> to your project

## Examples
The test.py file shows how you can use the library. 

Below are also some examples:
```python
from src.textformat import Text

print(Text.green("Hello World!"))
print(Text.green("Multiline example", true))
print("Test")
print("Hello" + Text.disable_multiline()) 
print("Normal")
print(Text.bold(Text.underline(Text.red("Error Message:"))))
```

## Testing
This application was testet with xterm and KDE konsole terminals

If the colors are not equal with the method names please check your personal settings on
your terminal. 

## TODO
* port to other languages when finished

## Support
If some errors appears please write a issue that I can fix it.

## See also
* [C++ textformat library](https://github.com/Shadowsith/cli-textformat-cpp)
* [Ruby textformat library](https://github.com/Shadowsith/cli-textformat-ruby)

## License
MIT
