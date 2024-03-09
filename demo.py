from py_ui import Button


def Component():
    def handleClick(element, event):
        if event == 'click':
            print('clicked')

    return Button('click me!', onClick=handleClick),
