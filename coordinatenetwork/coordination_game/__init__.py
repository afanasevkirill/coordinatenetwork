from otree.api import *
import random
from statistics import multimode

def eval_options(code):
    mapping = {1:"абсолютно не согласен",
               2: "скорее не согласен",
                3: "затрудняюсь ответить",
                4: "скорее согласен",
               5: "абсолютно согласен",
               0: "Отказ от ответа"
               }
    return mapping[code]

decisions = {'engagement_1': 'Я всегда стараюсь защитить этот город и его окружающую среду от любого вреда.',
            'engagement_2': 'Я всегда энергично работаю над улучшением этого города и его окружающей среды, насколько это возможно.',
             'ee_1': 'Жители этого города вкладывают много энергии в совместную работу — как городское сообщество — над улучшением города и его окружающей среды.',
             'ee_2': 'Жители этого города очень стараются работать вместе — как городское сообщество — для защиты города и его окружающей среды.',
             'ident_1': 'Я чувствую сильную связь с этим городом или привязанность к нему.',
             'ident_2': 'Я твердо чувствую себя обязанным городу.',
             'ident_3': 'Я продолжу жить в городе в обозримом будущем.',
             'nature': 'Я чувствую сильную связь или привязанность к окружающей среде.',
             'pnb_1': 'Я считаю, что жители города должны вкладывать много энергии в совместную — как сообщество — над улучшением города и его окружающей среды.',
             'pnb_2': 'Я считаю, что жители города должны очень стараться работать вместе — как сообщество — для защиты города и его окружающей среды.',
             'ne_1': '''Предыдущие участники, так же как и вы, отмечали насколько они согласны со следующим утверждением: "Я считаю, что жители города должны вкладывать много энергии в совместную — как сообщество — над улучшением города и его окружающей среды". Выберите вариант ответа, который, как вам кажется, предыдущие участники эксперимента выбирали чаще всего.''',
                'ne_2': '''Предыдущие участники, так же как и вы, отмечали насколько они согласны со следующим утверждением: "Я считаю, что жители города должны очень стараться работать вместе — как сообщество — для защиты города и его окружающей среды." Выберите вариант ответа, который, как вам кажется, предыдущие участники эксперимента выбирали чаще всего. ''',


                                                          }


class C(BaseConstants):
    NAME_IN_URL = 'coordination_game'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    PRIZE = cu(250)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):
    random_decision = models.StringField()
    mode_answer = models.StringField()

    def set_payoff(self):
        self.random_decision = random.choice(['ne_1', 'ne_2'])
        list_of_decisions = eval(f'[p.field_maybe_none("{self.random_decision}") for p in self.subsession.get_players()]')
        mode_answers_list = multimode([x for x in list_of_decisions if x is not None])
        self.mode_answer = ', '.join([eval_options(item) for item in mode_answers_list])
        if eval(f'self.{self.random_decision}') in mode_answers_list:
            self.payoff = C.PRIZE
        else:
            self.payoff = cu(50)

    def make_field(label):
        return models.IntegerField(
            choices=[
                [1, 'абсолютно не согласен'],
                [2, 'скорее не согласен'],
                [3, 'затрудняюсь ответить'],
                [4, 'скорее согласен'],
                [5, 'абсолютно согласен'],
            ],
            widget=widgets.RadioSelect,
            label=label
        )

    city = models.StringField(
        label='В каком городе вы в данный момент постоянно проживаете?')
    engagement_1 = make_field(decisions['engagement_1'])
    engagement_2 = make_field(decisions['engagement_2'])
    ee_1 = make_field(decisions['ee_1'])
    ee_2 = make_field(decisions['ee_2'])
    ident_1 = make_field(decisions['ident_1'])
    ident_2 = make_field(decisions['ident_2'])
    ident_3 = make_field(decisions['ident_3'])
    nature = make_field(decisions['nature'])
    pnb_1 = make_field(decisions['pnb_1'])
    pnb_2 = make_field(decisions['pnb_2'])
    ne_1 = make_field(decisions['ne_1'])
    ne_2 = make_field(decisions['ne_2'])



# FUNCTIONS
# PAGES

class Introduction(Page):
    form_model = 'player'
    form_fields = []

class Rating1(Page):
    form_model = "player"
    form_fields = ['engagement_1','engagement_2', 'ee_1', 'ee_2', 'ident_1', 'ident_2', 'ident_3', 'nature', 'pnb_1', 'pnb_2']

class Rating2(Page):
    form_model = "player"
    timeout_seconds = 120
    form_fields = ['ne_1', 'ne_2']

    def before_next_page(player: Player, timeout_happened):
        player.set_payoff()


class Results(Page):
    def vars_for_template(self):
        decision_to_pay = decisions[self.random_decision]
        persons_answer = eval_options(eval(f"self.{self.random_decision}"))
        if self.payoff == C.PRIZE:
            result = f'''Ваш ответ: "{persons_answer}" совпал с модальным.'''
        else:
            result = f'''Ваш ответ: "{persons_answer}" не совпал с модальным. Модальный ответ: {self.mode_answer}'''
        return dict(
            decision_to_pay=decision_to_pay,
            result=result
        )


page_sequence = [Introduction,
                 Rating1,
                 Rating2,
                Results
]
