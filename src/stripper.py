
import unidecode, enchant, nltk
import string, re


class Stripper:
	'Clean a string by removing symbols, hyperlinks, and non-english characters or words'

	# removing emojis, hyperlinks, punctuation, and non-unicode characters.
	def removeAll(self, dirtyString):
		try:
			urlFree = self.removeURL(dirtyString.lower())
			cleanString = self.removeEmojis(urlFree)
			accentFree = self.changeCharacters(urlFree)
			en_str = self.englishOnly(accentFree)
			symbolFree = self.removePunctuation(en_str)
			return cleanString
			
		except Exception as e:
			print(f"\n\n\t\tSTRIPPER FAIL\n  {e}\n")
			exit()
		
	# remove non-english words
	def englishOnly(self, str):
		en_US = enchant.Dict("en_US")
		en_AU = enchant.Dict("en_AU")
		en_GB = enchant.Dict("en_GB")

		res = " ".join(w for w in nltk.wordpunct_tokenize(str) \
			if en_US.check(w) or en_GB.check(w) or en_AU.check(w) or not w.isalpha())
		
		return res
	
	# transliterate non-latin characters to latin characters (unicode to ascii), e.g., á
	def changeCharacters(self, accented):
		return unidecode.unidecode(accented)
	
	# remove emojis
	def removeEmojis(self, str):
		try:
			emoji_pattern = re.compile("["
							   u"\U0001F600-\U0001F64F"  
							   u"\U0001F300-\U0001F5FF"
							   u"\U0001F680-\U0001F6FF"
							   u"\U0001F1E0-\U0001F1FF"
							   "]+", flags=re.UNICODE)
							   
			return emoji_pattern.sub(r'', str)
		except Exception as e:
			print(f"\n\tSomething went wrong removing emojis::{e}\n\n")

	#remove hyperlinks
	def removeURL(self, str):
		return re.sub(r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))', '', str, flags=re.MULTILINE)
		
	
	# remove punctuation
	def removePunctuation(self, str):
		translation_table = str.maketrans('', '', string.punctuation)
		return str.translate(translation_table)
		
	def stripSpaces(self, str):
		return str.strip()

	
	
def test_stripping():
	#a test case
	print(u"beginning Stripper exam")
	tease = Stripper()
	
	#TEST TEXT 1
	text1 = "🤔 🙈 mie así, \u200c @hashtags @ &^% * \ud83c Black cats back rats baking matts and add it to their Résumé.  es se 😌 ds 💕👭👙 \u200c \ude18 :-) русский язык, tr. rússkiy yazýk andiamo العَرَبِيَّة‎ catss git.ly/asd/home/homeie/134oij23j23i4jl2k3jlk http://www.google.com During the month of may with colour. \N{MAHJONG TILE GREEN DRAGON} ->\U0001F620\U0001F310\U0001F690\U0001F1F0<-"
	
	results = tease.removeAll(text1)
	
	# print(f"\n\tSAMPLE TEXT\n{text1}\n")
	print(f"\n\tSAMPLE TEXT\n{results}\n")
	
if __name__ == "__main__":
	test_stripping()