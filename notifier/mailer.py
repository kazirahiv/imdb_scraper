import smtplib

def send_mail(recipient, seriesName):
	sm = smtplib.SMTP('smtp-mail.outlook.com', 587)
	sm.ehlo()
	sm.starttls()
	sm.login('rahivjobs@outlook.com', '')
	message = 'Subject: Alert! '+seriesName+' Episode Released !'
	print(message)
	sm.sendmail('rahivjobs@outlook.com',recipient, message)
	sm.quit()
	return True
