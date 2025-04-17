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
    NAME_IN_URL = 'adv1'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 10
    bonus = cu(1)
    fixedfee = cu(1)
    numberselections = 5
    Auszahlungsfaktor = 100
    budget = 10000
    budget_string = "10.000"
    Anlagehorizont = 10
    groupybudget = cu(1)

class Subsession(BaseSubsession):
    pass

def select_unique_risky_shares(data, n):
    shuffled_data = data.sample(frac=1).reset_index(drop=True)
    unique_risky_shares = shuffled_data.drop_duplicates(subset=['riskyshare']).sample(n=n)
    return unique_risky_shares

def creating_session(subsession: Subsession):
    import itertools
    variant = itertools.cycle(['bel', 'pat', 'verypat', 'pat_accept', 'verypat_accept'])
    groups = itertools.cycle(['circle', 'triangle',])
    if subsession.round_number == 1:
        for p in subsession.get_players():
            if 'variant' in subsession.session.config:
                p.participant.variant = subsession.session.config['variant']
            else:
                p.participant.variant = next(variant)
            p.participant.group = next(groups)
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
                                        [0, "Portfolio mit 0% Risikoanteil"],
                                        [10, "Portfolio mit 10% Risikoanteil"], 
                                        [20, "Portfolio mit 20% Risikoanteil"], 
                                        [30, "Portfolio mit 30% Risikoanteil"], 
                                        [40, "Portfolio mit 40% Risikoanteil"],
                                        [50, "Portfolio mit 50% Risikoanteil"], 
                                        [60, "Portfolio mit 60% Risikoanteil"], 
                                        [70, "Portfolio mit 70% Risikoanteil"], 
                                        [80, "Portfolio mit 80% Risikoanteil"], 
                                        [90, "Portfolio mit 90% Risikoanteil"],
                                        [100, "Portfolio mit 100% Risikoanteil"]],
                                        verbose_name="""""")
    advice_certainty_example = models.IntegerField(blank=True,
                                               choices=[[1, "sehr sicher"],
                                                        [2, "ziemlich sicher"],
                                                        [3, "ziemlich unsicher"], 
                                                        [4, "sehr unsicher"]],
                                        verbose_name="""""")
    riskgroup = models.IntegerField(blank=False)
    advice = models.IntegerField(choices=[
                                        [0, "Portfolio mit 0% Risikoanteil (ETF)"],
                                        [10, "Portfolio mit 10% Risikoanteil (ETF)"], 
                                        [20, "Portfolio mit 20% Risikoanteil (ETF)"], 
                                        [30, "Portfolio mit 30% Risikoanteil (ETF)"], 
                                        [40, "Portfolio mit 40% Risikoanteil (ETF)"],
                                        [50, "Portfolio mit 50% Risikoanteil (ETF)"], 
                                        [60, "Portfolio mit 60% Risikoanteil (ETF)"], 
                                        [70, "Portfolio mit 70% Risikoanteil (ETF)"], 
                                        [80, "Portfolio mit 80% Risikoanteil (ETF)"], 
                                        [90, "Portfolio mit 90% Risikoanteil (ETF)"],
                                        [100, "Portfolio mit 100% Risikoanteil (ETF)"]
                                        ],
                                        verbose_name="""""")
    advice_certainty = models.IntegerField(blank=False,
                                               choices=[[1, "sehr sicher"],
                                                        [2, "ziemlich sicher"],
                                                        [3, "ziemlich unsicher"], 
                                                        [4, "sehr unsicher"]],
                                        verbose_name="""""")

    offer = models.IntegerField()
    selected_best_advice = models.StringField(verbose_name="""""")

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

    distract = models.CharField(initial = None,
                                verbose_name = 'Hand aufs Herz: Können wir Ihre Daten bedenkenlos analysieren oder waren Sie während der Umfrage durch irgendwelche Einflüsse abgelenkt? <i>(Die Antwort auf diese Frage hat keinerlei Auswirkungen auf Ihre Auszahlung.)',
                                choices = [[1, 'Ich war sehr aufmerksam und gar nicht abgelenkt.'],
                                          [2, 'Ich war größstenteils aufmerksam und fast gar nicht abgelenkt.'],
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

    q1_advisor = models.IntegerField(blank=False)
    q2_advisor = models.IntegerField(blank=False)
    q3_advisor = models.IntegerField(blank=False)
    q4_advisor = models.IntegerField(blank=False)
    q5_advisor = models.IntegerField(blank=False)

    risktoolresult = models.FloatField()

    prolific_id = models.StringField(default=str(" "))

    groupy = models.FloatField()

    finpart = models.CharField()

# PAGES
class consent_de(Page):
    form_model = 'player'
    form_fields = ['consent']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1
    
    @staticmethod
    def before_next_page(self, timeout_happened):
        self.prolific_id = self.participant.label
    
class instructions_de(Page):
    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        return {
            'variant': participant.variant,
        }

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1
 
     
class risk_survey_de_2(Page):
    form_model = 'player'
    form_fields = ['q1_advisor', 'q2_advisor', 'q3_advisor', 'q4_advisor', 'q5_advisor']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1
    


class risk_tool_explanations(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1
    
    @staticmethod
    def vars_for_template(player):
        return {
            'Auszahlung': int(C.budget / C.Auszahlungsfaktor),
        }
    
class risk_tool_de(Page):
    @staticmethod
    def live_method(player, data):
        player.finalDecisionValue = str(data['final-decision-value'])

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1
    
class risk_tool_placeholder(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1
    


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
        #risktoolresult = player.risktoolresult*100
        return {
        #    'risktoolresult': risktoolresult,
            'variant': participant.variant,
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
            'picpath': 'profilepics/' + prolificid_client + '.jpg',
            'scalepath1': 'scales/scale' + str(q1) + '.png',
            'scalepath2': 'scales/scale' + str(q2) + '.png',
            'scalepath3': 'scales/scale' + str(q3) + '.png',
            'scalepath4': 'scales/scale' + str(q4) + '.png',
            'scalepath5': 'scales/scale' + str(q5) + '.png',
        }
    





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
        #risktoolresult = player.risktoolresult*100
        return {
        #    'risktoolresult': risktoolresult,
            'variant': participant.variant,
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
            'picpath': 'profilepics/' + prolificid_client + '.jpg',
            'scalepath1': 'scales/scale' + str(q1) + '.png',
            'scalepath2': 'scales/scale' + str(q2) + '.png',
            'scalepath3': 'scales/scale' + str(q3) + '.png',
            'scalepath4': 'scales/scale' + str(q4) + '.png',
            'scalepath5': 'scales/scale' + str(q5) + '.png',
       }
    

class payment_instructions_de(Page):  
    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        return {
            'variant': participant.variant,
        }

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS and player.participant.variant != 'pat' and player.participant.variant != 'verypat'


class payment_de(Page):
    form_model = 'player'
    form_fields = ['selected_best_advice']

    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        print(participant.profiles)
        print(player.round_number)
        profile1 = participant.profiles[1]
        profile2 = participant.profiles[2]
        profile3 = participant.profiles[3]
        profile4 = participant.profiles[4]
        profile5 = participant.profiles[5]
        profile6 = participant.profiles[6]
        profile7 = participant.profiles[7]
        profile8 = participant.profiles[8]
        profile9 = participant.profiles[9]
        profile10 = participant.profiles[10]
        prolificid_client1 = profile1["prolificid_client"]
        prolificid_client2 = profile2["prolificid_client"]
        prolificid_client3 = profile3["prolificid_client"]
        prolificid_client4 = profile4["prolificid_client"]
        prolificid_client5 = profile5["prolificid_client"]
        prolificid_client6 = profile6["prolificid_client"]
        prolificid_client7 = profile7["prolificid_client"]
        prolificid_client8 = profile8["prolificid_client"]
        prolificid_client9 = profile9["prolificid_client"]
        prolificid_client10 = profile10["prolificid_client"]
        name1 = profile1["name"]
        name2 = profile2["name"]
        name3 = profile3["name"]
        name4 = profile4["name"]
        name5 = profile5["name"]
        name6 = profile6["name"]
        name7 = profile7["name"]
        name8 = profile8["name"]
        name9 = profile9["name"]
        name10 = profile10["name"]
        prolificid_client1 = profile1["prolificid_client"]
        prolificid_client2 = profile2["prolificid_client"]
        prolificid_client3 = profile3["prolificid_client"]
        prolificid_client4 = profile4["prolificid_client"]
        prolificid_client5 = profile5["prolificid_client"]
        prolificid_client6 = profile6["prolificid_client"]
        prolificid_client7 = profile7["prolificid_client"]
        prolificid_client8 = profile8["prolificid_client"]
        prolificid_client9 = profile9["prolificid_client"]
        prolificid_client10 = profile10["prolificid_client"]
        return {
            'picpath1': 'profilepics/' + prolificid_client1 + '.jpg',
            'picpath2': 'profilepics/' + prolificid_client2 + '.jpg',
            'picpath3': 'profilepics/' + prolificid_client3 + '.jpg',
            'picpath4': 'profilepics/' + prolificid_client4 + '.jpg',
            'picpath5': 'profilepics/' + prolificid_client5 + '.jpg',
            'picpath6': 'profilepics/' + prolificid_client6 + '.jpg',
            'picpath7': 'profilepics/' + prolificid_client7 + '.jpg',
            'picpath8': 'profilepics/' + prolificid_client8 + '.jpg',
            'picpath9': 'profilepics/' + prolificid_client9 + '.jpg',
            'picpath10': 'profilepics/' + prolificid_client10 + '.jpg',
            'name1': name1,
            'name2': name2,
            'name3': name3,
            'name4': name4,
            'name5': name5,
            'name6': name6,
            'name7': name7,
            'name8': name8,
            'name9': name9,
            'name10': name10,
            'prolificid_client1': prolificid_client1,
            'prolificid_client2': prolificid_client2,
            'prolificid_client3': prolificid_client3,
            'prolificid_client4': prolificid_client4,
            'prolificid_client5': prolificid_client5,
            'prolificid_client6': prolificid_client6,
            'prolificid_client7': prolificid_client7,
            'prolificid_client8': prolificid_client8,
            'prolificid_client9': prolificid_client9,
            'prolificid_client10': prolificid_client10,
            'advice1': player.in_round(1).advice,
            'advice2': player.in_round(2).advice,
            'advice3': player.in_round(3).advice,
            'advice4': player.in_round(4).advice,
            'advice5': player.in_round(5).advice,
            'advice6': player.in_round(6).advice,
            'advice7': player.in_round(7).advice,
            'advice8': player.in_round(8).advice,
            'advice9': player.in_round(9).advice,
            'advice10': player.in_round(10).advice
            }

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
                   'education_school', 'education_uni','religion', 'party', 'distract', 'attention_check', 'finpart']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS
    
class groupy_de(Page):
    form_model = 'player'
    form_fields = ['groupy']

    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        return {
            'group': participant.group,
        }

    @staticmethod
    def error_message(player, values):
        if values['groupy'] is None:
            return 'Bitte klicken Sie auf den Slider um eine Entscheidung zu treffen.'
        return None
    
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
    risk_survey_de_2,
    risk_tool_explanations,
    #risk_tool_de,
    risk_tool_placeholder,
    evaluation_example_de_3,
    evaluation_de_3,
    payment_instructions_de,
    payment_de,
    demos_de,
    groupy_de,
    end_de
                   ]
