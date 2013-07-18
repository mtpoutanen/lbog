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
'China',
'Colombia',
'Comoros',
'Congo',
'Costa Rica',
'Cote d\'Ivoire',
'Croatia',
'Cuba',
'Cyprus',
'Czech Republic',
'Democratic Republic of Congo',
'Denmark',
'Djibouti',
'Dominica',
'Dominican Republic',
'East Timor',
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
'Gambia',
'Georgia',
'Germany',
'Ghana',
'Greece',
'Grenada',
'Guatemala',
'Guinea',
'Guinea Bissau',
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
'Myanmar',
'Namibia',
'Nauru',
'Nepal',
'Netherlands',
'New Zealand',
'Nicaragua',
'Niger',
'Nigeria',
'North Korea',
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
'South Korea',
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
'n/a (outside of US or Canada)',
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
'Alberta',
'British Columbia',
'Manitoba',
'New Brunswick',
'Newfoundland and Labrador',
'Nova Scotia',
'Ontario',
'Prince Edward Island',
'Quebec',
'Saskatchewan',
]

skill_list = ['PHP', 'Java', 'Ruby', 'Android', 'C', 'C#', 'C++', 
            'HTML5', 'Objective-C', 'SQL', 'JavaScript', 'Python']

usernames       = ['test_developer',        'test_charity',             'mikko']
emails          = ['dev@lbog.com',          'charity@lbog.com',         'mtpoutanen.gmail.com']
passwords       = ['password',              'password',                 'postgres']    
titles          = ['Senior Developer',      'Director',                 'Overall Genius']
user_types      = ['Developer',             'Charity',                  'Developer']
given_names     = ['John',                  'Jill',                     'Mikko']
family_names    = ['Dogooder',              'Peaceandlove',             'Poutanen']
companies       = ['Mikkosoft',             'World Peace',              'UCL']
countries       = ['Finland',               'United States',            'United Kingdom']
states          = ['n/a (outside of US or Canada)',     'Virginia',     'n/a (outside of US or Canada)']
cities          = ['Vaasa',                 'Richmond',                 'London']
lats            = [30.00,                   50.00,                      90.00]
lons            = [30.00,                   50.00,                      90.00]
# post_codes      = ['65200',                 'ZZZ',                      'NW8 9JT']
# addresses       = ['Majakka',               'Blaah',                    '3 Elm Tree Court']    
descriptions    = ['superb developer',      'a really nice charity',    'Master of Universe']

user_lists      = [usernames, emails, passwords]
profile_lists   = [titles, user_types, given_names, family_names, companies, 
                    countries, states, cities, lats, lons,
                    # post_codes, addresses, 
                    descriptions]

user_field_list     = ['username', 'email', 'password']
profile_field_list  = ['title', 'user_type', 'given_name', 'family_name', 'company_name', 
                        'country', 'state', 'city', 
                        # 'post_code', 'address', 
                        'description']

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

            if field_name == 'password':
                devuser.set_password(dev_value)
                charityuser.set_password(charity_value)
                adminuser.set_password(admin_value)
            else:
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


