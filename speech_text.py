import speech_recognition as sr

def getSpeechCommand():
    r = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("Please wait")
        r.adjust_for_ambient_noise(source)
        print("Say your command")
        audio = r.listen(source)

    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    try:
        response["transcription"] = r.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response
