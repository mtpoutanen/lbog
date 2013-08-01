from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from users.models import Country, State, Skill
from lbog.forms import ProjectSearchForm
from projects.models import Project
from stories.models import Story
from django.core.context_processors import csrf
from django.db.models import Q
from operator import or_, and_
import math

def home(request):

    latest_completed    = Project.objects.filter(status='completed').order_by('-time_completed')[:3]
    latest_created      = Project.objects.filter(status='looking').order_by('-time_created')[:2]
    latest_stories      = Story.objects.all().order_by('-time_created')[:3]
    context                     = { 'latest_completed': latest_completed,
                                    'latest_created':   latest_created,
                                    'latest_stories':   latest_stories,
                                    }

    return render_to_response('index.html', context, context_instance=RequestContext(request))
   
def volunteers(request):
    '''
    comments
    '''
    form = ProjectSearchForm()
    context = {'form': form,}
    context.update(csrf(request))
    return render_to_response('volunteers.html', context, context_instance=RequestContext(request))    

def search_projects(request):
    '''
    comments
    '''
    if request.method == 'GET':
        context     = {}
        country     = request.GET['country']
        qlat        = -1.0
        qlon        = -1.0
        qlat_str    = request.GET['lat']
        if qlat_str != '':
            qlat = float(qlat_str)
        qlon_str    = request.GET['lon']
        if qlon_str != '':
            qlon = float(qlon_str)
        radius      = request.GET['radius']
        if radius != 'same_country' and radius != 'no_radius':
            radius = int(radius)
        keywords    = request.GET['keywords'].split(' ')
        skills      = request.GET.getlist('skills[]')

        argument_list = []

        if keywords != ['']:
            for kw in keywords:
                argument_list.append( Q(**{'description__icontains': kw} ))

        if qlat == -1.0 and radius == 'same_country':
            argument_list.append( Q(**{'country__country_name': country} ))            
        elif qlat == -1.0:
            pass
        else:
            distance_proj_ids = []
            all_projects = Project.objects.all()
            for proj in all_projects:
                if get_distance(proj.lat, proj.lon, qlat, qlon) <= radius:
                    distance_proj_ids.append(proj.id)
            argument_list.append( Q(**{'pk__in': distance_proj_ids} ))            

        if skills:
            skill_ids = Skill.objects.filter(skill_name__in=skills).values_list('id', flat=True)
            argument_list.append( Q(**{'skills__id__in': skill_ids} ))
            # import pdb; 
            # pdb.set_trace()

        if not argument_list:
            context['no_args'] = True
        else:
            context['projects'] = Project.objects.filter(reduce(and_, argument_list)).distinct()
            if not context['projects']:
                context['nothing_found'] = True

        return render_to_response('project-search-results.html', context)

def get_distance(projlat, projlon, qlat, qlon):
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