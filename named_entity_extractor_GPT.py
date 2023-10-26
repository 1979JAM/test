import spacy


class NamedEntityExtractor:
    def __init__(self, model_name='uk_core_news_sm'):
        self.nlp = self.load_model(model_name)

    def get_extract_entities(self, text):
        self._validate_input(text)
        doc = self.nlp(text)
        return {ent.text: ent.label_ for ent in doc.ents}

    def _validate_input(self, text):
        if not isinstance(text, str):
            raise TypeError("Input must be a string")

    @classmethod
    def load_model(cls, model_name):
        try:
            return spacy.load(model_name)
        except OSError as e:
            return None
