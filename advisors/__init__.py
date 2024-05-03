from otree.api import *


doc = """
Your app description
"""

import pandas as pd
import random

df = pd.read_excel('_static/global/clients.xlsx', keep_default_na=False, engine='openpyxl')
df["gender"] = df["gender"].astype(str)
df["nationality"] = df["nationality"].astype(str)
df["introduction"] = df["introduction"].astype(str)
df["age"] = df["age"].astype(int)
df["riskgroup"] = df["riskgroup"].astype(int)
df["riskgroup_text"] = df["riskgroup_text"].astype(str)
df["id"] = df["id"].astype(int)


choices = pd.read_excel('_static/global/choices.xlsx', engine = 'openpyxl') # can also index sheet by name or fetch all sheets
countries = choices['Land'][0:197].tolist()
years = choices['Jahr'][0:101].tolist()
years = [int(year) for year in years]
nationalities = choices['Nationalität'][0:199].tolist()

class C(BaseConstants):
    NAME_IN_URL = 'advisors'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 4
    bonus = cu(2)


class Subsession(BaseSubsession):
    pass

def creating_session(subsession: Subsession):
    import itertools
    variant_rt = itertools.cycle(['rt', 'nort'])
    if subsession.round_number == 1:
        for p in subsession.get_players():
            if 'variant_rt' in subsession.session.config:
                p.participant.variant_rt = subsession.session.config['variant_rt']
            else:
                p.participant.variant_rt = next(variant_rt)
            p.participant.profiles = []
            for i in range(0,C.NUM_ROUNDS+1):
                selected_profiles_df = df[df.id==i]
                print(i)
                profiles = selected_profiles_df.to_dict(orient='records')
                random.shuffle(profiles)
                p.participant.profiles.append(profiles)

            
class Group(BaseGroup):
    pass


class Player(BasePlayer):
    consent = models.BooleanField()
    riskgroup_example = models.IntegerField(blank=True)
    riskyshare_example = models.IntegerField(blank=True)
    riskgroup = models.IntegerField(blank=False)
    riskyshare = models.IntegerField(blank=False)
    offer = models.IntegerField()
    best_advice = models.IntegerField()	

    name = models.CharField(blank=True,
                            initial=None,
                            verbose_name='Wie lautet Ihr erster Vorname? (Ihre Antworten können trotz Angabe Ihres ersten Vornamens nicht auf Sie persönlich zurückgeführt werden!)')
    age = models.IntegerField(verbose_name='Wie alt sind Sie?')
    gender = models.CharField(initial=None,
                              choices=['weiblich', 'männlich', 'nicht-binär'],
                              verbose_name='Was ist ihr Geschlecht?',
                              widget=widgets.RadioSelect())
    nationality = models.CharField(initial=None,
                                    choices=nationalities,
                                    verbose_name='Was ist ihre Nationalität? (Falls Sie mehrere Nationalitäten haben, geben Sie bitte die Nationalität an, mit der Sie sich am meisten identifizieren.)')

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
    favmovie = models.CharField(initial = None,
                                verbose_name = "Was ist Ihr Lieblingsfilm?")
    
    q1 = models.IntegerField(blank=False)
    q2 = models.IntegerField(blank=False)
    q3 = models.IntegerField(blank=False)
    q4 = models.IntegerField(blank=False)
    q5 = models.IntegerField(blank=False)

# PAGES
class consent_de(Page):
    form_model = 'player'
    form_fields = ['consent']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1
    
