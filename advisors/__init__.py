from otree.api import *


doc = """
Your app description
"""

import pandas as pd
import random

df = pd.read_excel('_static/global/clients.xlsx', keep_default_na=False, engine='openpyxl')
df["gender"] = df["gender"].astype(str)
df["nationality"] = df["nationality"].astype(str)
df["religion"] = df["religion"].astype(str)
df["education_uni"] = df["education_uni"].astype(str)
df["education_school"] = df["education_school"].astype(str)
df["profession"] = df["profession"].astype(str)
df["introduction"] = df["introduction"].astype(str)
df["age"] = df["age"].astype(int)
df["riskgroup"] = df["riskgroup"].astype(int)
df["riskgroup_text"] = df["riskgroup_text"].astype(str)
df["prolificid_client"] = df["prolificid_client"].astype(str)
df["income"] = df["income"].astype(str)

df["q1_text"] = "Keine Antwort"
df.loc[(df.q1==1),"q1_text"] = "Der Erhalt meiner Kapitalanlage ist mir gar nicht wichtig."
df.loc[(df.q1==2),"q1_text"] = "Der Erhalt meiner Kapitalanlage ist mir eher nicht wichtig."
df.loc[(df.q1==3),"q1_text"] = "Der Erhalt meiner Kapitalanlage ist mir eher wichtig."
df.loc[(df.q1==4),"q1_text"] = "Der Erhalt meiner Kapitalanlage ist mir sehr wichtig."
df["q2_text"] = "Keine Antwort"
df.loc[(df.q2==1),"q2_text"] = "Um meinen Ertrag zu erhöhen ist mir viel wichtiger Risiken einzugehen, als eine zuverlässige Rendite zu bekommen."
df.loc[(df.q2==2),"q2_text"] = "Um meinen Ertrag zu erhöhen ist mir eher wichtiger Risiken einzugehen, als eine zuverlässige Rendite zu bekommen."
df.loc[(df.q2==3),"q2_text"] = "Um meinen Ertrag zu erhöhen ist mir eher wichtiger eine zuverlässige Rendite zu bekommen, als Risiken einzugehen."
df.loc[(df.q2==4),"q2_text"] = "Um meinen Ertrag zu erhöhen ist mir viel wichtiger eine zuverlässige Rendite zu bekommen, als Risiken einzugehen."
df["q3_text"] = "Keine Antwort"
df.loc[(df.q3==1),"q3_text"] = "Kleinste Verluste machen mich gar nicht nervös."
df.loc[(df.q3==2),"q3_text"] = "Kleinste Verluste machen mich eher nicht nervös."
df.loc[(df.q3==3),"q3_text"] = "Kleinste Verluste machen mich bereits etwas nervös."
df.loc[(df.q3==4),"q3_text"] = "Kleinste Verluste machen mich bereits sehr nervös."
df["q4_text"] = "Keine Antwort"
df.loc[(df.q4==1),"q4_text"] = "Finanzielle Risiken sind gar nicht reizvoll."
df.loc[(df.q4==2),"q4_text"] = "Finanzielle Risiken sind eher nicht reizvoll."
df.loc[(df.q4==3),"q4_text"] = "Finanzielle Risiken sind eher reizvoll."
df.loc[(df.q4==4),"q4_text"] = "Finanzielle Risiken sind sehr reizvoll."
df["q5_text"] = "Keine Antwort"
df.loc[(df.q5==1),"q5_text"] = "Ich nehme den Verlust meines Vermögens nicht in Kauf wenn ich gleichzeitig die Chance habe, meine Gewinne zu erhöhen."
df.loc[(df.q5==2),"q5_text"] = "Ich nehme den Verlust meines Vermögens eher nicht in Kauf wenn ich gleichzeitig die Chance habe, meine Gewinne zu erhöhen."
df.loc[(df.q5==3),"q5_text"] = "Ich nehme den Verlust meines Vermögens eher in Kauf wenn ich gleichzeitig die Chance habe, meine Gewinne zu erhöhen."
df.loc[(df.q5==4),"q5_text"] = "Ich nehme den Verlust meines Vermögens in Kauf wenn ich gleichzeitig die Chance habe, meine Gewinne zu erhöhen."

