from users.models import Country, State, Skill, UserProfile
from projects.models import Project
from django.contrib.auth.models import User
import random
import datetime

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
'Bahamas',
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
'n/a (Outside of US or Canada)',
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

skill_list = ['iOS','Android','Windows Mobile','Mobile Development HTML5','Desktop Development',
'Web Development Full Stack','Web Development Server Side','Web Development Frond End','SQL / Database Development',]

usernames       = ['test_dev_manchester',   'test_char_london',         'mikko']
emails          = ['dev@lbog.com',          'charity@lbog.com',         'mtpoutanen@gmail.com']
passwords       = ['password',              'password',                 'postgres']    
titles          = ['Senior Developer',      'Director',                 'Overall Genius']
wwws            = ['www.mikkosoft.com',      'www.world-peace.com',     'www.ucl.ac.uk']
user_types      = ['Developer',             'Charity',                  'Developer']
given_names     = ['John',                  'Mary',                     'Mikko']
family_names    = ['Smith',                 'Poppins',                  'Poutanen']
companies       = ['Mikkosoft',             'World Peace',              'UCL']
countries       = ['United Kingdom',        'United Kingdom',           'United Kingdom']
states          = ['n/a (Outside of US or Canada)', 'n/a (Outside of US or Canada)', 'n/a (Outside of US or Canada)']
cities          = ['Manchester',            'Birmingham',               'London']
lats            = [53.479606,            	52.486779, 					51.511427]
lons            = [-2.24851,                -1.890299,                  -0.11978]
allow_contacts  = [False,                    True,                      True]
images          = [
'images/profile_images/1/prof1.jpg',
'images/profile_images/2/prof2.jpg',
'images/profile_images/3/prof3.jpg',
]
descriptions    = ['Several years of experience as a python and HTML5 Developer',
                  'We aim to help hungry children in need',
                  'Done development in Java, Miranda, PHP, HTML5, Android, Python, Django etc.']

user_lists      = [usernames, emails, passwords]
profile_lists   = [titles, user_types, given_names, family_names, wwws, companies, 
                    countries, states, cities, lats, lons, descriptions, allow_contacts, images]

user_field_list     = ['username', 'email', 'password']
profile_field_list  = ['title', 'user_type', 'given_name', 'family_name', 'www', 'company_name', 
                        'country', 'state', 'city', 'lat', 'lon', 'description', 'allow_contact', 'logo']

p_titles            = [
'London Looking',
'Brighton Looking',
'Bristol Looking',
'Birmingham Looking',
'Liverpool Looking',
'Manchester Looking',
'Cambridge Looking',
'Slough Looking',
'Sheffield Looking',
'Edinburgh Under Way',
'Brighton Under Way',
'Bristol Under Way',
'Chelmsform Under Way',
'Liverpool Under Way',
'Luton Completed',
'London Completed',
'Swindon Completed',
'Reading Completed',
'Eastbourne Completed',
'Portsmouth Completed',
]

p_need_locals       = [
True,
False,
True,
False,
True,
False,
True,
False,
True,
False,
True,
False,
True,
False,
True,
False,
True,
False,
True,
False,
]
p_statuses          = [
'looking',
'looking',
'looking',
'looking',
'looking',
'looking',
'looking',
'looking',
'looking',
'under_way',
'under_way',
'under_way',
'under_way',
'under_way',
'completed',
'completed',
'completed',
'completed',
'completed',
'completed',
]


p_cities            = [
'London',
'Brighton',
'Bristol',
'Birmingham',
'Liverpool',
'Manchester',
'Cambridge',
'Slough',
'Sheffield',
'Edinburgh',
'Brighton',
'Bristol',
'Chelmsform',
'Liverpool',
'Luton',
'London',
'Swindon',
'Reading',
'Eastbourne',
'Portsmouth',
]

p_lats              = [
51.535231,
50.82871,
51.46513,
52.493651,
53.415671,
53.488454,
52.20645,
51.511253,
53.381613,
55.954102,
50.82871,
51.46513,
51.736756,
53.415671,
51.879723,
51.535231,
51.556956,
51.45406,
50.769362,
50.817134,
]

p_lons              = [
-0.119691,
-0.143219,
-2.587388,
-1.889756,
-2.993195,
-2.250245,
0.121866,
-0.594942,
-1.470201,
-3.188828,
-0.143219,
-2.587388,
0.468622,
-2.993195,
-0.420069,
-0.119691,
-1.779455,
-0.973934,
0.290438,
-1.083319,
]

p_descriptions      = [
'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
]

p_images            = [
'images/project_images/1/proj1.jpg',
None,
'images/project_images/3/proj3.jpg',
None,
'images/project_images/5/proj5.jpg',
None,
'images/project_images/7/proj7.jpg',
None,
'images/project_images/9/proj9.jpg',
None,
'images/project_images/11/proj11.jpg',
None,
'images/project_images/13/proj13.jpg',
None,
'images/project_images/15/proj15.jpg',
None,
'images/project_images/17/proj17.jpg',
None,
'images/project_images/19/proj19.jpg',
None,
]

project_field_list  = ['title', 'need_locals', 'status', 
                         'city', 'lat', 'lon', 'description',  'image']
project_lists = [p_titles, p_need_locals, p_statuses, p_cities,
                p_lats, p_lons, p_descriptions, p_images]

# 'time_created', 'time_completed', 'country', 'state','skills',

class DB_Filler():

    def fill_all(self):
        self.create_countries()
        self.create_skills()
        self.create_states()
        self.create_users()
        self.create_projects()

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
            if len(myskill.skill_name) > 15:
                myskills.append(myskill)

        devprofile.skills = myskills

        devuser.save()
        charityuser.save()
        adminuser.save()

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

    def create_projects(self):
        charity = UserProfile.objects.get(id=2)
        for x in xrange(0,20):
            project = Project()
            for y in xrange(0, 8):
                setattr(project, project_field_list[y], project_lists[y][x])
            country = Country.objects.get(country_name='United Kingdom')
            project.country = country
            state = State.objects.get(state_name__startswith='n/a')
            project.state = state
            project.charity = charity
            project.save()
            skills = Skill.objects.all()
            skills_sample = random.sample(skills, 3)
            project.skills = skills_sample
            td = datetime.timedelta(days=x)
            time_created = datetime.datetime.now() - 2*td
            if project.status == 'completed':
                project.time_completed = datetime.datetime.now() - td
            project.save()

    def delete_all(self):
        self.delete_users()
        self.delete_states()
        self.delete_countries()
        self.delete_skills()
        self.delete_projects()

    def delete_users(self):
        User.objects.all().delete()

    def delete_states(self):
        State.objects.all().delete()
    
    def delete_skills(self):        
        Skill.objects.all().delete()
    
    def delete_countries(self):
        Country.objects.all().delete()

    def delete_projects(self):
        Project.objects.all().delete()