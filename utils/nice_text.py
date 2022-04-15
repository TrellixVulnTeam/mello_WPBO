import pyfiglet


def get_text(text):
    """Converts the text into an ascii text art"""
    return pyfiglet.figlet_format(text)
