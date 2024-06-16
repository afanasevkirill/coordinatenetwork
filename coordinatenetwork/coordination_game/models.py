from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import random
from statistics import multimode

def eval_options(code):
    mapping = {-2:"Социально неприемлемо",
               -1: "Скорее социально неприемлемо",
                1: "Скорее социально приемлемо",
                2: "Социально приемлемо",
               0: "Отказ от ответа"
               }
    return mapping[code]


decisions = {'eval_not_demand': 'Участник Б ничего не запросил у участника А. Оцените поведение участника Б.',
          'eval_demand': 'Участник Б запросил у участника А 15 очков из положенных 25 очков. Оцените поведение участника Б.',
          'eval_pay': 'Участник А согласился отдавать участнику Б 15 запрошенных очков. Оцените поведение участника А.',
          'eval_not_pay': 'Участник А отказался отдавать участнику Б 15 запрошенных очков. Оцените поведение участника А.',
          'eval_punish_B': 'Участник Б запросил часть вознаграждения у участника А. Наблюдая это, участник В уменьшает выигрыш участника Б на 5 очков. Оцените поведение участника В.',
          'eval_not_punish_B': 'Участник Б запросил часть вознаграждения у участника А. Наблюдая это, участник В не уменьшает выигрыш участника Б. Оцените поведение участника В.',
          'eval_punish_A': 'Участник А соглашается отдать часть приза участнику Б. Наблюдая это, участник В уменьшает выигрыш участника А на 5 очков. Оцените поведение участника В.',
          'eval_not_punish_A': 'Участник А соглашается отдать часть приза участнику Б. Наблюдая это, участник В не уменьшает выигрыш участника А на 5 очков. Оцените поведение участника В.',
                                                          }


author = 'Sofya'

doc = """
Your app description
"""

class Constants(BaseConstants):
    name_in_url = 'coordination_game'
    players_per_group = None
    num_rounds = 1
    prize = c(25)



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    random_decision = models.StringField()
    mode_answer = models.StringField()

    def set_payoff(self):
        self.random_decision = random.choice(['eval_not_demand', 'eval_demand', 'eval_pay', 'eval_not_pay'])
        list_of_decisions = eval(f'[p.{self.random_decision} for p in self.get_players()]')
        mode_answers_list = multimode(list_of_decisions)
        self.mode_answer = ', '.join([eval_options(item) for item in mode_answers_list])
        for p in self.get_players():
            if eval(f'p.{self.random_decision}') in mode_answers_list:
                p.payoff = Constants.prize
            else:
                p.payoff = 0

class Player(BasePlayer):
    training_answer = models.CurrencyField(verbose_name='Вы заработаете')

    def make_field(label):
        return models.IntegerField(
            choices=[
                [-2, 'Социально неприемлемо'],
                [-1, 'Скорее социально неприемлемо'],
                [1, 'Скорее социально приемлемо'],
                [2, 'Социально приемлемо'],
            ],
            label=label
        )


    eval_not_demand = make_field(decisions['eval_not_demand'])
    eval_demand = make_field(decisions['eval_demand'])
    eval_pay = make_field(decisions['eval_pay'])
    eval_not_pay = make_field(decisions['eval_not_pay'])

    eval_punish_B = make_field(decisions['eval_punish_B'])
    eval_not_punish_B = make_field(decisions['eval_not_punish_B'])
    eval_punish_A = make_field(decisions['eval_punish_A'])
    eval_not_punish_A = make_field(decisions['eval_not_punish_A'])

