def evaluateComponent(component):
    if isinstance(component, str):
        return component
    return component()
