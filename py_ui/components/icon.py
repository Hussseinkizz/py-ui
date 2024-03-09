from types.types import Handler


def Icon(svg: str, classNames: list[str], onClick: Handler = None) -> str:
    """An Icon component which finally renders into a normal html svg icon wrapped inside a span in the broswer. `<span><svg>...</svg></span>`

    Args:
        svg (str): a multiline string of svg code
        classNames (list[str]): the styles to apply to the icon wrapper
        onClick (Handler, optional): handler function to handle any given event, Defaults to None.

    Returns:
        str: preprocessed html string
    """
    pass