df["q1_short"] = "Keine Antwort"
df.loc[(df.q1==1),"q1_short"] = "gar nicht"
df.loc[(df.q1==2),"q1_short"] = "eher nicht"
df.loc[(df.q1==3),"q1_short"] = "eher"
df.loc[(df.q1==4),"q1_short"] = "voll und ganz"
df["q2_short"] = "Keine Antwort"
df.loc[(df.q2==1),"q2_short"] = "gar nicht"
df.loc[(df.q2==2),"q2_short"] = "eher nicht"
df.loc[(df.q2==3),"q2_short"] = "eher"
df.loc[(df.q2==4),"q2_short"] = "voll und ganz"
df["q3_short"] = "Keine Antwort"
df.loc[(df.q3==1),"q3_short"] = "gar nicht"
df.loc[(df.q3==2),"q3_short"] = "eher nicht"
df.loc[(df.q3==3),"q3_short"] = "eher"
df.loc[(df.q3==4),"q3_short"] = "voll und ganz"
df["q4_short"] = "Keine Antwort"
df.loc[(df.q4==1),"q4_short"] = "gar nicht"
df.loc[(df.q4==2),"q4_short"] = "eher nicht"
df.loc[(df.q4==3),"q4_short"] = "eher"
df.loc[(df.q4==4),"q4_short"] = "voll und ganz"
df["q5_short"] = "Keine Antwort"
df.loc[(df.q5==1),"q5_short"] = "gar nicht"
df.loc[(df.q5==2),"q5_short"] = "eher nicht"
df.loc[(df.q5==3),"q5_short"] = "eher"
df.loc[(df.q5==4),"q5_short"] = "voll und ganz"

choices = pd.read_excel('_static/global/choices.xlsx', engine = 'openpyxl') # can also index sheet by name or fetch all sheets
countries = choices['Land'][0:197].tolist()
years = choices['Jahr'][0:101].tolist()
years = [int(year) for year in years]
nationalities = choices['Nationalität'][0:199].tolist()

class C(BaseConstants):
    NAME_IN_URL = 'advisors'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 10
    bonus = cu(2)


class Subsession(BaseSubsession):
    pass

def select_unique_risky_shares(data, n):
    unique_risky_shares = data.drop_duplicates(subset=['riskyshare']).sample(n=n)
    return unique_risky_shares

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
            selected_profiles_df = select_unique_risky_shares(df, 11)
            profiles = selected_profiles_df.to_dict(orient='records')
            random.shuffle(profiles)
            p.participant.profiles = profiles

            
class Group(BaseGroup):
    pass


class Player(BasePlayer):
    consent = models.BooleanField()
    riskgroup_example = models.IntegerField(blank=True)
    advice_example = models.IntegerField(blank=True,
                                             choices=[
                                        [0, "0% Risikoanteil"],
                                        [10, "10% Risikoanteil"], 
                                        [20, "20% Risikoanteil"], 
                                        [30, "30% Risikoanteil"], 
                                        [40, "40% Risikoanteil"],
                                        [50, "50% Risikoanteil"], 
                                        [60, "60% Risikoanteil"], 
                                        [70, "70% Risikoanteil"], 
                                        [80, "80% Risikoanteil"], 
                                        [90, "90% Risikoanteil"],
                                        [100, "100% Risikoanteil"]],
                                        verbose_name="""""")
    advice_certainty_example = models.IntegerField(blank=True,
                                               choices=[[1, "sehr sicher"],
                                                        [2, "ziemlich sicher"],
                                                        [3, "ziemlich unsicher"], 
                                                        [4, "sehr unsicher"]],
                                        verbose_name="""""")
    riskgroup = models.IntegerField(blank=False)
    advice = models.IntegerField(choices=[
                                        [0, "0% Risikoanteil"],
                                        [10, "10% Risikoanteil"], 
                                        [20, "20% Risikoanteil"], 
                                        [30, "30% Risikoanteil"], 
                                        [40, "40% Risikoanteil"],
                                        [50, "50% Risikoanteil"], 
                                        [60, "60% Risikoanteil"], 
                                        [70, "70% Risikoanteil"], 
                                        [80, "80% Risikoanteil"], 
                                        [90, "90% Risikoanteil"],
                                        [100, "100% Risikoanteil"]
                                        ],
                                        verbose_name="""""")
    advice_certainty = models.IntegerField(blank=False,
                                               choices=[[1, "sehr sicher"],
                                                        [2, "ziemlich sicher"],
                                                        [3, "ziemlich unsicher"], 
                                                        [4, "sehr unsicher"]],
                                        verbose_name="""""")

    offer = models.IntegerField()
    best_advice = models.IntegerField(verbose_name="Bei welcher Empfehlung sind sich sich am sichersten? <br> <i>(Bitte geben Sie den Namen des jeweiligen Kunden bzw. der jeweiligen Kundin ein.)</i>")	

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
                                    verbose_name='Was ist ihre Nationalität? <br><i>(Falls Sie mehrere Nationalitäten haben, geben Sie bitte die Nationalität an, mit der Sie sich am meisten identifizieren.)</i>')

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
    
    q1_advisor = models.IntegerField(blank=False)
    q2_advisor = models.IntegerField(blank=False)
    q3_advisor = models.IntegerField(blank=False)
    q4_advisor = models.IntegerField(blank=False)
    q5_advisor = models.IntegerField(blank=False)

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

