import colorama

class log_c:
    '''
    simple logger class, yes, I know logging exists, but I just wanted
    something simple for this.
    '''
    def error(self, msg):
        print(
            colorama.Fore.RED +
            f'ERROR: {msg}' +
            colorama.Fore.RESET
        )

    def info(self, msg):
        print(
            colorama.Fore.RESET +
            f'{msg}' +
            colorama.Fore.RESET
        )

    def good(self, msg):
        print(
            colorama.Fore.GREEN +
            f'{msg}' +
            colorama.Fore.RESET
        )

    def separator(self, symbol):
        tmp = symbol * 15
        print(tmp)

def color_sign(x):
    c = colorama.Fore.GREEN
    if x == 0:
        c = colorama.Fore.BLUE
    if x == 6:
        c = colorama.Fore.BLACK
    if x == 8:
        c = colorama.Fore.RED
    return f'{c}{x}{colorama.Fore.RESET}'

