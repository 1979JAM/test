import spacy


class NamedEntityExtractor:
    @staticmethod
    def load_model(model_name):
        try:
            return spacy.load(model_name)
        except OSError:
            return None

    def __init__(self):
        self.nlp = self.load_model('uk_core_news_sm')

    def get_extract_entities(self, text):
        if not isinstance(text, str):
            raise TypeError("Input must be a string")
        elif text == "":
            return {}
        else:
            doc = self.nlp(text)
            return {ent.text: ent.label_ for ent in doc.ents}
