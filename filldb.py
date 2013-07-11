from users.models import Country, State, Skill, UserProfile
from django.contrib.auth.models import User

countrylist = [
'Afghanistan',
'Albania',
'Algeria',
'Andorra',
'Angola',
'Antigua and Barbuda',
'Argentina',
'Armenia',
'Australia',
'Austria',
'Azerbaijan',
'Bahamas, The',
'Bahrain',
'Bangladesh',
'Barbados',
'Belarus',
'Belgium',
'Belize',
'Benin',
'Bhutan',
'Bolivia',
'Bosnia and Herzegovina',
'Botswana',
'Brazil',
'Brunei',
'Bulgaria',
'Burkina Faso',
'Burundi',
'Cambodia',
'Cameroon',
'Canada',
'Cape Verde',
'Central African Republic',
'Chad',
'Chile',
'China, People\'s Republic of',
'Colombia',
'Comoros',
'Congo, (Congo Brazzaville)',
'Congo, (Congo Kinshasa)',
'Costa Rica',
'Cote d\'Ivoire (Ivory Coast)',
'Croatia',
'Cuba',
'Cyprus',
'Czech Republic',
'Denmark',
'Djibouti',
'Dominica',
'Dominican Republic',
'Ecuador',
'Egypt',
'El Salvador',
'Equatorial Guinea',
'Eritrea',
'Estonia',
'Ethiopia',
'Faroe Islands',
'Fiji',
'Finland',
'France',
'Gabon',
'Gambia, The',
'Georgia',
'Germany',
'Ghana',
'Greece',
'Grenada',
'Guatemala',
'Guinea',
'Guinea-Bissau',
'Guyana',
'Haiti',
'Honduras',
'Hong Kong',
'Hungary',
'Iceland',
'India',
'Indonesia',
'Iran',
'Iraq',
'Ireland',
'Israel',
'Italy',
'Jamaica',
'Japan',
'Jordan',
'Kazakhstan',
'Kenya',
'Kiribati',
'Korea, North',
'Korea, South',
'Kuwait',
'Kyrgyzstan',
'Laos',
'Latvia',
'Lebanon',
'Lesotho',
'Liberia',
'Libya',
'Liechtenstein',
'Lithuania',
'Luxembourg',
'Macau',
'Macedonia',
'Madagascar',
'Malawi',
'Malaysia',
'Maldives',
'Mali',
'Malta',
'Marshall Islands',
'Mauritania',
'Mauritius',
'Mexico',
'Micronesia',
'Moldova',
'Monaco',
'Mongolia',
'Montenegro',
'Morocco',
'Mozambique',
'Myanmar (Burma)',
'Namibia',
'Nauru',
'Nepal',
'Netherlands',
'New Zealand',
'Nicaragua',
'Niger',
'Nigeria',
'Norway',
'Oman',
'Pakistan',
'Palau',
'Panama',
'Papua New Guinea',
'Paraguay',
'Peru',
'Philippines',
'Poland',
'Portugal',
'Qatar',
'Romania',
'Russia',
'Rwanda',
'Saint Kitts and Nevis',
'Saint Lucia',
'Saint Vincent and the Grenadines',
'Samoa',
'San Marino',
'Sao Tome and Principe',
'Saudi Arabia',
'Senegal',
'Serbia',
'Seychelles',
'Sierra Leone',
'Singapore',
'Slovakia',
'Slovenia',
'Solomon Islands',
'Somalia',
'South Africa',
'Spain',
'Sri Lanka',
'Sudan',
'Suriname',
'Swaziland',
'Sweden',
'Switzerland',
'Syria',
'Tajikistan',
'Tanzania',
'Thailand',
'Timor-Leste (East Timor)',
'Togo',
'Tonga',
'Trinidad and Tobago',
'Tunisia',
'Turkey',
'Turkmenistan',
'Tuvalu',
'Uganda',
'Ukraine',
'United Arab Emirates',
'United Kingdom',
'United States',
'Uruguay',
'Uzbekistan',
'Vanuatu',
'Vatican City',
'Venezuela',
'Vietnam',
'Yemen',
'Zambia',
'Zimbabwe']

