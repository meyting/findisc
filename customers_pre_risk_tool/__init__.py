from otree.api import *


doc = """
Your app description
"""

class C(BaseConstants):
    NAME_IN_URL = 'c1'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    budget = "10.000"
    Anlagehorizont = 10


class Subsession(BaseSubsession):
    pass

def creating_session(subsession: Subsession):
    pass
    #import itertools
    #suggestion = itertools.cycle(['expertsuggestion', 'laymansuggestion'])
    #if subsession.round_number == 1:
    #    for p in subsession.get_players():
    #        if 'suggestion' in subsession.session.config:
    #            p.participant.suggestion = subsession.session.config['suggestion']
    #        else:
    #            p.participant.suggestion = next(suggestion)



class Group(BaseGroup):
    pass


class Player(BasePlayer):
    consent = models.BooleanField()
    q1 = models.IntegerField()
    q2 = models.IntegerField()
    q3 = models.IntegerField()
    q4 = models.IntegerField()
    q5 = models.IntegerField()
 
    intro = models.LongStringField(blank=False,
                                   verbose_name='Bitte beschreiben Sie sich in 2-3 Sätzen. Gehen Sie dabei z.B. auf Ihre Hobbies, Interessen, Familie, etc. ein.')
    look = models.LongStringField(blank=False,
                                  verbose_name='Bitte beschreiben Sie Ihr Aussehen in 2-3 Sätzen. Gehen Sie dabei z.B. auf Ihre Haarfarbe, Augenfarbe, Größe, Brille(?), etc. ein.')

    prolific_id = models.StringField(default=str(" "))

    
# PAGES
class consent_en(Page):
    form_model = 'player'
    form_fields = ['consent']

    @staticmethod
    def before_next_page(self, timeout_happened):
        self.prolific_id = self.participant.label

class background_en(Page):
    pass

class risk_survey_en_2(Page):
    form_model = 'player'
    form_fields = ['q1','q2','q3','q4','q5']


class personal_en(Page):
    form_model = 'player'
    form_fields = ['intro', 'look']




page_sequence = [
    consent_en,
    personal_en,
    background_en,
    risk_survey_en_2,
                   ]
