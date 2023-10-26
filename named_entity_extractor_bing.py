import spacy


class NamedEntityExtractor:
    def __init__(self, model='uk_core_news_sm'):
        self.nlp = self._load_and_validate_model(model)

    @staticmethod
    def _load_and_validate_model(model):
        try:
            return spacy.load(model)
        except OSError:
            print(f"Model '{model}' does not exist. Please provide a valid model.")
            return None

    def _validate_input(self, text):
        if not isinstance(text, str):
            raise TypeError("Input must be a string")

    def get_extract_entities(self, text):
        self._validate_input(text)
        if not self.nlp:
            print("Model is not loaded. Please load a valid model before extracting entities.")
            return {}
        doc = self.nlp(text)
        return {ent.text: ent.label_ for ent in doc.ents}
