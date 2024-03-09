from types.types import Component, Handler
from utils.evaluateComponent import evaluateComponent


def Image(imagePath: str, classNames: list[str], alt: str = '', onClick: Handler = None) -> str:
    """An Image component which finally renders into a normal html image tag in the broswer. `<img src="..." alt="..."/>`

    Args:
        imagePath (str): the path to the image in the static directory
        alt (str, optional): the alt text to display if the image fails to load, Defaults to ''.
        classNames (list[str]): the styles to apply to the image
        onClick (Handler, optional): handler function to handle any given event, Defaults to None.

    Returns:
        str: preprocessed html string
    """
    return f'<img src="/static/{imagePath}" alt="{alt}">'
