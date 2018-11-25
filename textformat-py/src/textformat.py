class Text:
    __begin = "\033[";
    __end = "\033[0m";
    __multiline_end = "\033[0a";
    __reset = "0m";
    __bold = "1m";
    __underline = "4m";
    __inverse = "7m";
    __bold_off = "21m";
    __underline_off = "24m";
    __invserse_off = "27m";

    # foreground
    def black(text, multiline = False):
        if(multiline == True):
            return  Text.__begin + Text.Color.Fg.black + text + Text.__multiline_end;
        else:
            return Text.__begin + Text.Color.Fg.black + text + Text.__end;

    def red(text, multiline = False):
        if(multiline == True):
            return  Text.__begin + Text.Color.Fg.red + text + Text.__multiline_end;
        else:
            return Text.__begin + Text.Color.Fg.red + text + Text.__end;

    def green(text, multiline = False):
        if(multiline == True):
            return  Text.__begin + Text.Color.Fg.green + text + Text.__multiline_end;
        else:
            return Text.__begin + Text.Color.Fg.green + text + Text.__end;

    def yellow(text, multiline = False):
        if(multiline == True):
            return  Text.__begin + Text.Color.Fg.yellow + text + Text.__multiline_end;
        else:
            return Text.__begin + Text.Color.Fg.yellow + text + Text.__end;

    def blue(text, multiline = False):
        if(multiline == True):
            return  Text.__begin + Text.Color.Fg.blue + text + Text.__multiline_end;
        else:
            return Text.__begin + Text.Color.Fg.blue + text + Text.__end;

    def magenta(text, multiline = False):
        if(multiline == True):
            return  Text.__begin + Text.Color.Fg.magenta + text + Text.__multiline_end;
        else:
            return Text.__begin + Text.Color.Fg.magenta + text + Text.__end;

    def cyan(text, multiline = False):
        if(multiline == True):
            return  Text.__begin + Text.Color.Fg.cyan + text + Text.__multiline_end;
        else:
            return Text.__begin + Text.Color.Fg.cyan + text + Text.__end;

    def white(text, multiline = False):
        if(multiline == True):
            return  Text.__begin + Text.Color.Fg.white + text + Text.__multiline_end;
        else:
            return Text.__begin + Text.Color.Fg.white + text + Text.__end;

    # background 

    def black_bg(text, multiline = False):
        if(multiline == True):
            return  Text.__begin + Text.Color.Bg.black + text + Text.__multiline_end;
        else:
            return Text.__begin + Text.Color.Bg.black + text + Text.__end;

    def red_bg(text, multiline = False):
        if(multiline == True):
            return  Text.__begin + Text.Color.Bg.red + text + Text.__multiline_end;
        else:
            return Text.__begin + Text.Color.Bg.red + text + Text.__end;

    def green_bg(text, multiline = False):
        if(multiline == True):
            return  Text.__begin + Text.Color.Bg.green + text + Text.__multiline_end;
        else:
            return Text.__begin + Text.Color.Bg.green + text + Text.__end;

    def yellow_bg(text, multiline = False):
        if(multiline == True):
            return  Text.__begin + Text.Color.Bg.yellow + text + Text.__multiline_end;
        else:
            return Text.__begin + Text.Color.Bg.yellow + text + Text.__end;

    def blue_bg(text, multiline = False):
        if(multiline == True):
            return  Text.__begin + Text.Color.Bg.blue + text + Text.__multiline_end;
        else:
            return Text.__begin + Text.Color.Bg.blue + text + Text.__end;

    def magenta_bg(text, multiline = False):
        if(multiline == True):
            return  Text.__begin + Text.Color.Bg.magenta + text + Text.__multiline_end;
        else:
            return Text.__begin + Text.Color.Bg.magenta + text + Text.__end;

    def cyan_bg(text, multiline = False):
        if(multiline == True):
            return  Text.__begin + Text.Color.Bg.cyan + text + Text.__multiline_end;
        else:
            return Text.__begin + Text.Color.Bg.cyan + text + Text.__end;

    def white_bg(text, multiline = False):
        if(multiline == True):
            return  Text.__begin + Text.Color.Bg.white + text + Text.__multiline_end;
        else:
            return Text.__begin + Text.Color.Bg.white + text + Text.__end;

    # formatting 
    def bold(text, multiline = False):
        if(multiline == True):
            return  Text.__begin + Text.__bold + text + Text.__multiline_end;
        else:
            return Text.__begin + Text.__bold + text + Text.__end;

    def disable_multiline():
        return Text.__end

    def inverse(text, multiline = False):
        if(multiline == True):
            return  Text.__begin + Text.__inverse + text + Text.__multiline_end;
        else:
            return Text.__begin + Text.__inverse + text + Text.__end;

    def underline(text, multiline = False):
        if(multiline == True):
            return  Text.__begin + Text.__underline + text + Text.__multiline_end;
        else:
            return Text.__begin + Text.__underline + text + Text.__end;

    class Color:
        class Fg:
            black = "30m";
            red = "31m";
            green = "32m";
            yellow = "33m";
            blue = "34m";
            magenta = "35m";
            cyan = "36m";
            white = "37m";


        class Bg:
            black = "40m";
            red = "41m";
            green = "42m";
            yellow = "43m";
            blue = "44m";
            magenta = "45m";
            cyan = "46m";
            white = "47m";

