from googletrans import Translator
translator = Translator()
output = translator.translate("they are expansive in cost",src="en",dest="gu")
print(output)
