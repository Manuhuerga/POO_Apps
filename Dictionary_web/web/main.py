from home import Home
from about import About
from dic import Dicctionary
import justpy as jp

jp.Route(Home.path, Home.server)
jp.Route(About.path, About.server)
jp.Route(Dicctionary.path, Dicctionary.server)
jp.justpy(port=8001)
