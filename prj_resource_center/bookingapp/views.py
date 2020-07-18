from django.shortcuts import render
from django.views.generic import TemplateView
from bookingapp.models import Building, Level, Room
from json import dumps 

# Create your views here.

# logger = logging.getLogger(__name__)

class BookingHome(TemplateView):
	template_name = "bookingapp/booking_home.html"

	def get(self, request):
		levels = {}
		level_names = []
		for building in Building.objects.all():
			level_names = []
			for level in Level.objects.filter(building_id=building.id):
				if level:					
					level_names.append(level.name)
			if level_names:
				levels[building.name] = level_names
			
		for k, v in levels.items():
			print("Levels of", k, ":", v )
		levels_by_building = dumps(levels)
		context_data = {
			'buildings': Building.objects.all(),
			# 'levels': Level.objects.all(),
			'levels': levels,
			}
		print(f"Buildings: {context_data['buildings']}")
		print(f"Levels: {context_data['levels']}")		
		return render(request, self.template_name, context_data)


