import speech_recognition as sr

r = sr.Recognizer()
mic_list = sr.Microphone.list_microphone_names()

print("Available Microphones:")
for i, mic_name in enumerate(mic_list):
    print(f"{i}: {mic_name}")

device_index = int(input("Enter your mic index from above list: "))

with sr.Microphone(device_index=device_index) as source:
    print("Say something...")
    r.adjust_for_ambient_noise(source, duration=1)
    audio = r.listen(source)

try:
    print("You said:", r.recognize_google(audio, language="en-IN"))
except sr.UnknownValueError:
    print("Couldn't understand audio")
except sr.RequestError as e:
    print("Could not request results; check internet connection")
