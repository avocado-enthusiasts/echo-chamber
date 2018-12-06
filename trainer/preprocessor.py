import re
import string
import enchant
import nltk
import unidecode


class Strip:
    """Clean a string by removing symbols, hyperlinks, and non-english characters, and other undesired words."""

    def __init__(self, create=True):
        """Not going to remove stop words? Pass in 'false' to skip building the set."""
        if create:
            self.stpwrds = set(nltk.corpus.stopwords.words('english'))

    def removeAllJSON(self, json_object, json_field, user_length=3):
        """Do the exact same thing with a JSON object"""
        clean = self.removeALL(json_object[json_field], user_length)
        json_object[json_field] = clean
        return json_object

    def removeALL(self, dirty, user_length=3):
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
    def remove_short_words(self, str, length=3):
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
            temp = re.sub(":((\+|\-)|([A-z]|[0-9]))+:", ' ', str)  # remove text based emoji

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

    # remove hyperlinks
    def stripURLs(self, str):
        return re.sub(
            r'http\S+',
            '', str, flags=re.MULTILINE)

    # remove punctuation
    def stripPunctuation(self, str):
        translation_table = str.maketrans('', '', string.punctuation)
        return str.translate(translation_table)

    # remove extra spaces within and on the ends of the string.
    def stripSpaces(self, str):
        s = re.sub(' +', ' ', str)
        return s.strip()


# def test_example_strip_class():
#     """test example for the Strip class"""
#     print("## beginning strip class example ##")
#     tease = Strip()
#
#     # TEST TEXT
#     text = '{"author": "numis10", "author_flair_css_class": "purpleblack", "author_flair_text": "the fury of 20 bil. women silenced by the church (aka 1st reich)", "body": "just saying that violence doesn't need to be forms we have have already tried many times before and seen the results of - like gun revolutions and their results of leading to expansion of empire and war... that's the thing.. this kind of violence leads to growth of capital, because it courts and seeks out war..... and war is expansion of capital.... french revolution led to napoleon... american revolution led to this bullshit we in now.... german revolutions led to.. well..  you get the point..\n\nhow about magic or something...? curse putin and trump... crack their brains with some serious lucid dreaming astral souldiving tech...... it\'s something different...\n\nhow about just everyone goes to the white house and goes inside and refuses to leave... if enough ppl did it.... they would not be able to shoot or remove em alll... \n\ni dunnol....\n\nbut, we got enough smarts and talent among the lot of us.... we should be able to figure this out!\n\n\n", "can_gild": true, "controversiality": 0, "created_utc": 1518667755, "distinguished": null, "edited": false, "gilded": 0, "id": "du9rvq9", "is_submitter": false, "link_id": "t3_7xklto", "parent_id": "t1_du9qtjg", "permalink": "/r/Anarchism/comments/7xklto/meet_the_radical_leftists_in_america_arming/du9rvq9/", "retrieved_on": 1519259037, "score": 1, "stickied": false, "subreddit": "Anarchism", "subreddit_id": "t5_2qh5j", "subreddit_type": "public"}'
#
#     res = tease.removeALL(text)
#     print(res)
#
#     ans = 'black cats back rats baking add resume month may colour'
#     print(ans)
#
#     if res == ans:
#         print(True)
#     else:
#         print(False)
#
#
# if __name__ == "__main__":
#     test_example_strip_class()
