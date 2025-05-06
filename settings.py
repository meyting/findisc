from os import environ

SESSION_CONFIGS = [
     dict(
         name='advisors_norisktool',
         app_sequence=['advisors'],	
         num_demo_participants=10,
         variant='bel'
     ),
    dict(
         name='advisors_noriskttool_implement',
         app_sequence=['advisors'],	
         num_demo_participants=10,
         variant='pat'

     ),
    dict(
         name='advisors_risktool_implement',
         app_sequence=['advisors'],	
         num_demo_participants=10,
         variant='verypat'
     ),
    dict(
         name='advisors_norisktool_accept',
         app_sequence=['advisors'],   	
         num_demo_participants=10,
         variant='pat_accept'
     ),
    dict(
         name='advisors_risktool_accept',
         app_sequence=['advisors'],	
         num_demo_participants=10,
         variant='verypat_accept'
     ),
    dict(
         name='advisors_random',
         app_sequence=['advisors'],	
         num_demo_participants=10,
     ),
    dict(
         name='customers',
         app_sequence=['customers_pre_risk_tool',
                        'riskToolOtreeApp',
                        'customers_post_risk_tool'],
         num_demo_participants=10,
     ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

ROOMS = [
    dict(
        name='adaccunrt',
        display_name='adaccunrt',
        # participant_label_file='_rooms/your_study.txt',
        #use_secure_urls=True,
    ),
        dict(
        name='adimplnrt',
        display_name='adimplnrt',
        # participant_label_file='_rooms/your_study.txt',
        #use_secure_urls=True,
    ),
        dict(
        name='adimplrt',
        display_name='adimplrt',
        # participant_label_file='_rooms/your_study.txt',
        #use_secure_urls=True,
    ),
        dict(
        name='adaccenrt',
        display_name='adaccenrt',
        # participant_label_file='_rooms/your_study.txt',
        #use_secure_urls=True,
    ),
        dict(
        name='adaccert',
        display_name='adaccert',
        # participant_label_file='_rooms/your_study.txt',
        #use_secure_urls=True,
    ),
        dict(
        name='clients',
        display_name='clients',
        # participant_label_file='_rooms/your_study.txt',
        #use_secure_urls=True,
    ),
        dict(
        name='pilot',
        display_name='pilot',
        # participant_label_file='_rooms/your_study.txt',
        #use_secure_urls=True,
    ),
]

PARTICIPANT_FIELDS = ["variant", "profiles", "suggestion", "group"]
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'de'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = False

AUTH_LEVEL = 'STUDY' # wieder löschen wenn Umgebungsvariable gesetzt			!!!!!!!!!!!!!!!

ADMIN_USERNAME = 'meyting_findisc'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = 'findisc'

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '8515273728031'

