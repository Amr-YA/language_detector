import re
import string

class Cleaner:
	arabic_punctuations = '''`÷×؛<>_()*&^%][ـ،/:"؟.,'{}~¦+|!”…“–ـ'''
	english_punctuations = string.punctuation
	punctuations_list = arabic_punctuations + english_punctuations
	translator = str.maketrans('', '', punctuations_list)
	url_pattern = re.compile('https?://\S+|www\.\S+')

	def __init__(self):
		pass

	def clean(sentance):
		text = re.sub(r'[[]]', ' ', sentance)
		text = text.lower()
		text = Cleaner.url_pattern.sub(r'', text) # remove URLs
		text = text.translate(Cleaner.translator) # remove punc
		text = re.sub('[0-9]', '', text)
		text = text.strip()
		
		return text