class instructions_de(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class evaluation_example(Page):
    form_model = 'player'
    form_fields = ['riskgroup_example', 'riskyshare_example', 'offer', 'q1', 'q2', 'q3', 'q4', 'q5']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1
    
    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        profile = participant.profiles[player.round_number-1][0]
        gender = profile["gender"]
        name = profile["name"]
        nationality = profile["nationality"]
        introduction = profile["introduction"]
        age = profile["age"]
        id = profile["id"]
        return {
            'profile': profile,
            'id': id,
            'gender': gender,
            'nationality': nationality,
            'introduction': introduction,
            'age': age,
            'name':name,
        }

    @staticmethod
    def js_vars(player):
        participant = player.participant
        profile = participant.profiles[player.round_number-1][0]
        q1 = profile["q1"]
        q2 = profile["q2"]
        q3 = profile["q3"]
        q4 = profile["q4"]
        q5 = profile["q5"]
        return dict(
            q1= q1,
            q2= q2,
            q3= q3,
            q4= q4,
            q5= q5,
        )
    
class evaluation_example_2(Page):
    form_model = 'player'
    form_fields = ['riskyshare_example', 'offer', 'q1', 'q2', 'q3', 'q4', 'q5']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1
    
    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        profile = participant.profiles[player.round_number-1][0]
        gender = profile["gender"]
        name = profile["name"]
        nationality = profile["nationality"]
        introduction = profile["introduction"]
        riskgroup = profile["riskgroup"]
        riskgroup_text = profile["riskgroup_text"]
        age = profile["age"]
        id = profile["id"]
        return {
            'name':name,
            'profile': profile,
            'id': id,
            'gender': gender,
            'nationality': nationality,
            'introduction': introduction,
            'riskgroup': riskgroup,
            'riskgroup_text': riskgroup_text,
            'age': age,
        }
    
    @staticmethod
    def js_vars(player):
        participant = player.participant
        profile = participant.profiles[player.round_number-1][0]
        q1 = profile["q1"]
        q2 = profile["q2"]
        q3 = profile["q3"]
        q4 = profile["q4"]
        q5 = profile["q5"]
        return dict(
            q1= q1,
            q2= q2,
            q3= q3,
            q4= q4,
            q5= q5,
        )

class payment_instructions_de(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class explanations_rt_de(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1





class evaluation_de(Page):
    form_model = 'player'
    form_fields = ['riskgroup', 'riskyshare', 'offer', 'q1', 'q2', 'q3', 'q4', 'q5']

    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        print(participant.profiles)
        print(player.round_number)
        profile = participant.profiles[player.round_number][0]
        gender = profile["gender"]
        nationality = profile["nationality"]
        introduction = profile["introduction"]
        age = profile["age"]
        id = profile["id"]
        name = profile["name"]
        return {
            'name':name,
            'profile': profile,
            'id': id,
            'gender': gender,
            'nationality': nationality,
            'introduction': introduction,
            'age': age,
       }
    
    @staticmethod
    def js_vars(player):
        participant = player.participant
        profile = participant.profiles[player.round_number][0]
        q1 = profile["q1"]
        q2 = profile["q2"]
        q3 = profile["q3"]
        q4 = profile["q4"]
        q5 = profile["q5"]
        return dict(
            q1= q1,
            q2= q2,
            q3= q3,
            q4= q4,
            q5= q5,
        )





class evaluation_de_2(Page):
    form_model = 'player'
    form_fields = ['riskyshare', 'offer', 'q1', 'q2', 'q3', 'q4', 'q5']

    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        print(participant.profiles)
        print(player.round_number)
        profile = participant.profiles[player.round_number][0]
        gender = profile["gender"]
        nationality = profile["nationality"]
        name = profile["name"]
        introduction = profile["introduction"]
        riskgroup = profile["riskgroup"]
        riskgroup_text = profile["riskgroup_text"]
        age = profile["age"]
        id = profile["id"]
        return {
            'profile': profile,
            'id': id,
            'name':name,
            'gender': gender,
            'nationality': nationality,
            'introduction': introduction,
            'riskgroup': riskgroup,	
            'riskgroup_text': riskgroup_text,
            'age': age,
       }
    
    @staticmethod
    def js_vars(player):
        participant = player.participant
        profile = participant.profiles[player.round_number][0]
        q1 = profile["q1"]
        q2 = profile["q2"]
        q3 = profile["q3"]
        q4 = profile["q4"]
        q5 = profile["q5"]
        return dict(
            q1= q1,
            q2= q2,
            q3= q3,
            q4= q4,
            q5= q5,
        )






class payment_de(Page):
    form_model = 'player'
    form_fields = ['best_advice']

    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        print(participant.profiles)
        print(player.round_number)
        profile1 = participant.profiles[1][0]
        profile2 = participant.profiles[2][0]
        profile3 = participant.profiles[3][0]
        profile4 = participant.profiles[4][0]
        gender1 = profile1["gender"]
        nationality1 = profile1["nationality"]
        name1 = profile1["name"]
        introduction1 = profile1["introduction"]
        riskgroup1 = profile1["riskgroup"]
        riskgroup_text1 = profile1["riskgroup_text"]
        age1 = profile1["age"]
        id1 = profile1["id"]
        gender2 = profile2["gender"]
        nationality2 = profile2["nationality"]
        name2 = profile2["name"]
        introduction2 = profile2["introduction"]
        riskgroup2 = profile2["riskgroup"]
        riskgroup_text2 = profile2["riskgroup_text"]
        age2 = profile2["age"]
        id2 = profile2["id"]
        gender3 = profile3["gender"]
        nationality3 = profile3["nationality"]
        name3 = profile3["name"]
        introduction3 = profile3["introduction"]
        riskgroup3 = profile3["riskgroup"]
        riskgroup_text3 = profile3["riskgroup_text"]
        age3 = profile3["age"]
        id3 = profile3["id"]
        gender4 = profile4["gender"]
        nationality4 = profile4["nationality"]
        name4 = profile1["name"]
        introduction4 = profile4["introduction"]
        riskgroup4 = profile4["riskgroup"]
        riskgroup_text4 = profile4["riskgroup_text"]
        age4 = profile4["age"]
        id4 = profile4["id"]
        return {
            'gender1': gender1,
            'name1': name1,
            'nationality1': nationality1,
            'riskgroup1': riskgroup1,	
            'riskgroup_text1': riskgroup_text1,
            'age1': age1,
            'gender2': gender2,
            'name2': name2,
            'nationality2': nationality2,
            'riskgroup2': riskgroup2,	
            'riskgroup_text2': riskgroup_text2,
            'age2': age2,
            'gender3': gender3,
            'name3': name3,
            'nationality3': nationality3,
            'riskgroup3': riskgroup3,	
            'riskgroup_text3': riskgroup_text3,
            'age3': age3,
            'gender4': gender4,
            'name4': name4,
            'nationality4': nationality4,
            'riskgroup4': riskgroup4,	
            'riskgroup_text4': riskgroup_text4,
            'age4': age4,
            'advice1': player.in_round(1).riskyshare,
            'advice2': player.in_round(2).riskyshare,
            'advice3': player.in_round(3).riskyshare,
            'advice4': player.in_round(4).riskyshare
            }

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS
    
class groupy_de(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS

class iat_de(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS
    
class demos_de(Page):
    form_model = 'player'
    form_fields = ['name','age', 'gender', 'profession', 'fieldofstudy', 'occupation', 'nationality', 
                   'education_school', 'education_uni','religion', 'party', 'favmovie']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS
    
class end_de(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS

page_sequence = [
    consent_de,
    instructions_de,
    evaluation_example,
    evaluation_example_2,
    payment_instructions_de,
    explanations_rt_de,
    evaluation_de,
    evaluation_de_2,
    payment_de,
    groupy_de,
    iat_de,
    demos_de,
    end_de
                   ]
