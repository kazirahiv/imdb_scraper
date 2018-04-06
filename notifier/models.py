from django.db import models
from django.core.mail import send_mail
import smtplib

# Create your models here.
def send_mail(recipient):
	sm = smtplib.SMTP('smtp-mail.outlook.com', 587)
	sm.ehlo()
	sm.starttls()
	sm.login('rahivjobs@outlook.com', 'mustangGT1997')
	sm.sendmail('rahivjobs@outlook.com',recipient, 'Subject: Alert!\n Episode Released')
	sm.quit()



class notf_req(models.Model):
	series_name = models.CharField(max_length=40)
	email =  models.CharField(max_length=25)
	current_episodes = models.IntegerField(default=0)
	updated_episode = models.IntegerField(default=0)
	status = models.BooleanField(default=None)
	series_link = models.CharField(max_length=40)

	def trigger(self):
		if self.updated_episode>self.current_episodes:
			send_mail(self.email)
			self.status = True



