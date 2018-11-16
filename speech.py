import speech_recognition as sr

#record audio
r=sr recogniser()
with sr.microphone()as source:
	r.adjust_for_ambient_noise(source,duration=5)
	r.dynamic_energy_threshold= True
	print("speak something!")
	audio = r.listen(source)

#speech recognition using google speech recognition
try:
	print("you said: "+ r.recognize_google(audio))
except sr.UknownValueError:
	print("google speech recognition could not understand audio")
except sr.RequestError as e:
	print("could not request results from google speech recognition service; {0}".form)