from otree.api import *
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


class C(BaseConstants):
    NAME_IN_URL = 'coordination_game'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    PRIZE = cu(25)


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
                p.payoff = C.PRIZE
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

# FUNCTIONS
# PAGES



class Rating1(Page):
    form_model = "player"
    form_fields = ['eval_not_demand','eval_demand', 'eval_pay', 'eval_not_pay']

class Rating2(Page):
    form_model = "player"
    form_fields = ['eval_punish_B', 'eval_not_punish_B', 'eval_punish_A', 'eval_not_punish_A']


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoff()


class Results(Page):
    def vars_for_template(self):
        decision_to_pay = decisions[self.group.random_decision]
        persons_answer = eval_options(eval(f"self.{self.group.random_decision}"))
        if self.payoff == 25:
            result = f'''Ваш ответ: "{persons_answer}" совпал с модальным.'''
        else:
            result = f'''Ваш ответ: "{persons_answer}" не совпал с модальным. Модальный ответ: {self.group.mode_answer}'''
        return dict(
            decision_to_pay=decision_to_pay,
            result=result
        )


page_sequence = [
                 Rating1,
                 Rating2,
                 ResultsWaitPage,
                Results
]
