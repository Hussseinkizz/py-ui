from types.types import Component
# implement the styling modules


def createStyles(styles: dict[dict]) -> str:
    """A Style utility which is used to create styles (css) for components.

    Args:
        styles (dict[dict]): the styles to create and bind to element.

    Returns:
        str: a css object with namespaces bound to the given styles.
    """
    pass


def useStyles(element: Component, styles: dict[str, str]) -> Component:
    """A Style utility which is used to apply styles (css) to a given element

    Args:
        element (Component): the element to apply styles to.
        styles (dict[str, str]): the styles to apply to the element.

    Returns:
        Component: the element with the given styles applied.
    """
