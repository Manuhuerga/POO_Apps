import justpy as jp
from justpy import tailwind
from justpy.htmlcomponents import Path

class About:
    path = '/about'
    def __init__(self) -> None:
        pass
    def server(self):
        wp = jp.QuasarPage(tailwind = True)
        div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text = 'This is the about page!', classes='text-4xl m-2')
        jp.Div(a=div, text ='This is a body of about page')
        return wp


