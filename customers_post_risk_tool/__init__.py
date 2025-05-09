from otree.api import *


doc = """
Your app description
"""

import pandas as pd
choices = pd.read_excel('_static/global/choices.xlsx', engine = 'openpyxl') # can also index sheet by name or fetch all sheets
countries = choices['country'][0:197].tolist()
years = choices['Jahr'][0:101].tolist()
years = [int(year) for year in years]
nationalities = choices['nationality'][0:199].tolist()

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
                            verbose_name='What is your first name?')
    age = models.IntegerField(verbose_name='How old are you?')
    gender = models.CharField(initial=None,
                              choices=['female', 'male', 'non-binary'],
                              verbose_name='What is your gender?',
                              widget=widgets.RadioSelect())
    nationality = models.CharField(initial=None,
                                    choices=nationalities,
                                    verbose_name='What is your nationality? <br> <i>(In case you have multiple nationalities, indicate the one you identify with the most.)</i>')

#    currentcountry = models.CharField(initial=None,
#                                        verbose_name='In welchem Land wohnen Sie aktuell?',
#                                        choices = countries,)
#    currentcountry_duration = models.IntegerField(initial=None,
#                                        verbose_name='Seit welchem Jahr wohnen Sie schon in diesem Land?',
#                                        choices = years,)

    education_uni =  models.CharField(initial=None,
                                      verbose_name='What is your highest level of education?',
                                      choices=['Bachelor', 'Master', 'PhD', 'None', 'Other'],)
    fieldofstudy = models.CharField(initial=None,
                                    blank = True,
                                    verbose_name='What do you study?',
                                    )
    income = models.CharField(initial=None,
                                    blank = True,
                                    verbose_name='What is your monthly net income?',
                                    choices = ['less than $1000', '$1000-$1999', '$2000-$2999', '$3000-$3999', 'more than $4000']
                                    )
    occupation=models.IntegerField(initial=None)
    profession = models.CharField(initial = None,
                                  blank = True,
                                  verbose_name='What is your profession?')

    religion = models.CharField(initial = None,
                                verbose_name = 'Which religious group do you identify with?',
                                choices = ['Catholic', 'Protestant', 'Orthodox',
                                           'Not religious', 'Muslim', 'Buddhist', 'Jewish',
                                           'Hindu', 'Other'],)
    party = models.CharField(initial = None,
                                verbose_name = 'Which political party would you vote for if there were elections today?',
                                choices = ['Democrats', 'Republicans', 'Independent', 'I dont vote'],)

    distract = models.CharField(initial = None,
                                verbose_name = 'Please tell us: Can we safely analyze your data, or were you distracted by any influences during the survey? <i>(Your answer to this question will have no impact on your payment.)</i>',
                                choices = [
                                    [1, 'I was very attentive and not distracted at all.'],
                                    [2, 'I was mostly attentive and barely distracted.'],
                                    [3, 'I was not very attentive and somewhat distracted.'],
                                    [4, 'I was not attentive at all and quite distracted.'],
                                    ],)
    attention_check = models.CharField(
        initial=None,
        choices=[
            ['false1', 'blue'], ['true', 'orange'], ['false2', 'red'], ['false3', 'yellow'], ['false4', 'green'], ['false5', 'black']
        ],
        label = 'It is important to us that you pay attention. Please click on the second option from the top in the following list.',
        widget=widgets.RadioSelect(),
    )

    easy = models.CharField(
        initial=None,
        choices=[
            [1, 'very simple'], [2, 'rather simple'], [3, 'rather difficult'], [4, 'very difficult']
        ],
        verbose_name='How easy did you find it to complete this survey?',
        widget=widgets.RadioSelect(),
    )    
    understood = models.CharField(
        initial=None,
        choices = [
            [1, 'I completely understood what was asked.'],
            [2, 'I mostly understood what was asked.'],
            [3, 'I didn’t fully understand what was asked.'],
            [4, 'I didn’t understand what was asked at all.']
            ],
        verbose_name = 'Did you fully understand what was required of you?',
        widget = widgets.RadioSelect(),)

    feedback = models.LongStringField(
        initial=None,
        label='If you have any further feedback about this survey, please let us know here – thank you!',
        blank=True,
    )
    selected_finpart = models.CharField(blank=True)
# PAGES

class risk_tool_accept_en2(Page):
    #@staticmethod
    #def vars_for_template(player: Player):
    #    suggestion = player.participant.suggestion
    #    return {
    #        'suggestion' : suggestion,
    #    }
    
    form_model = 'player'
    form_fields = ['lowerbound', 'upperbound']	



class personal_en(Page):
    form_model = 'player'
    form_fields = ['name','age', 'gender', 'profession', 'fieldofstudy', 'occupation', 'nationality', 'income', 'attention_check',
                   'education_uni','religion', 'party', 'distract', 'easy', 'understood', 'feedback','selected_finpart']


class end_en(Page):
    pass



page_sequence = [
    risk_tool_accept_en2,
    personal_en,
    end_en
    
                 ]
