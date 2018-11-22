
import unidecode, enchant, nltk
import string, re


class Strip:
	'Clean a string by removing symbols, hyperlinks, and non-english characters, and other undesired words.'
	
	def __init__(self, create = True):
		"""Not going to remove stop words? Pass in 'false' to skip building the set."""
		if create:
			self.stpwrds = set(nltk.corpus.stopwords.words('english'))

	def removeALL(self, dirty, user_length = 3):
		"""Removes all symobols and non-English characters, as well as stop words and short words.
			Will include words with lengths >= 3 (default)."""
		try:
			urlFree = self.stripURLs(dirty.lower())
			emojiFree = self.stripEmojis(urlFree)
			accentFree = self.transliterate(emojiFree)
			en_str = self.englishWordsOnly(accentFree)
			symbolFree = self.stripPunctuation(en_str)
			words = self.remove_stop_words(symbolFree)
			
			return self.stripSpaces(self.remove_short_words(words, user_length))

		except Exception as e:
			print(f"\n\n\t\tSTRIP removeALL FAIL\n  {e}\n")
			exit()
	
	
	# removing emojis, hyperlinks, punctuation, and non-unicode characters.
	def removeSymbols(self, dirty):
		"""Removes all symobols and non-English characters."""
		try:
			urlFree = self.stripURLs(dirty.lower())
			emojiFree = self.stripEmojis(urlFree)
			accentFree = self.transliterate(emojiFree)
			en_str = self.englishWordsOnly(accentFree)
			symbolFree = self.stripPunctuation(en_str)
			
			return self.stripSpaces(symbolFree)
			
		except Exception as e:
			print(f"\n\n\t\tSTRIP removeSymbols FAIL\n  {e}\n")
			exit()
	
	# remove english stop words
	def remove_stop_words(self, str):
		return " ".join(w for w in nltk.wordpunct_tokenize(str) \
			if w not in self.stpwrds)
	
	# remove short words
	def remove_short_words(self, str, length = 3):
		"""Removes any word with length >= 3 (default) or user defined"""
		return " ".join(w for w in nltk.wordpunct_tokenize(str) if len(w) >= length)
	
	# remove non-english words
	def englishWordsOnly(self, str):
		en_US = enchant.Dict("en_US")
		en_AU = enchant.Dict("en_AU")
		en_GB = enchant.Dict("en_GB")

		res = " ".join(w for w in nltk.wordpunct_tokenize(str) \
			if en_US.check(w) or en_GB.check(w) or en_AU.check(w) or not w.isalpha())
		
		return res
	
	# transliterate non-latin characters to latin characters (unicode to ascii), e.g., á
	def transliterate(self, accented):
		return unidecode.unidecode(accented)
	
	# remove emojis
	def stripEmojis(self, str):
		try:
			temp = re.sub(":((\+|\-)|([A-z]|[0-9]))+:", ' ', str) #remove text based emoji
		
			emoji_pattern = re.compile("["
					u"\U0001F600-\U0001F64F"  # emoticons
					u"\U0001F300-\U0001F5FF"  # symbols & pictographs
					u"\U0001F680-\U0001F6FF"  # transport & map symbols
					u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
					u"\U0001F1F2-\U0001F1F4"  # Macau flag
					u"\U0001F1E6-\U0001F1FF"  # flags
					u"\U0001F600-\U0001F64F"
					u"\U00002702-\U000027B0"
					u"\U000024C2-\U0001F251"
					u"\U0001f926-\U0001f937"
					u"\U0001F1F2"
					u"\U0001F1F4"
					u"\U0001F620"
					u"\u200d"
					u"\u2640-\u2642"
					"]+", flags=re.UNICODE)

			return emoji_pattern.sub(r'', temp)
			
		except Exception as e:
			print(f"\n\tSomething went wrong removing emojis::{e}\n\n")

	#remove hyperlinks
	def stripURLs(self, str):
		return re.sub(r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))', '', str, flags=re.MULTILINE)
		
	
	# remove punctuation
	def stripPunctuation(self, str):
		translation_table = str.maketrans('', '', string.punctuation)
		return str.translate(translation_table)
	
	# remove extra spaces within and on the ends of the string.
	def stripSpaces(self, str):
		s = re.sub(' +', ' ', str)
		return s.strip()

	
	
def test_example_strip_class():
	"""test example for the Strip class"""
	print("## beginning strip class example ##")
	tease = Strip()
	
	#TEST TEXT
	text = " :+1: :clock1230: :-1: :rocket: :stuck_out_tongue_closed_eyes: :octocat: 🤔 🙈 mie así, \u200c @hashtags @ &^% * \ud83c Black cats back rats baking matts and add it to their Résumé. i oh you es se 😌 ds 💕👭👙 \u200c \ude18 :-) русский язык, tr. rússkiy yazýk andiamo العَرَبِيَّة‎ catss git.ly/asd/home/homeie/134oij23j23i4jl2k3jlk http://www.google.com During the month of may with colour. \N{MAHJONG TILE GREEN DRAGON} ->\U0001F620\U0001F310\U0001F690\U0001F1F0<-"
	
	res = tease.removeALL(text)
		
	ans = 'black cats back rats baking add resume month may colour'
	
	if res == ans:
		print(True)
	else:
		print(False)
	
if __name__ == "__main__":
	test_example_strip_class()