class risk_survey_de(Page):
    form_model = 'player'
    form_fields = ['q1_advisor', 'q2_advisor', 'q3_advisor', 'q4_advisor', 'q5_advisor']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1
'''
class evaluation_example_de(Page):
    form_model = 'player'
    form_fields = ['riskgroup_example', 'advice_example', 'offer', 'q1', 'q2', 'q3', 'q4', 'q5']

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
        religion = profile["religion"]
        profession = profile["profession"]
        income = profile["income"]
        education_school = profile["education_school"]
        education_uni = profile["education_uni"]
        introduction = profile["introduction"]
        age = profile["age"]
        q1_text = profile["q1_text"]
        q2_text = profile["q2_text"]
        q3_text = profile["q3_text"]
        q4_text = profile["q4_text"]
        q5_text = profile["q5_text"]
        id = profile["id"]
        idpic = profile["idpic"]
        return {
            'profile': profile,
            'id': id,
            'gender': gender,
            'nationality': nationality,
            'profession': profession,
            'q1_text': q1_text,
            'q2_text': q2_text,
            'q3_text': q3_text,
            'q4_text': q4_text,
            'q5_text': q5_text,
            'education_school': education_school,
            'education_uni': education_uni,
            'nationality': nationality,
            'religion': religion,
            'income': income,
            'introduction': introduction,
            'age': age,
            'name':name,
            'picpath': 'profilepics/' + idpic + '.JPG',
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
    
class evaluation_example_de_2(Page):
    form_model = 'player'
    form_fields = ['advice_example', 'offer', 'q1', 'q2', 'q3', 'q4', 'q5']

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
        religion = profile["religion"]
        profession = profile["profession"]
        education_school = profile["education_school"]
        income = profile["income"]
        q1_text = profile["q1_text"]
        q2_text = profile["q2_text"]
        q3_text = profile["q3_text"]
        q4_text = profile["q4_text"]
        q5_text = profile["q5_text"]
        education_uni = profile["education_uni"]
        introduction = profile["introduction"]
        riskgroup = profile["riskgroup"]
        riskgroup_text = profile["riskgroup_text"]
        age = profile["age"]
        id = profile["id"]
        idpic = profile["idpic"]
        return {
            'name':name,
            'profile': profile,
            'id': id,
            'q1_text': q1_text,
            'q2_text': q2_text,
            'q3_text': q3_text,
            'q4_text': q4_text,
            'q5_text': q5_text,
            'gender': gender,
            'nationality': nationality,
            'profession': profession,
            'education_school': education_school,
            'education_uni': education_uni,
            'income':income,
            'nationality': nationality,
            'religion': religion,
            'riskgroup': riskgroup,
            'riskgroup_text': riskgroup_text,
            'introduction': introduction,
            'age': age,
            'picpath': 'profilepics/' + idpic + '.JPG',
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
'''

