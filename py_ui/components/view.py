from types.types import Component, Handler
from utils.evaluateComponent import evaluateComponent


def View(children: Component, classNames: list[str], onClick: Handler = None) -> str:
    """A View component which finally renders into a normal html div in the broswer. `<div>...</div>`

    Args:
        children (str or component): the div content to render into the div
        classNames (list[str]): the styles to apply to the div
        onClick (Handler, optional): handler function to handle given button event, Defaults to None.

    Returns:
        str: preprocessed html div string
    """

    css_class_string = " ".join(classNames)
    return f'<div class="{css_class_string}">{evaluateComponent(children)}</div>'
