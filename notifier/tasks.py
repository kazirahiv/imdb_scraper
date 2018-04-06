from celery import task
from notifier.models import notf_req
from notifier.mailer import send_mail
from notifier.imdb import season_scan
archive = notf_req.objects.all()

@task()
def mail():
	for series in archive:
		print("tasking.................")
		series_name = series.series_name 
		series_link = series.series_link
		current_episode = series.current_episodes
		scanned = season_scan(series_link)
		updated_episode = scanned['total-released']
		series.updated_episode = updated_episode
		series.save()
		mail = series.email
		if series.updated_episode>current_episode:
			status = send_mail(mail, series_name)
			if status:
				series.status = status
				series.save()
		if series.status == True:
			series.delete()