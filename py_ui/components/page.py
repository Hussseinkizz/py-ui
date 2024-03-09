from types.types import Component, Handler
from utils.evaluateComponent import evaluateComponent


def Page(children: list[Component], globalStyles: list[str], **kwargs) -> str:
    """A Page component which finally renders into a normal html section in the broswer. `<section>...</section>` Intended as a page that wrapps other elements on a page, it acts as an html document.

    Args:
        children (str or component): the components to render into the app
        globalStyles (list[str]): the styles to apply on a global scope
    Returns:
        str: preprocessed html page string
    """

    return f'<section>...</section>'
