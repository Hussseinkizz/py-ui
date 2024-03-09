from types.types import Component, Handler
from utils.evaluateComponent import evaluateComponent


def Text(children: Component, classNames: list[str], onClick: Handler = None, variant: str = 'h1') -> str:
    """A Text component which finally renders into a normal html h1 in the broswer. `<h1>...</h1>`

    Args:
        children (str or icon component): the text content to render into the result heading tag
        variant (str, optional): the variant of the heading tag, Defaults to 'h1' for h1.
        classNames (list[str]): the styles to apply to the heading tag
        onClick (Handler, optional): handler function to handle given button event, Defaults to None.

    Returns:
        str: preprocessed html string
    """

    css_class_string = " ".join(classNames)
    return f'<h1 class="{css_class_string}">{evaluateComponent(children)}</h1>'
