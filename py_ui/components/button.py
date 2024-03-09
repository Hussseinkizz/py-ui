from types.types import Component, Handler
from utils.evaluateComponent import evaluateComponent


def Button(children: Component, classNames: list[str], onClick: Handler = None) -> str:
    """A Button component which finally renders into a normal html button in the broswer. `<button>...</button>`

    Args:
        children (str or component): the button content to render into the button
        classNames (list[str]): the styles to apply to the button
        onClick (Handler, optional): handler function to handle given button event, Defaults to None.

    Returns:
        str: preprocessed html button string
    """

    css_class_string = " ".join(classNames)
    return f'<button class="{css_class_string}">{evaluateComponent(children)}</button>'


if __name__ == "__main__":
    print(Button('hello', ['btn', 'btn-primary']))
    # prints: <button class="btn btn-primary">hello</button>