statelist = [
'n/a (outside of US)',
'Alabama',
'Alaska',
'Arizona',
'Arkansas',
'California',
'Colorado',
'Connecticut',
'Delaware',
'District of Columbia',
'Florida',
'Georgia',
'Hawaii',
'Idaho',
'Illinois',
'Indiana',
'Iowa',
'Kansas',
'Kentucky',
'Louisiana',
'Maine',
'Montana',
'Nebraska',
'Nevada',
'New Hampshire',
'New Jersey',
'New Mexico',
'New York',
'North Carolina',
'North Dakota',
'Ohio',
'Oklahoma',
'Oregon',
'Maryland',
'Massachusetts',
'Michigan',
'Minnesota',
'Mississippi',
'Missouri',
'Pennsylvania',
'Rhode Island',
'South Carolina',
'South Dakota',
'Tennessee',
'Texas',
'Utah',
'Vermont',
'Virginia',
'Washington',
'West Virginia',
'Wisconsin',
'Wyoming',
]

skill_list = ['PHP', 'Java', 'Ruby', 'Android', 'C', 'C#', 'C++', 
            'HTML5', 'Objective-C', 'SQL', 'JavaScript', 'Python']

usernames       = ['test_developer',        'test_charity',             'mtpoutanen']
emails          = ['dev@lbog.com',          'charity@lbog.com',         'm.poutanen.12@ucl.ac.uk']
first_names     = ['John',                  'Jill',                     'Mikko']
last_names      = ['Dogooder',              'Peaceandlove',             'Poutanen']
passwords       = ['password',              'password',                 'postgres']    
titles          = ['Senior Developer',      'Director',                 'Overall Genius']
user_types      = ['Developer',             'Charity',                  'Developer']
companies       = ['Mikkosoft',             'World Peace',              'UCL']
countries       = ['Finland',               'United Kingdom',           'United States']
states          = ['n/a (outside of US)',   'n/a (outside of US)',      'Virginia']
cities          = ['Vaasa',                 'London',                   'Richmond']
post_codes      = ['65200',                 'NW8 9JT',                  'ZZZ']
addresses       = ['Majakka',               'Elm Tree',                 'Blaah']    
descriptions    = ['superb developer',      'a really nice charity',    'Master of Universe']

user_lists      = [usernames, emails, first_names, last_names, passwords]
profile_lists   = [titles, user_types, companies, countries, states, cities, post_codes, addresses, descriptions]

user_field_list     = ['username', 'email', 'first_name', 'last_name', 'password']
profile_field_list  = ['title', 'user_type','company_name', 'country', 'state', 'city', 'post_code', 'address', 'description']

class DB_Filler():

    def fill_all(self):
        self.create_countries()
        self.create_skills()
        self.create_states()
        self.create_users()

    def create_users(self):
        adminuser = User()
        devuser = User()
        charityuser = User()

        for i in xrange(0, len(user_field_list)):
            field_name              = user_field_list[i]
            source_list             = user_lists[i]
            dev_value               = source_list[0]
            charity_value           = source_list[1]
            admin_value             = source_list[2]
            setattr(devuser, field_name, dev_value)
            setattr(charityuser, field_name, charity_value)
            setattr(adminuser, field_name, admin_value)

        adminuser.is_superuser      = True
        adminuser.is_staff          = True

        devuser.save()
        charityuser.save()
        adminuser.save()

        devprofile          = devuser.get_profile()
        charity_profile     = charityuser.get_profile()
        adminprofile        = adminuser.get_profile()

        for i in xrange(0, len(profile_field_list)):
            field_name                  = profile_field_list[i]
            source_list                 = profile_lists[i]
            dev_value                   = source_list[0]
            charity_value               = source_list[1]
            admin_value                 = source_list[2]
            
            if field_name == 'country':
                dev_value       = Country.objects.get(country_name=source_list[0])
                charity_value   = Country.objects.get(country_name=source_list[1])
                admin_value     = Country.objects.get(country_name=source_list[2])
            
            if field_name == 'state':
                dev_value       = State.objects.get(state_name=source_list[0])
                charity_value   = State.objects.get(state_name=source_list[1])
                admin_value     = State.objects.get(state_name=source_list[2])
            
            setattr(devprofile, field_name, dev_value)
            setattr(charity_profile, field_name, charity_value)
            setattr(adminprofile, field_name, admin_value)

        allskills = Skill.objects.all()
        myskills = []

        for myskill in allskills:
            if len(myskill.skill_name) > 5:
                myskills.append(myskill)

        devprofile.skills = myskills

        devprofile.save()
        charity_profile.save()
        adminprofile.save()
    
    def create_countries(self):
        for country in countrylist:
            newcountry = Country(country_name=country)
            newcountry.save()

    def create_states(self):
        for state in statelist:
            newstate = State(state_name=state)
            newstate.save()

    def create_skills(self):
        for skill in skill_list:
            newskill = Skill(skill_name=skill)
            newskill.save()        


