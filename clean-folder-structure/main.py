"""
The main entrypoint of the writer app
"""

import time

import writer as wf

initial_state = wf.init_state(
    {
        "my_app": {"title": "EXAMPLE APP"},
        "button1_pressed_message": "",
        "button2_pressed_message": "",
    }
)


def button1_pressed(state):
    state["button1_pressed_message"] = "You pressed button 1"
    time.sleep(2)
    state["button1_pressed_message"] = ""


def button2_pressed(state):
    state["button2_pressed_message"] = "You pressed button 2"
    time.sleep(2)
    state["button2_pressed_message"] = ""
