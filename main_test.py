import logging

from main import set_light_color


def test_color_red(caplog):
    caplog.set_level(logging.INFO)
    set_light_color("red")


def test_color_blue(caplog):
    caplog.set_level(logging.INFO)
    set_light_color("blue")

def test_color_white(caplog):
    caplog.set_level(logging.INFO)
    set_light_color("white")