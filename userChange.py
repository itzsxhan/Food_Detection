from flet import *
import flet as ft
from flet import TextField, Checkbox, ElevatedButton, Row, Text, Column
from flet_core import Page, Container
from flet_core.control_event import ControlEvent
import pandas as pd
from tensorflow.keras.models import load_model
import Main
from checkBox import CustomCheckBox
import random2
from chat import Message, ChatMessage

import csv
from random2 import randint
from app import *

'''
page.title = 'cool'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 700
    page.window_height = 700
    page.window_resizable =True
'''
blue = '#2d3140'
lightBlue = '#e9fafc'
mediumBlue = "#a7bfd7"
coral = '#d17255'
gold = '#E0B15E'

fitness = TextField(color=blue,width=550,height=98)
def taskAdder():
    infoChange =Container(on_click=lambda _: page.go('/'),
                          height=900,
                          width=650,
                          content=Row(controls=[Icon(icons.FULLSCREEN_EXIT_SHARP),Container(height=900,
                          width=650,
                          bgcolor=mediumBlue,
                          border_radius=45, padding=padding.only(left=20, top=25),
                          content=Column(width=3, controls=[Text("Tasks:", color=coral, weight=FontWeight.BOLD, size=17),
                                                            Row(controls=[fitness])])
                          )]))

    return [infoChange,fitness.value]
'''
    Container(height=800,
                       width=650,
                       border_radius=30,
                       bgcolor=blue,
                       content=Column(controls=[Row(controls=
                                                    [Text(value="Fitness Goals", text_align=ft.TextAlign.LEFT, width=350, size=50, height=30)]),
                                                Row(controls=
                                                    [TextField(label="Enter fitness Goals", text_align=ft.TextAlign.LEFT,  width=350, height=50)])],
                                     )
                       )
                    '''
lightGold = '#FFFAEB'
