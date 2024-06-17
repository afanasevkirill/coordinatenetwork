from otree.api import *

class C(BaseConstants):
    NAME_IN_URL = 'survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


def make_test_curr():
    return models.CurrencyField(verbose_name='', choices = [
    [0, 0],
    [50, 50],
    [100, 100],
    [150, 150],
    [200, 200],
    [250, 250]
], widget=widgets.RadioSelect)


def make_test_bool(false_opt, true_opt):
    return eval(f'''models.BooleanField(
        choices=[
            [False, "{false_opt}"],
            [True, "{true_opt}"],
        ]
    )''')


class Player(BasePlayer):
    age = models.IntegerField(label='Укажите год своего рождения:', min=1920, max=2015)
    gender = models.StringField(choices=[['female', 'Женщина'], ['male', 'Мужчина'],
                                         ],
                                label='Ваш пол:', widget=widgets.RadioSelect)
    birth = models.StringField(
        label='В каком регионе Вы родились?')
    childhood = models.StringField(
        label='В каком регионе Вы провели большую часть детства? Если вы провели большую часть детства не в России, пожалуйста, укажите название страны.')

    work_field = models.StringField(choices=[['Не работаю', 'Не работаю'],
                                             ['Специалист c высшим образованием',
                                              'Специалист c высшим образованием – такой, например, как врач, преподаватель, инженер, художник, юрист'],
                                             ['Руководитель высшего звена',
                                              'Руководитель высшего звена - такой, например, как финансовый директор, исполнительный директор крупного предприятия, руководитель высшего звена в органах государственной власти, местного самоуправления или профсоюзов'],
                                             ['Офисный работник',
                                              'Офисный работник - такой, например, как секретарь, офисный служащий, офис-менеджер, бухгалтер'],
                                             ['Работник в сфере торговли или продаж',
                                              'Работник в сфере торговли или продаж - такой, например, как менеджер по сбыту, владелец магазина, продавец, страховой агент'],
                                             ['Квалифицированный сотрудник в сфере услуг',
                                              'Квалифицированный сотрудник в сфере услуг - такой, например, как сотрудник милиции, официант/ бармен, парикмахер, военнослужащий без офицерского звания, медсестра '],
                                             ['Рабочий высокой квалификации или руководитель бригады рабочих',
                                              'Рабочий высокой квалификации или руководитель бригады рабочих - такой, например, как мастер, прораб, автомеханик, монтажник, наборщик/ печатник, инструментальщик, электрик'],
                                             ['Рабочий средней квалификации',
                                              'Рабочий средней квалификации - такой например, каккаменщик, водитель, плотник/ столяр, жестянщик, пекарь '],
                                             ['Неквалифицированный рабочий',
                                              'Неквалифицированный рабочий - такой, например, как чернорабочий, грузчик, сторож'],
                                             ['Работник в сельском хозяйстве',
                                              'Работник в сельском хозяйстве – например, тракторист/ комбайнер, рыболов, доярка'],
                                             ['Фермер, управляющий фермой ', 'Фермер, управляющий фермой'],
                                             ['Другая область', 'Другая область']],
                                    label='В какой области Вы работаете?', widget=widgets.RadioSelect)

    study_field = models.StringField(
        choices=[['Не учусь', 'Не учусь'], ['Экономика и управление', 'Экономика и управление'],
                 ['Инженерное дело, технологии и технические науки',
                  'Инженерное дело, технологии и технические науки'],
                 ['Здравоохранение и медицинские науки',
                  'Здравоохранение и медицинские науки'],
                 ['Образование и педагогические науки',
                  'Образование и педагогические науки'],
                 ['Искусство и культура', 'Искусство и культура'],
                 ['Социология, психология и философия',
                  'Социология, психология и философия'],
                 ['Юриспруденция', 'Юриспруденция'],
                 ['Политические науки и регионоведение',
                  'Политические науки и регионоведение'],
                 ['Языкознание и литературоведение', 'Языкознание и литературоведение'],
                 ['История и археология', 'История и археология'],
                 ['Другая область', 'Другая область']],
        label='В какой области Вы учитесь?', widget=widgets.RadioSelect)

    education = models.StringField(
        choices=[['Среднее общее образование', 'Среднее общее образование (11 классов)'],
                 ['Среднее профессиональное образование (техникум, колледж)',
                  'Среднее профессиональное образование (техникум, колледж)'],
                 ['Я сейчас студент бакалавриата', 'Я сейчас студент бакалавриата'],
                 ['Высшее образование - бакалавриат', 'Высшее образование - бакалавриат'],
                 ['Высшее образование - специалитет, магистратура', 'Высшее образование - специалитет, магистратура'],
                 ['Высшее образование - подготовка кадров высшей квалификации',
                  'Высшее образование - подготовка кадров высшей квалификации']],
        label='Ваш наивысший достигнутый уровень образования', widget=widgets.RadioSelect)

    # education = models.StringField(
    #     choices=[['Учусь в школе', 'Учусь в школе'],
    #              ['Учусь в университете (бакалавриат или специалитет)', 'Учусь в университете (бакалавриат или специалитет)'],
    #              ['Учусь в университете (магистратура)', 'Учусь в университете (магистратура)'],
    #              # ['Незаконченное высшее образование - бакалавриат', 'Незаконченное высшее образование - бакалавриат'],
    #              ['Высшее образование - бакалавриат', 'Высшее образование - бакалавриат'],
    #              ['Высшее образование - специалитет, магистратура', 'Высшее образование - специалитет, магистратура'],
    #              ['Высшее образование - подготовка кадров высшей квалификаци',
    #               'Высшее образование - подготовка кадров высшей квалификаци']],
    #     label='Укажите ваш статус', widget=widgets.RadioSelect)

    risk = models.StringField(choices=[['Мне нравится рисковать', 'Мне нравится рисковать'],
                                       ['Мне скорее нравится рисковать', 'Мне скорее нравится рисковать'],
                                       ['Нейтрально', 'Нейтрально'],
                                       ['Я скорее избегаю риска', 'Я скорее избегаю риска'],
                                       ['Я избегаю риска', 'Я избегаю риска']],
                              label='Как Вы относитесь к риску?',
                              widget=widgets.RadioSelect)
    # income = models.IntegerField(
    #     label="Представьте шкалу дохода, где 1 означает принадлежность к группе с самым низким доходом, 10 - к группе "
    #           "с самым высоким доходом в стране. Укажите, к какой группе принадлежит ваше домохозяйство. Пожалуйста, учтите "
    #           "все зарплаты, пенсионные выплаты и другие доходы",
    #     widget=widgets.RadioSelectHorizontal,
    #     choices=[[1, "1"], [2, "2"], [3, "3"], [4, "4"], [5, "5"], [6, "6"], [7, "7"], [8, "8"], [9, "9"], [10, "10"]]
    # )
    income = models.IntegerField(
        label="Какое утверждение лучше всего характеризует вашу финансовую ситуацию. Пожалуйста, отметьте свою позицию на шкале, где 1 означает «Денег не хватает для выживания», а "
              "10 означает «Я могу позволить себе все расходы в любой момент времени»",
        widget=widgets.RadioSelectHorizontal,
        choices=[[1, "1"], [2, "2"], [3, "3"], [4, "4"], [5, "5"], [6, "6"], [7, "7"], [8, "8"], [9, "9"], [10, "10"]]
    )
    # income = models.IntegerField(
    #     label="Представьте шкалу дохода, где 1 означает принадлежность к группе с самым низким доходом, 10 - к группе "
    #           "с самым высоким доходом в стране. Укажите, к какой группе принадлежит ваше домохозяйство. Пожалуйста, учтите "
    #           "все зарплаты, пенсионные выплаты и другие доходы",
    #     widget=widgets.RadioSelectHorizontal,
    #     choices=[[1, "1"], [2, "2"], [3, "3"], [4, "4"], [5, "5"], [6, "6"], [7, "7"], [8, "8"], [9, "9"], [10, "10"]]
    # )
    life_satisfaction = models.IntegerField(
        label="Учитывая все обстоятельства, насколько вы удовлетворены своей жизнью в целом? "
              "Пожалуйста, отметьте свою позицию на шкале, где 1 означает «совершенно неудовлетворён», а "
              "10 означает «полностью удовлетворён»",
        widget=widgets.RadioSelectHorizontal,
        choices=[[1, "1"], [2, "2"], [3, "3"], [4, "4"], [5, "5"], [6, "6"], [7, "7"], [8, "8"], [9, "9"], [10, "10"]]
    )
    trust = models.IntegerField(
        label="Как Вы считаете в целом - можно ли доверять большинству людей, или при общении с другими людьми "
              "никогда не помешает осторожность? Пожалуйста, отметьте свою позицию на шкале, где 1 означает «Нужно "
              "быть максимально осторожным в вопросе доверия к другим людям», а 10 означает «Большинству людей можно "
              "полностью доверять»",
        widget=widgets.RadioSelectHorizontal,
        choices=[[1, "1"], [2, "2"], [3, "3"], [4, "4"], [5, "5"], [6, "6"], [7, "7"], [8, "8"], [9, "9"], [10, "10"]])
    freedom_of_choice = models.IntegerField(
        label="Часть людей чувствует, что они имеют полную свободу выбора и полный контроль над своими жизнями, "
              "когда как другие люди чувствуют, что их действия не имеют реального влияния на то, что происходит с ними. "
              "В какой степени это характерно для вас? Пожалуйста, отметьте свою позицию на шкале, где 1 означает «Я не имею свободы выбора», а "
              "10 означает «Я имею полную свободу выбора»",
        widget=widgets.RadioSelectHorizontal,
        choices=[[1, "1"], [2, "2"], [3, "3"], [4, "4"], [5, "5"], [6, "6"], [7, "7"], [8, "8"], [9, "9"], [10, "10"]])


    feedback = models.LongStringField(
        label="Здесь Вы можете оставить свои комментарии и поделиться впечатлениями от участия в эксперименте (если Вы не хотите что-либо писать, просто поставьте прочерк):"
        )

    # wealth = models.IntegerField(
    #     label="Представьте шкалу дохода, где 1 означает принадлежность к группе с самым низким доходом, 10 - к группе "
    #           "с самым высоким доходом в стране. Укажите, к какой группе принадлежит ваше домохозяйство. Пожалуйста, учтите "
    #           "все зарплаты, пенсионные выплаты и другие доходы",
    #     widget=widgets.RadioSelectHorizontal,
    #     choices=[[1, "1"], [2, "2"], [3, "3"], [4, "4"], [5, "5"], [6, "6"], [7, "7"], [8, "8"], [9, "9"], [10, "10"]]
    # )