class evaluation_example_de_3(Page):
    form_model = 'player'
    form_fields = ['advice_example', 'offer', 'advice_certainty_example']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1
    
    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        profile = participant.profiles[player.round_number-1]
        gender = profile["gender"]
        name = profile["name"]
        nationality = profile["nationality"]
        prolificid_client = profile["prolificid_client"]
        religion = profile["religion"]
        profession = profile["profession"]
        education_school = profile["education_school"]
        education_uni = profile["education_uni"]
        income = profile["income"]
        q1_text = profile["q1_text"]
        q2_text = profile["q2_text"]
        q3_text = profile["q3_text"]
        q4_text = profile["q4_text"]
        q5_text = profile["q5_text"]
        q1_short = profile["q1_short"]
        q2_short = profile["q2_short"]
        q3_short = profile["q3_short"]
        q4_short = profile["q4_short"]
        q5_short = profile["q5_short"]
        introduction = profile["introduction"]
        riskgroup = profile["riskgroup"]
        riskgroup_text = profile["riskgroup_text"]
        age = profile["age"]
        q1 = profile["q1"]
        q2 = profile["q2"]
        q3 = profile["q3"]
        q4 = profile["q4"]
        q5 = profile["q5"]
        return {
            'name':name,
            'profile': profile,
            'gender': gender,
            'prolificid_client': prolificid_client,
            'q1_text': q1_text,
            'q2_text': q2_text,
            'q3_text': q3_text,
            'q4_text': q4_text,
            'q5_text': q5_text,
            'q1_short': q1_short,
            'q2_short': q2_short,
            'q3_short': q3_short,
            'q4_short': q4_short,
            'q5_short': q5_short,
            'nationality': nationality,
            'profession': profession,
            'education_school': education_school,
            'education_uni': education_uni,
            'income':income,
            'nationality': nationality,
            'religion': religion,
            'riskgroup': riskgroup,
            'riskgroup_text': riskgroup_text,
            'introduction': introduction,
            'age': age,
            'picpath': 'profilepics/' + prolificid_client + '.JPG',
            'scalepath1': 'scales/scale' + str(q1) + '.png',
            'scalepath2': 'scales/scale' + str(q2) + '.png',
            'scalepath3': 'scales/scale' + str(q3) + '.png',
            'scalepath4': 'scales/scale' + str(q4) + '.png',
            'scalepath5': 'scales/scale' + str(q5) + '.png',
        }
    


