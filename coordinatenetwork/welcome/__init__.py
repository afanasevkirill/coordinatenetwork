from otree.api import *
import numpy as np
import requests
import os

class C(BaseConstants):
    NAME_IN_URL = 'survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 5


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    phone_number = models.IntegerField(label='Введите ваш номер телефона без +7, напр. 9531122333', min=1000000000, max=9999999999)
    send_code = models.IntegerField()
    enter_code = models.IntegerField(label='Введите код из смс', min=1000,
                                       max=9999)
    result_sms_send= models.StringField()



# FUNCTIONS
# PAGES
class Introduction(Page):
    form_model = 'player'
    form_fields = ['phone_number']

    def is_displayed(player: Player):
        p = player.group.get_player_by_id(1)
        if player.round_number == 1:
            p.participant.auth_success = False
        else:
            pass
        auth_success = p.participant.auth_success
        return not auth_success

    def before_next_page(player: Player, timeout_happened):
        player.send_code = np.random.randint(low=1000, high=9999)
        url = 'https://api.exolve.ru/messaging/v1/SendSMS'
        data = dict(
            number="79681645172",
            destination=f'7{player.phone_number}',
            text=f'Ваш код проверки: {player.send_code}'
        )
        header = {"Authorization": os.getenv('EXOLVE_TOKEN')}
        sms_sender = requests.post(url, headers=header, json=data)
        player.result_sms_send = str(sms_sender)


class CheckCode(Page):
    form_model = 'player'
    form_fields = ['enter_code']

    def is_displayed(player: Player):
        p = player.group.get_player_by_id(1)
        auth_success = p.participant.auth_success
        return not auth_success

    def before_next_page(player: Player, timeout_happened):
        if player.enter_code == player.send_code:
            p = player.group.get_player_by_id(1)
            p.participant.auth_success = True




page_sequence = [Introduction, CheckCode]