#
# religion = models.StringField(choices=[['Атеизм или Агностицизм', 'Атеизм и Агностицизм (не верите в бога или что '
#                                                                   'знания о его существовании достижимы)'],
#                                        ['Христианство', 'Христианство'],
#                                        ['Ислам', 'Ислам'],
#                                        ['Иудаизм', 'Иудаизм'],
#                                        ['Буддизм', 'Буддизм'],
#                                        ['Этнические религии (язычество)', 'Этнические религии (язычество)'],
#                                        ['Другое', 'Другое']],
#                               label='Ваше вероисповедание:',
#                               widget=widgets.RadioSelect)
# worship = models.StringField(choices=[['Раз в неделю', 'Раз в неделю'],
#                                       ['Чаще раза в неделю', 'Чаще раза в неделю'],
#                                       ['Раз в месяц', 'Раз в месяц'],
#                                       ['На Рождество/Пасху', 'На Рождество/Пасху'],
#                                       ['В другие религиозные праздники', 'В другие религиозные праздники'],
#                                       ['Раз в год', 'Раз в год'],
#                                       ['Гораздо реже, чем представленные опции',
#                                        'Гораздо реже, чем представленные опции'],
#                                       ['Никогда/практически никогда', 'Никогда/практически никогда']],
#                              label='Как часто Вы посещаете религиозную службу? (не считая свадеб, похорон, крещений)',
#                              widget=widgets.RadioSelect)



class Survey(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'birth', 'childhood', 'work_field', 'study_field', 'education', 'risk', 'income', 'life_satisfaction', 'trust', 'freedom_of_choice', 'feedback']


page_sequence = [Survey]


