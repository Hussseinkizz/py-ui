from py_ui.py_ui import Page, Text, View, Button, Engine, createStyles, useStyles


@Engine.Page('/sample')
def SamplePage():
    def handleClick(element, event):
        if event == 'click':
            print('clicked')

        useStyles(element, {
            'color': 'green',
            'flexDirection': 'row',
            'alignItems': 'center',
            'justifyContent': 'space-between',
        })

    return Page(
        View(
            [
                Text('just red', []),
                Text('just bigBlue', [styles.bigBlue]),
                Text('bigBlue, then red', [styles.bigBlue, styles.red]),
                Text('red, then bigBlue', [styles.red, styles.bigBlue])
            ], [styles.container]),
        Button('click me!', onClick=handleClick),
    )


styles = createStyles({
    'container': {
        'marginTop': 50,
    },
    'bigBlue': {
        'color': 'blue',
        'fontWeight': 'bold',
        'fontSize': 30,
    },
    'red': {
        'color': 'red',
    },
})
