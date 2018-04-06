from django.shortcuts import render
from notifier.imdb import season_scan
from .models import notf_req
from .forms import submit
# Create your views here.


def index(request):
	if request.method == "POST":
		mail = request.POST.get('email',)
		link = request.POST.get('link')
		print("Submitted link-",link)
		print("Submitted email-",mail)
		scanned = season_scan(link)
		current_episodes = scanned['total-released']
		series_name = scanned['series_name']
		obj = notf_req(series_name=series_name, series_link=link, email=mail, current_episodes=current_episodes, updated_episode= 0, status=False)
		obj.save()
		return render(request, 'notifier/thanks.html')
	else:
		form = submit()

	return render(request, 'notifier/index.html', {'form': form})