class payment_instructions_de(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class explanations_rt_de(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

'''
class evaluation_de(Page):
    form_model = 'player'
    form_fields = ['riskgroup', 'advice', 'offer', 'q1', 'q2', 'q3', 'q4', 'q5']

    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        print(participant.profiles)
        print(player.round_number)
        profile = participant.profiles[player.round_number][0]
        gender = profile["gender"]
        nationality = profile["nationality"]
        introduction = profile["introduction"]
        religion = profile["religion"]
        profession = profile["profession"]
        education_school = profile["education_school"]
        income = profile["income"]
        q1_text = profile["q1_text"]
        q2_text = profile["q2_text"]
        q3_text = profile["q3_text"]
        q4_text = profile["q4_text"]
        q5_text = profile["q5_text"]
        education_uni = profile["education_uni"]
        age = profile["age"]
        id = profile["id"]
        idpic = profile["idpic"]
        name = profile["name"]
        return {
            'name':name,
            'profile': profile,
            'id': id,
            'gender': gender,
            'nationality': nationality,
            'introduction': introduction,
            'age': age,
            'q1_text': q1_text,
            'q2_text': q2_text,
            'q3_text': q3_text,
            'q4_text': q4_text,
            'q5_text': q5_text,
            'income': income,
            'profession': profession,
            'education_school': education_school,
            'education_uni': education_uni,
            'nationality': nationality,
            'religion': religion,
            'picpath': 'profilepics/' + idpic + '.JPG',
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
    form_fields = ['advice', 'offer', 'q1', 'q2', 'q3', 'q4', 'q5']

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
        religion = profile["religion"]
        profession = profile["profession"]
        income = profile["income"]
        q1_text = profile["q1_text"]
        q2_text = profile["q2_text"]
        q3_text = profile["q3_text"]
        q4_text = profile["q4_text"]
        q5_text = profile["q5_text"]
        education_school = profile["education_school"]
        education_uni = profile["education_uni"]
        riskgroup = profile["riskgroup"]
        riskgroup_text = profile["riskgroup_text"]
        age = profile["age"]
        id = profile["id"]
        idpic = profile["idpic"]
        return {
            'profile': profile,
            'id': id,
            'name':name,
            'gender': gender,
            'nationality': nationality,
            'profession': profession,
            'q1_text': q1_text,
            'q2_text': q2_text,
            'q3_text': q3_text,
            'q4_text': q4_text,
            'q5_text': q5_text,
            'education_school': education_school,
            'education_uni': education_uni,
            'nationality': nationality,
            'income': income,
            'religion': religion,
            'introduction': introduction,
            'riskgroup': riskgroup,	
            'riskgroup_text': riskgroup_text,
            'age': age, 
            'picpath': 'profilepics/' + idpic + '.JPG',

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
'''


class evaluation_de_3(Page):
    form_model = 'player'
    form_fields = ['advice', 'offer', 'advice_certainty']

    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        print(participant.profiles)
        print(player.round_number)
        profile = participant.profiles[player.round_number]
        prolificid_client = profile["prolificid_client"]
        nationality = profile["nationality"]
        name = profile["name"]
        introduction = profile["introduction"]
        religion = profile["religion"]
        profession = profile["profession"]
        gender = profile["gender"]
        income = profile["income"]
        q1_text = profile["q1_text"]
        q2_text = profile["q2_text"]
        q3_text = profile["q3_text"]
        q4_text = profile["q4_text"]
        q5_text = profile["q5_text"]
        q1_short = profile["q1_short"]
        q2_short = profile["q2_short"]
        q3_short = profile["q3_short"]
        q4_short = profile["q4_short"]
        q5_short = profile["q5_short"]
        education_school = profile["education_school"]
        education_uni = profile["education_uni"]
        riskgroup = profile["riskgroup"]
        riskgroup_text = profile["riskgroup_text"]
        age = profile["age"]
        q1 = profile["q1"]
        q2 = profile["q2"]
        q3 = profile["q3"]
        q4 = profile["q4"]
        q5 = profile["q5"]
        return {
            'profile': profile,
            'name':name,
            'nationality': nationality,
            'profession': profession,
            'prolificid_client': prolificid_client,
            'q1_text': q1_text,
            'q2_text': q2_text,
            'q3_text': q3_text,
            'q4_text': q4_text,
            'q5_text': q5_text,
            'q1_short': q1_short,
            'q2_short': q2_short,
            'q3_short': q3_short,
            'q4_short': q4_short,
            'q5_short': q5_short,
            'education_school': education_school,
            'gender': gender,
            'education_uni': education_uni,
            'nationality': nationality,
            'income': income,
            'religion': religion,
            'introduction': introduction,
            'riskgroup': riskgroup,	
            'riskgroup_text': riskgroup_text,
            'age': age, 
            'picpath': 'profilepics/' + prolificid_client + '.JPG',
            'scalepath1': 'scales/scale' + str(q1) + '.png',
            'scalepath2': 'scales/scale' + str(q2) + '.png',
            'scalepath3': 'scales/scale' + str(q3) + '.png',
            'scalepath4': 'scales/scale' + str(q4) + '.png',
            'scalepath5': 'scales/scale' + str(q5) + '.png',
       }
    

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
        name4 = profile4["name"]
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
            'advice1': player.in_round(1).advice,
            'advice2': player.in_round(2).advice,
            'advice3': player.in_round(3).advice,
            'advice4': player.in_round(4).advice
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
                   'education_school', 'education_uni','religion', 'party',]

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
    risk_survey_de,
    #evaluation_example_de,
    #evaluation_example_de_2,
    evaluation_example_de_3,
    #payment_instructions_de,
    explanations_rt_de,
    #evaluation_de,
    #evaluation_de_2,
    evaluation_de_3,
    payment_de,
    groupy_de,
    iat_de,
    demos_de,
    end_de
                   ]
