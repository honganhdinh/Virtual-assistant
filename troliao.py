#listening

import speech_recognition,pyttsx3
from datetime import date,datetime 


robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain =''
while True:
	with speech_recognition.Microphone() as mic:
		print("Robot: I'm Listening")
		audio = robot_ear.listen(mic)

	print('Robot...')
	try:
		you = robot_ear.recognize_google(audio)
	except:
		you =""
	print('You: ' + you)

	#understand
	if you =='':
		print(' Sorry i cant hear what you say')
	elif 'hello' in you:
		robot_brain = ' hello hong anh'
	elif 'today' in you:
		today = date.today()
		robot_brain = today.strftime("%B %d, %Y")
	elif 'time' in you:
		now = datetime.now()
		robot_brain = now.strftime('%H hour %M minutes %S seconds')
	elif 'president' in you:
		robot_brain = 'Nguyen Tan Phuc'
	elif 'bye' in you:
		robot_brain = 'see you again sir'
		print('Robot ' + robot_brain)
		robot_mouth.say(robot_brain)
		robot_mouth.runAndWait()
		break
	else:
		robot_brain = ' i am fine'
	print('Robot ' + robot_brain)
		
	#speak
	robot_mouth.say(robot_brain)
	robot_mouth.runAndWait()




