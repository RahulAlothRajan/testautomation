from termcolor import colored
import emoji


def print_error(string: str):
    text = colored(string, "red")
    print("\n" + text + emoji.emojize(":thumbs_down:"))
    pass


def print_warning(string: str):
    text = colored(string, "yellow")
    print("\n" + text + emoji.emojize(":clapping_hands:"))
    pass


def print_success(string: str):
    text = colored(string, "green")
    print("\n" + text + emoji.emojize(":thumbs_up:"))
    pass
