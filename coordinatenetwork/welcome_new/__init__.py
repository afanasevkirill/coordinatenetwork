from otree.api import *
import numpy as np
import requests
import os

class C(BaseConstants):
    NAME_IN_URL = 'welcome_new'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass



# FUNCTIONS
# PAGES
class Introduction(Page):
    form_model = 'player'
    form_fields = []



page_sequence = [Introduction]
