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
    NAME_IN_URL = 'c3'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    budget = 1000

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    lowerbound = models.IntegerField(blank=False,)
    upperbound = models.IntegerField(blank=False,)

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

    distract = models.CharField(initial = None,
                                verbose_name = 'Hand aufs Herz: Können wir Ihre Daten bedenkenlos analysieren oder waren Sie während der Umfrage durch irgendwelche Einflüsse abgelenkt? <i>(Die Antwort auf diese Frage hat keinerlei Auswirkungen auf Ihre Auszahlung.)</i>',
                                choices = [[1, 'Ich war sehr aufmerksam und gar nicht abgelenkt.'],
                                          [2, 'Ich war größtenteils aufmerksam und fast gar nicht abgelenkt.'],
                                          [3, 'Ich war eher nicht so aufmerksam, sondern etwas abgelenkt.'],
                                          [4, 'Ich war gar nicht aufmerksam, sondern ziemlich abgelenkt.']],)
    attention_check = models.CharField(
        initial=None,
        choices=[
            ['false1', 'blau'], ['true', 'orange'], ['false2', 'rot'], ['false3', 'gelb'], ['false4', 'grün'], ['false5', 'schwarz']
        ],
        label='Es ist wichtig für uns, dass sie aufmerksam sind. Bitte klicken Sie in der nachfolgenden Liste auf die zweite Option von oben.',
        widget=widgets.RadioSelect(),
    )

    easy = models.CharField(
        initial=None,
        choices=[
            [1, 'sehr einfach'], [2, 'eher einfach'], [3, 'eher schwierig'], [4, 'sehr schwierig']
        ],
        verbose_name='Wie einfach fanden Sie es, diese Umfrage auszufüllen?',
        widget=widgets.RadioSelect(),
    )    
    understood = models.CharField(
        initial=None,
        choices = [[1, 'Ich habe komplett verstanden, was gefragt war.'],
                   [2, 'Ich habe größtenteils verstanden, was gefragt war.'],
                   [3, 'Ich habe eher nicht verstanden, was gefragt war.'],
                   [4, 'Ich habe nicht verstanden, was gefragt war.']],
        verbose_name='Haben Sie vollständig verstanden, was von Ihnen verlangt wurde?',
        widget=widgets.RadioSelect(),
    )
    feedback = models.LongStringField(
        initial=None,
        label='Falls Sie noch weiteres Feedback zu dieser Umfrage haben, sagen Sie uns gerne hier Bescheid - vielen Dank!',
        blank=True,
    )
# PAGES

class risk_tool_accept_de2(Page):
    #@staticmethod
    #def vars_for_template(player: Player):
    #    suggestion = player.participant.suggestion
    #    return {
    #        'suggestion' : suggestion,
    #    }
    
    form_model = 'player'
    form_fields = ['lowerbound', 'upperbound']	



class personal_de(Page):
    form_model = 'player'
    form_fields = ['name','age', 'gender', 'profession', 'fieldofstudy', 'occupation', 'nationality', 'income', 'attention_check',
                   'education_school', 'education_uni','religion', 'party', 'distract', 'easy', 'understood', 'feedback']


class end_de(Page):
    pass



page_sequence = [
    risk_tool_accept_de2,
    personal_de,
    end_de
    
                 ]
