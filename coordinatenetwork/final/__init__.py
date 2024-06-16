from otree.api import *
import numpy as np
import requests
import os

class C(BaseConstants):
    NAME_IN_URL = 'final'
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
class Final(Page):
    form_model = 'player'
    form_fields = []

    def vars_for_template(self):
        payoff = self.participant.payoff_plus_participation_fee()
        try:
            link = self.participant.recipient
        except:
            link = "Ошибка! Напишите организатору"
        friends_participated = 0
        for i in self.subsession.get_players():
            try:
                inviter = i.participant.inviter
            except:
                inviter = 0
            if f"https://t.me/behexpbot?start={inviter}" == link:
                friends_participated += 1

        return dict(
            link=link,
            friends_participated=friends_participated,
            payoff=payoff
        )


page_sequence = [Final]
