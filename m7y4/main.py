import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr
import random
from googletrans import Translator


duration = 5  # секунды записи
sample_rate = 44100

easy_level = ["кот", "собака", "яблоко", "молоко", "солнце",'стул','корова','коробка','стол']

medium_level = ["банан", "Школа", "друг", "окно", "желтый",'телефон','компьютер','самолет']

hard_level = ["технология", "Университет", "информация", "произношение", "воображение",'подводная лодка','медицина','математика','психология','Подземелье']

level_selection = input('Привет! Это игра - переводчик. \nВ чём суть этой игры? \nЭта игра помогает выучить Английский. \nКак в неё играть? \n1:Сначала вам надо выбрать сложность , легкий , средний или сложный. \n2:Потом программа напишет случайное слово исходя из сложности, которую вы выбрали. \n3.Вы должны перевисти это слово на Английский в течение 5 секунд. \n4:Программа проверит ваш ответ и скажет вам правильно или нет. \nТеперь вам надо выбрать сложноть. Если легкий уровень напишите "легкий" , если средний уровень напишите "средний" и если сложный напишите "сложный":')

while True:
    
    if level_selection == 'легкий':
        easy_from_ru_to_en_word = random.choice(easy_level)


        print("🎙Переведи слово " , easy_from_ru_to_en_word ,", на Английский время пошло...")
        recording = sd.rec(
        int(duration * sample_rate), # длительность записи в сэмплах
        samplerate=sample_rate,      # частота дискретизации
        channels=1,                  # 1 — это моно
        dtype="int16")               # формат аудиоданных
        sd.wait()  # ждём завершения записи

        wav.write("output.wav", sample_rate, recording)
        print("✅ Запись завершена, теперь распознаём...")

        recognizer = sr.Recognizer()
        with sr.AudioFile("output.wav") as source:
            audio = recognizer.record(source)

        try:
            text = recognizer.recognize_google(audio, language="en-EN")
            print("📝Ты сказал:", text)

        except sr.UnknownValueError:             # - если Google не понял речь (шум, молчание)
            print("Не удалось распознать речь.")
        except sr.RequestError as e:             # - если нет интернета или API недоступен
            print(f"Ошибка сервиса: {e}")


        translator = Translator()
        translator = Translator()
        translated = translator.translate(text, dest='ru')
        if translated.text == easy_from_ru_to_en_word:
            print('Правильно!!! У вас хорошо получается продолжайте в том же духе')
            
        elif translated.text != easy_from_ru_to_en_word:
            print('Не правильно! Ничего страшного. В следуюший раз точно получится!')     
        learn_more1 = input('Будете продолжать , или нет?(Если да то напишите !да! , если нет то напишите !нет!)')
        if learn_more1 == 'да':
            level_selection = input('Выберете сложность если легкий уровень напишите "легкий" , если средний уровень напишите "средний" и если сложный напишите "сложный":')
            
        elif learn_more1 == 'нет':
            print('На сегодня всё!')
            break
        else:
            print('Неверный ввод!!!')
            break

    elif level_selection == 'средний':
        medium_from_ru_to_en_word = random.choice(medium_level)


        print("🎙Переведи слово " , medium_from_ru_to_en_word ,", на Английский время пошло...")
        recording = sd.rec(
        int(duration * sample_rate), # длительность записи в сэмплах
        samplerate=sample_rate,      # частота дискретизации
        channels=1,                  # 1 — это моно
        dtype="int16")               # формат аудиоданных
        sd.wait()  # ждём завершения записи

        wav.write("output.wav", sample_rate, recording)
        print("✅ Запись завершена, теперь распознаём...")

        recognizer = sr.Recognizer()
        with sr.AudioFile("output.wav") as source:
            audio = recognizer.record(source)

        try:
            text = recognizer.recognize_google(audio, language="en-EN")
            print("📝Ты сказал:", text)

        except sr.UnknownValueError:             # - если Google не понял речь (шум, молчание)
            print("Не удалось распознать речь.")
        except sr.RequestError as e:             # - если нет интернета или API недоступен
            print(f"Ошибка сервиса: {e}")


        translator = Translator()
        translator = Translator()
        translated = translator.translate(text, dest='ru')
        if translated.text == medium_from_ru_to_en_word:
            print('Правильно!!! У вас хорошо получается продолжайте в том же духе')
            
        elif translated.text != medium_from_ru_to_en_word:
            print('Не правильно! Ничего страшного. В следуюший раз точно получится!')     
        learn_more2 = input('Будете продолжать , или нет?(Если да то напишите !да! , если нет то напишите !нет!)')
        if learn_more2 == 'да':
            level_selection = input('Выберете сложность если легкий уровень напишите "легкий" , если средний уровень напишите "средний" и если сложный напишите "сложный":')
        elif learn_more2 == 'нет':
            print('На сегодня всё!')
            break
        else:
            print('Неверный ввод!!!')
            break
    elif level_selection == 'сложный':
        hard_from_ru_to_en_word = random.choice(hard_level)


        print("🎙Переведи слово " , hard_from_ru_to_en_word ,", на Английский время пошло...")
        recording = sd.rec(
        int(duration * sample_rate), # длительность записи в сэмплах
        samplerate=sample_rate,      # частота дискретизации
        channels=1,                  # 1 — это моно
        dtype="int16")               # формат аудиоданных
        sd.wait()  # ждём завершения записи

        wav.write("output.wav", sample_rate, recording)
        print("✅ Запись завершена, теперь распознаём...")

        recognizer = sr.Recognizer()
        with sr.AudioFile("output.wav") as source:
            audio = recognizer.record(source)

        try:
            text = recognizer.recognize_google(audio, language="en-EN")
            print("📝Ты сказал:", text)

        except sr.UnknownValueError:             # - если Google не понял речь (шум, молчание)
            print("Не удалось распознать речь.")
        except sr.RequestError as e:             # - если нет интернета или API недоступен
            print(f"Ошибка сервиса: {e}")


        translator = Translator()
        translator = Translator()
        translated = translator.translate(text, dest='ru')
        if translated.text == hard_from_ru_to_en_word:
            print('Правильно!!! У вас хорошо получается продолжайте в том же духе')
            
        elif translated.text != hard_from_ru_to_en_word:
            print('Не правильно! Ничего страшного. В следуюший раз точно получится!')     
        learn_more3 = input('Будете продолжать , или нет?(Если да то напишите !да! , если нет то напишите !нет!)')
        if learn_more3 == 'да':
            level_selection = input('Выберете сложность если легкий уровень напишите "легкий" , если средний уровень напишите "средний" и если сложный напишите "сложный":')
            
        elif learn_more3 == 'нет':
            print('На сегодня всё!')
            break
        else:
            print('Неверный ввод!!!')
            break
    else:
        print('Неверный ввод!!!')
        break