from otree.api import *


doc = """
Your app description
"""
import pandas as pd
choices = pd.read_excel('_static/global/choices.xlsx', engine = 'openpyxl') # can also index sheet by name or fetch all sheets
countries = choices['Land'][0:197].tolist()
years = choices['Jahr'][0:101].tolist()
years = [int(year) for year in years]
nationalities = choices['Nationalität'][0:199].tolist()


class C(BaseConstants):
    NAME_IN_URL = 'c1'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    budget = "10.000"
    Anlagehorizont = 10


class Subsession(BaseSubsession):
    pass

def creating_session(subsession: Subsession):
    import itertools
    suggestion = itertools.cycle(['expertsuggestion', 'laymnsuggestion'])
    if subsession.round_number == 1:
        for p in subsession.get_players():
            if 'suggestion' in subsession.session.config:
                p.participant.suggestion = subsession.session.config['suggestion']
            else:
                p.participant.suggestion = next(suggestion)



class Group(BaseGroup):
    pass


class Player(BasePlayer):
    consent = models.BooleanField()
    q1 = models.IntegerField()
    q2 = models.IntegerField()
    q3 = models.IntegerField()
    q4 = models.IntegerField()
    q5 = models.IntegerField()
    name = models.CharField(blank=True,
                            initial=None,
                            verbose_name='Wie lautet Ihr erster Vorname?')
    age = models.IntegerField(verbose_name='Wie alt sind Sie?')
    gender = models.CharField(initial=None,
                              choices=['weiblich', 'männlich', 'nicht-binär'],
                              verbose_name='Was ist ihr Geschlecht?',
                              widget=widgets.RadioSelect())
    nationality = models.CharField(initial=None,
                                    choices=nationalities,
                                    verbose_name='Was ist ihre Nationalität? <br> <i>(Falls Sie mehrere Nationalitäten haben, geben Sie bitte die Nationalität an, mit der Sie sich am meisten identifizieren.)</i>')

#    currentcountry = models.CharField(initial=None,
#                                        verbose_name='In welchem Land wohnen Sie aktuell?',
#                                        choices = countries,)
#    currentcountry_duration = models.IntegerField(initial=None,
#                                        verbose_name='Seit welchem Jahr wohnen Sie schon in diesem Land?',
#                                        choices = years,)
    education_school = models.CharField(initial=None,
                                        verbose_name='Was ist Ihr höchster Schulabschluss?',
                                        choices = ['(noch) kein Schulabschluss', 'Volks-/Hauptschulabschluss',
                                                   'Realschule (Mittlere Reife)', 'Fachhochschulreife', 'Gymnasium (Abitur)',
                                                   'Sonstiger Bildungsabschluss'],)
    education_uni =  models.CharField(initial=None,
                                      verbose_name='Was ist Ihr höchster Universität- oder Fachhochschulabschluss?',
                                      choices=['Bachelor', 'Master', 'Diplom', 'Magister', 'Promotion', '1. Staatsexamen',
                                               '2. Staatsexamen', '(noch) kein Uni- oder FH-Abschluss', 'Sonstiges'],)
    fieldofstudy = models.CharField(initial=None,
                                    blank = True,
                                    verbose_name='Was studieren Sie?',
                                    )
    income = models.CharField(initial=None,
                                    blank = True,
                                    verbose_name='Wie hoch ist ihr monatliches Einkommen?',
                                    choices = ['weniger als 1000€', '1000-1999€', '2000-2999€', '3000-3999€', 'mehr als 4000€']
                                    )
    occupation=models.IntegerField(initial=None)
    profession = models.CharField(initial = None,
                                  blank = True,
                                  verbose_name='Was ist ihr Beruf?')

    religion = models.CharField(initial = None,
                                verbose_name = 'Zu welcher Religionsgruppe fühlen Sie sich zugehörig?',
                                choices = ['Katholiken', 'Protestanten', 'Orthodoxen',
                                           'nicht gläubig', 'Moslem', 'Buddhisten', 'Juden',
                                           'Hindu', 'Sonstiges'],)
    party = models.CharField(initial = None,
                                verbose_name = 'Welche Partei würden Sie wählen, wenn heute Bundestagswahl wäre?',
                                choices = ['CDU/CSU', 'SPD', 'Grüne', 'FDP', 'Linke', 'AFD', 'weiß nicht', 'Sonstiges', 'bin Nichtwähler'],)
    intro = models.LongStringField(blank=False,
                                   verbose_name='Bitte beschreiben Sie sich in 2-3 Sätzen. Gehen Sie dabei z.B. auf Ihre Hobbies, Interessen, Familie, etc. ein.')
    look = models.LongStringField(blank=False,
                                  verbose_name='Bitte beschreiben Sie Ihr Aussehen in 2-3 Sätzen. Gehen Sie dabei z.B. auf Ihre Haarfarbe, Augenfarbe, Größe, Brille(?), etc. ein.')


# PAGES
class consent_de(Page):
    form_model = 'player'
    form_fields = ['consent']
    
class background_de(Page):
    pass

class personal_de(Page):
    form_model = 'player'
    form_fields = ['name','age', 'gender', 'profession', 'fieldofstudy', 'occupation', 'nationality', 'income',
                   'education_school', 'education_uni','religion', 'party', 'intro', 'look']

class risk_survey_de_2(Page):
    form_model = 'player'
    form_fields = ['q1','q2','q3','q4','q5']


class bridge(Page):
    pass  



page_sequence = [
    consent_de,
    personal_de,
    background_de,
    risk_survey_de_2,
                   ]
