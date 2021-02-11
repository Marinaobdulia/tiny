from translate import Translator
to_lang = 'zh'

path = 'test.txt'
with open(path,mode= 'r' ) as test_txt:
    to_translate = test_txt.readlines()

translator = Translator(to_lang=to_lang)

for line in to_translate:
    print(line)
    translation = translator.translate(line)
    print(translation)