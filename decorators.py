
def add_wrapping_with_style(style):
    def add_wrapping(item):
        def wrapped_item():
            return f'a {style} wrapped up a box for {item()}'
        return wrapped_item
    return add_wrapping
@add_wrapping_with_style('Neatly')
def new_gpu():
    return 'A new Tesla P100 GPU'

print(new_gpu())