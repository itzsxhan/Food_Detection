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
from userChange import *
import csv
import cv2
from random2 import randint
from ultralytics import YOLO


def main(page=ft.Page) -> None:
    blue = '#2d3140'
    lightBlue = '#e9fafc'
    mediumBlue = "#a7bfd7"
    coral = '#d17255'
    gold = '#E0B15E'
    lightGold = '#FFFAEB'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    model = YOLO("best (1).pt")

    username: TextField = TextField(label="Username", text_align=ft.TextAlign.LEFT, width=350)
    password: TextField = TextField(label="Password", text_align=ft.TextAlign.LEFT, width=350, password=True)
    signUp: Checkbox = Checkbox(label="I agree to terms and conditions", value=False)
    submitButton: ElevatedButton = ElevatedButton(text='Sign up', width=200, disabled=True)

    userFile = open("userDataSet.txt",'r')
    user = userFile.readlines()
    for i in range(0,len(user)):
        user[i] = user[i].strip("\n")
        user[i] = user[i].split("|")
    print(user)
    userNames = []
    passWords = []
    '''
    fileParse = open("Username&Passwords.txt", "r")
    for line in fileParse:
        dummyArray = line.split(" ")
        userNames.append(dummyArray[0])
        passWords.append(dummyArray[1])
    fileParse.close()
    print(userNames)
'''
    page.title = 'MealToGo'
    page.fonts = {
        'PD': 'Playfair Display'
    }

    page.add(Text("Meal", size=70, font_family='PD', weight=ft.FontWeight.BOLD, color=gold,
                  spans=[ft.TextSpan("ToGo", ft.TextStyle(font_family='Canva Sans', size=70, weight=ft.FontWeight.BOLD,
                                                          color='white'))],
                  text_align=ft.TextAlign.CENTER))
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 725
    page.window_height = 1000
    page.window_resizable = True

    def validate(e: ControlEvent) -> None:
        if all([username.value, password.value, signUp.value,[username.value,password.value] in user]):
            submitButton.disabled = False
        else:
            submitButton.disabled = True
        page.update()

    signUp.on_change = validate
    username.on_change = validate
    password.on_change = validate




    tasks = Column(
        height=430,
        scroll='auto',
        # controls=[Container(height= 100, width= 700, bgcolor= mediumBlue, border_radius= 45)]
    )
    fitness_todo_list = [
        "Go for a 30-minute jog",
        "Do 20 push-ups",
        "Stretch for 10 minutes",
        "Drink 8 glasses of water",
        "Prepare a healthy meal",
        "Take a cycling class",
        "Practice yoga for 15 minutes",
        "Try a new healthy recipe",
        "Do a workout",
        "Get at least 7 hours of sleep"
    ]

    for i in fitness_todo_list:
        tasks.controls.append(
            Container(height=98,
                      width=700,
                      bgcolor=mediumBlue,
                      border_radius=45, padding=padding.only(left=20, top=25),
                      content=Column(width=3, controls=[Text("Tasks:", color=coral, weight=FontWeight.BOLD, size=17),
                                                        Row(controls=[CustomCheckBox(blue, stroke_width=5),
                                                                      Text(i, color=blue, size=20, font_family='PD',
                                                                           weight=FontWeight.BOLD)])]),
                      )
        )

    def shrink(e):
        page_2.controls[0].width = 450
        page_2.controls[0].scale = transform.Scale(0.8, alignment=alignment.center_right)
        page_2.controls[0].border_radius = border_radius.only(top_left=35, top_right=0, bottom_left=35, bottom_right=0)
        page_2.update()

    def restore(e):
        page_2.controls[0].width = 650
        page_2.controls[0].scale = transform.Scale(1, alignment=alignment.center_right)
        page_2.update()

    def route_change(route):
        page.views.clear()
        page.views.append(
            pages[page.route]
        )

    circle = Stack(
        controls=[
            Container(
                width=100,
                height=100,
                border_radius=50,
                bgcolor='white12'
            ),
            Container(
                gradient=SweepGradient(
                    center=alignment.center,
                    start_angle=0.0,
                    end_angle=3,
                    stops=[0.5, 0.5],
                    colors=['#00000000', coral],
                ),
                width=100,
                height=100,
                border_radius=50,
                content=Row(alignment='center',
                            controls=[
                                Container(padding=padding.all(5),
                                          bgcolor=blue,
                                          width=90, height=90,
                                          border_radius=50,
                                          content=Container(bgcolor=lightBlue,
                                                            height=80, width=80,
                                                            border_radius=40,
                                                            content=CircleAvatar(opacity=0.8,
                                                                                 foreground_image_url="https://api.wallpapers.ai/static/downloads/4fb6a17634b74186850e9e3bf9fae995/upscaled/000000_98188236_kdpmpp2m15_PS7.5_Obito_uchiha_sad_sitting_on_a_cliff._digital_art_concept_art_[upscaled].jpg"
                                                                                 )
                                                            )
                                          )
                            ],
                            ),
            ),

        ]
    )

    circle2 = Stack(
        controls=[
            Container(
                width=80,
                height=80,
                border_radius=50,
                bgcolor='white12'
            ),
            Container(
                gradient=SweepGradient(
                    center=alignment.center,
                    start_angle=0.0,
                    end_angle=3,
                    stops=[0.5, 0.5],
                    colors=['#00000000', coral],
                ),
                width=80,
                height=80,
                border_radius=50,
                content=Row(alignment='center',
                            controls=[
                                Container(padding=padding.all(5),
                                          bgcolor=blue,
                                          width=90, height=90,
                                          border_radius=50,
                                          content=Container(bgcolor=lightBlue,
                                                            height=60, width=60,
                                                            border_radius=40,
                                                            content=CircleAvatar(opacity=0.8,
                                                                                 foreground_image_url="https://img.freepik.com/free-vector/doctor-character-background_1270-84.jpg?size=338&ext=jpg&ga=GA1.1.735520172.1710979200&semt=ais"
                                                                                 )
                                                            )
                                          )
                            ],
                            ),
            ),

        ]
    )

    categories = Row(scroll=True)

    contact = FloatingActionButton(width=190, bgcolor=blue, height=130, text="Get Help",
                                   on_click=lambda _: page.go('/messageBox'))

    meal_plan = FloatingActionButton(width=190, bgcolor=blue, height=130, text="Meal Plan",
                                     on_click=lambda _: page.go('/meal'))

    foodCheck = FloatingActionButton(width=190, height=130, bgcolor=blue, text="Calories",
                                     on_click=lambda _: page.go('/food_detect'))

    categorical_List = [contact, meal_plan, foodCheck]

    for category in categorical_List:
        categories.controls.append(
            category
        )

    first_page_contents = Container(
        content=Column(
            controls=[
                Row(alignment='spaceBetween', controls=[
                    Container(
                        on_click=lambda e: shrink(e),
                        content=Icon(icons.MENU, size=35)),
                    Row(controls=[
                        Icon(icons.SEARCH, size=35),
                        Icon(icons.NOTIFICATIONS_OUTLINED, size=35)
                    ])
                ]),
                Text(value='What\'s up !!!', font_family='PD', weight=ft.FontWeight.BOLD,
                     color=blue, size=25),
                Text(
                    value='CATEGORIES', font_family='PD', weight=ft.FontWeight.BOLD, color=blue
                ),
                Container(
                    padding=padding.only(top=10, bottom=20),
                    content=categories
                ),
                Container(height=20),
                Text("FITNESS GOALS", font_family='PD', weight=ft.FontWeight.BOLD, color=blue),
                Stack(
                    controls=[
                        tasks,
                        FloatingActionButton(bottom=2, right=20,
                                             icon=icons.ADD, bgcolor=coral, on_click=lambda _: page.go('/addTask')
                                             )
                    ]
                )

            ]
        )
    )

    vitals = Column(height=350, scroll='auto')

    features = ["BMI", "Weight", "Height",
                'Physical Activity', 'Fruit Consumption', 'Calorie Intake', 'Heavy Alcohol Consumption']

    for j in features:
        vitals.controls.append(
            Container(
                border_radius=20,
                bgcolor=blue,
                width=270,
                height=110,
                padding=15,
                content=Column(
                    controls=[
                        Text(j, font_family='PD', weight=FontWeight.BOLD),
                        Container(
                            width=random2.randint(25, 160),
                            height=5,
                            bgcolor=coral,
                            border_radius=20,
                            padding=padding.only(right=j * 30),
                            content=Container(
                                bgcolor=coral,
                            ),

                        )
                    ]

                )
            )
        )

    page.on_route_change = route_change
    page_1 = Container(content=Column(alignment=MainAxisAlignment.SPACE_EVENLY, controls=
    [Row(controls=[Container(content=Column(alignment=MainAxisAlignment.SPACE_EVENLY, controls=[
        Container(content=Column(controls=[Icon(icons.ARROW_BACK_IOS_NEW, color=blue),
                                           Row(controls=[Text(" Sehan", size=52, weight='bold', color=blue),
                                                         Container(height=15), circle]),
                                           Text('  Vitals:', size=32, weight='bold', color=blue), vitals])
                  , width=435, height=570, alignment=alignment.top_left)]),
                             padding=padding.only(bottom=20, right=20),
                             on_click=lambda e: restore(e),
                             width=480,
                             height=800,
                             bgcolor=mediumBlue,
                             border_radius=25,
                             alignment=alignment.top_left)]
         )]
                                      ))
    page_2 = Row(alignment='end',
                 controls=[Container(
                     width=650,
                     height=900,
                     bgcolor=lightBlue,
                     border_radius=30,
                     animate=animation.Animation(600, AnimationCurve.DECELERATE),
                     animate_scale=animation.Animation(400, curve='decelerate'),
                     padding=padding.only(
                         top=50, left=20,
                         right=20, bottom=5
                     ),
                     content=Column(
                         controls=[first_page_contents]
                     )
                 )]
                 )

    container = Container(
        width=650,
        height=900,
        bgcolor=blue,
        border_radius=30,
        content=Stack(
            controls=[page_1, page_2])

    )

    create_task_view = Container(
        content=Container(on_click=lambda _: page.go('/'),
                          height=40, width=40,
                          content=Icon(icons.FULLSCREEN_EXIT_SHARP))
    )

    calorieCalc = Container(
        content=Container(on_click=lambda _: page.go('/'),
                          height=40, width=40,
                          content=Row(controls=[Icon(icons.FULLSCREEN_EXIT_SHARP)]))
    )

    doctorContacts = Column(height=800, scroll=ScrollMode.AUTO)

    # List of example doctor information
    doctor_info_list = [
        "  Name: Dr. John Smith\nSpecialty: Cardiology\nExperience: 15 years\nLocation: New York",
        "  Name: Dr. Sarah Johnson\nSpecialty: Pediatrics\nExperience: 10 years\nLocation: Los Angeles",
        "  Name: Dr. Michael Lee\nSpecialty: Dermatology\nExperience: 12 years\nLocation: Chicago",
        "  Name: Dr. Emily Wang\nSpecialty: Psychiatry\nExperience: 8 years\nLocation: San Francisco",
        "  Name: Dr. David Brown\nSpecialty: Orthopedics\nExperience: 20 years\nLocation: Houston",
        "  Name: Dr. Jennifer Martinez\nSpecialty: Obstetrics & Gynecology\nExperience: 18 years\nLocation: Miami",
        "  Name: Dr. William Taylor\nSpecialty: Ophthalmology\nExperience: 14 years\nLocation: Boston",
        "  Name: Dr. Jessica Chen\nSpecialty: Neurology\nExperience: 11 years\nLocation: Seattle",
        "  Name: Dr. Andrew Rodriguez\nSpecialty: Family Medicine\nExperience: 9 years\nLocation: Dallas",
        "  Name: Dr. Samantha White\nSpecialty: Endocrinology\nExperience: 13 years\nLocation: Atlanta"
    ]

    # Dictionary to store doctor information
    doctors_dict = {}

    # Generating 10 different doctor information pages
    for i in range(10):
        random_index = random2.randint(0, len(doctor_info_list) - 1)
        doctor_info = doctor_info_list[random_index]
        doctors_dict[f"Doctor {i + 1}"] = doctor_info

    for doctor in range(10):
        doctorContacts.controls.append(
            Container(height=150, width=650,
                      content=Row(alignment=MainAxisAlignment.CENTER, controls=[Container(height=150,
                                                                                          width=270,
                                                                                          bgcolor=blue,
                                                                                          border_radius=35,
                                                                                          content=Row(controls=[circle2,
                                                                                                                Text(
                                                                                                                    doctors_dict[
                                                                                                                        f"Doctor {random2.randint(1, 10)}"])])),
                                                                                Container(height=150,
                                                                                          width=270,
                                                                                          bgcolor=blue,
                                                                                          border_radius=35,
                                                                                          content=Row(controls=[circle2,
                                                                                                                Text(
                                                                                                                    doctors_dict[
                                                                                                                        f"Doctor {random2.randint(1, 10)}"])]))]))
        )
        '''
    messageBox = Container(
        content=Container(on_click=lambda _: page.go('/'),
                          height=900,
                          width=650,
                          content=Row(controls=[Icon(icons.FULLSCREEN_EXIT_SHARP), Column(controls=[Container(width=650,
                                                                                                              height=900,
                                                                                                              bgcolor=lightBlue,
                                                                                                              border_radius=35,
                                                                                                              content=Column(controls=[Text('         Contacts: ',size=50,color=blue,font_family='Merriweather',weight=FontWeight.BOLD),doctorContacts]))])],
                                      height=900,
                                      width=650))
    )
'''
    df = pd.read_csv('idknewcv.csv')
    model = load_model('models/diabetes.h5')
    ypredict = model.predict(df, verbose=0)
    if ypredict == 0:
        ypredict = 'non diabetic'
    else:
        ypredict = 'diabetic'
    meal = Main.ask_gpt(f"give me a meal plan, and use this dataset to make it specific to me{df}, and i am {ypredict}")
    print(meal)

    def join_chat_click(e):
        if not join_user_name.value:
            join_user_name.error_text = "Name cannot be blank!"
            join_user_name.update()
        else:
            page.session.set("user_name", join_user_name.value)
            page.dialog.open = False
            new_message.prefix = ft.Text(f"{join_user_name.value}: ")
            page.pubsub.send_all(
                Message(user_name=join_user_name.value, text=f"{join_user_name.value} has joined the chat.",
                        message_type="login_message"))
            page.update()

    def send_message_click(e):
        if new_message.value != "":
            page.pubsub.send_all(Message(page.session.get("user_name"), new_message.value, message_type="chat_message"))
            respo = Main.ask_gpt(new_message.value + " ")
            page.pubsub.send_all(Message("MedStat", respo, message_type="chat_message"))
            print(respo)
            new_message.value = ""
            new_message.focus()
            page.update()

    def on_message(message: Message):
        if message.message_type == "chat_message":
            m = ChatMessage(message)
        elif message.message_type == "login_message":
            m = Text(message.text, italic=True, color=colors.BLACK45, size=12)
        chat.controls.append(m)
        page.update()

    meal_plan = Container(
        content=Container(on_click=lambda _: page.go('/'),
                          height=900,
                          width=650,
                          content=Row(controls=[Icon(icons.FULLSCREEN_EXIT_SHARP),
                                                Container(height=800, width=600, bgcolor=blue, border_radius=20,
                                                          content=Column(controls=[Text(meal, size=15)], scroll=True,
                                                                         height=800, width=600))]))
    )

    # Chat messages
    chat = ListView(
        expand=True,
        spacing=10,
        auto_scroll=True,
    )

    # A new message entry form
    new_message = TextField(
        hint_text="Write a message...",
        autofocus=True,
        shift_enter=True,
        min_lines=1,
        max_lines=5,
        filled=True,
        expand=True,
        on_submit=send_message_click,
    )

    join_user_name = TextField(
        label="Enter your name to join the chat",
        autofocus=True,
        on_submit=join_chat_click,
    )
    dialog = AlertDialog(
        open=True,
        modal=True,
        title=Text("Welcome!"),
        content=Column([join_user_name], width=300, height=70, tight=True),
        actions=[ElevatedButton(text="Join chat", on_click=join_chat_click)],
        actions_alignment="end",
    )

    messageBox = Row(
        controls=[FloatingActionButton(icon=icons.FULLSCREEN_EXIT_SHARP, on_click=lambda _: page.go('/')),
                  Container(
                      content=Column(controls=[chat, Row(
                          [
                              new_message,
                              IconButton(
                                  icon=ft.icons.SEND_ROUNDED,
                                  tooltip="Send message",
                                  on_click=send_message_click,
                              ),
                          ]
                      )]),
                      border=border.all(1, ft.colors.OUTLINE),
                      border_radius=5,
                      padding=10,
                      expand=True,
                      height=775,
                      width=650,
                  )])

    pages = {
        '/': View(
            "/",
            [
                container
            ],

        ),
        '/create_task': View(
            "/create_task",
            [
                create_task_view
            ]
        ),
        '/food_detect': View(
            "/create_task",
            [
                calorieCalc
            ]
        ),
        '/messageBox': View("/messageBox", [messageBox]),
        '/meal': View("/meal", [meal_plan]),
        '/addTask': View("/addTask",[taskAdder()[0]])

    }

    def submit(e: ControlEvent) -> None:
        print('Username', username.value)
        print('Password', password.value)
        page.clean()
        page.add(container)
        userNames.append(username.value)
        passWords.append(password.value)
        fileParse = open("Username&Passwords.txt", "w")
        for i in range(len(userNames)):
            fileParse.write(userNames[i] + " " + passWords[i] + "\n")
        fileParse.close()

    submitButton.on_click = submit
    page.pubsub.subscribe(on_message)

    page.add(Row(controls=[Column([username, password, signUp, submitButton])], alignment=ft.MainAxisAlignment.CENTER))


if __name__ == '__main__':
    ft.app(target=main)
