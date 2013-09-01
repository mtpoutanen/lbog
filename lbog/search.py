from users.models import UserProfile, Skill
from projects.models import Project
from django.db.models import Q
from operator import or_, and_
import math

class Search(object):
    '''
    A utility class that searches for developers or projects
    based on different parameters
    '''

    SEARCH_DEVELOPERS   = 'developers'
    SEARCH_PROJECTS     = 'projects'

    def __init__(self, request):
        '''
        All variables and some search parameters are identical
        for Project and Developer searches
        '''
        # initialise the valriables
        self.country     = request.GET['country']
        self.qlat_str    = request.GET['lat']
        self.qlon_str    = request.GET['lon']
        self.radius      = request.GET['radius']
        self.skills      = request.GET.getlist('skills[]')
        self.keywords    = request.GET['keywords'].split(' ')
        # dummy values in case the user is not searching by location.
        self.qlat        = -1.0
        self.qlon        = -1.0
        # set coordinates and radius
        if self.qlat_str != '':
            self.qlat = float(self.qlat_str)
        if self.qlon_str != '':
            self.qlon = float(self.qlon_str)
        if self.radius != 'same_country' and self.radius != 'no_radius':
            self.radius = int(self.radius)
        # initialise the argument list and append it with the 
        # keyword and skills filters
        self.argument_list = []
        if self.keywords != ['']:
            for kw in self.keywords:
                self.argument_list.append( Q(**{'description__icontains': kw} ))
        if self.skills:
            skill_ids = Skill.objects.filter(skill_name__in=self.skills).values_list('id', flat=True)
            self.argument_list.append( Q(**{'skills__id__in': skill_ids} ))

    def get_search_context(self, search_type):
        '''
        returns a context dictionary with the projects or developers
        '''

        context = {}

        # The user is filtering by country name only
        if self.qlat == -1.0 and self.radius == 'same_country':
            self.argument_list.append( Q(**{'country__country_name': self.country} ))
        # The user is not filtering by geography
        elif self.qlat == -1.0:
            pass
        else:
        # The user searches by distance
            if search_type == self.SEARCH_PROJECTS:
            # this part of the function constructs a list of ids of all projects
            # that are within the radius. The get_distance function was taken
            # from here: http://www.johndcook.com/python_longitude_latitude.html
            # finally, the arguments are appended with the pk__in filter, which
            # looks for the primary keys (id) in the adjacent projects list
            # The elif statement does the same for developers
                distance_proj_ids = []
                all_projects = Project.objects.all()
                for proj in all_projects:
                    if self.get_distance(proj.lat, proj.lon, self.qlat, self.qlon) <= self.radius:
                        distance_proj_ids.append(proj.id)
                self.argument_list.append( Q(**{'pk__in': distance_proj_ids} ))            
            elif search_type == self.SEARCH_DEVELOPERS:
                distance_dev_ids = []
                all_developers = UserProfile.objects.all()
                for developer in all_developers:
                    if self.get_distance(developer.lat, developer.lon, self.qlat, self.qlon) <= self.radius:
                        distance_dev_ids.append(developer.id)
                self.argument_list.append( Q(**{'pk__in': distance_dev_ids} ))            
            
        # if there are still no arguments (i.e. user didn't enter any), pass
        # a boolean variable to the context
        if not self.argument_list:
            context['no_args'] = True
        # else, perform search
        else:
            if search_type == 'projects':
                # only find projects that have the status 'looking'
                self.argument_list.append( Q(**{'status': 'looking'} ))
                # pass a "projects" object to context (a list of found projects)
                context['projects'] = Project.objects.filter(reduce(and_, 
                                                self.argument_list)).distinct()
                if not context['projects']:
                    context['nothing_found'] = True
            elif search_type == 'developers':
                # similarly to above, only return Developers that have
                # explicitly allowed to be found in searches
                self.argument_list.append( Q(**{'allow_contact': True} ))
                self.argument_list.append( Q(**{'user_type': 'Developer'} ))
                context['developers'] = UserProfile.objects.filter(reduce(and_, self.argument_list)).distinct()
                if not context['developers']:
                    context['nothing_found'] = True
        return context
        
    def get_distance(self, projlat, projlon, qlat, qlon):
        '''
        calculates the distance between two points.
        code from http://www.johndcook.com/python_longitude_latitude.html
        '''
        # Convert latitude and longitude to 
        # spherical coordinates in radians.
        degrees_to_radians = math.pi/180.0
            
        # phi = 90 - latitude
        phi1 = (90.0 - projlat)*degrees_to_radians
        phi2 = (90.0 - qlat)*degrees_to_radians

        # theta = longitude
        theta1 = projlon*degrees_to_radians
        theta2 = qlon*degrees_to_radians
            
        # Compute spherical distance from spherical coordinates.
            
        # For two locations in spherical coordinates 
        # (1, theta, phi) and (1, theta, phi)
        # cosine( arc length ) = 
        #    sin phi sin phi' cos(theta-theta') + cos phi cos phi'
        # distance = rho * arc length
        
        cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) + 
               math.cos(phi1)*math.cos(phi2))
        arc = math.acos( cos )

        # Remember to multiply arc by the radius of the earth 
        # in your favorite set of units to get length.
        # 6371 = earth's radius in km
        return 6371*arc
