import spacy


class NamedEntityExtractor:

    def __init__(self, model_name='uk_core_news_sm'):
        self.model = self.load_model(model_name)

    @staticmethod
    def load_model(model):
        try:
            return spacy.load(model)
        except Exception as e:
            print(f"An error occurred while loading the model: {e}")
            return None

    def get_extract_entities(self, text):
        if not isinstance(text, str):
            raise TypeError('text must be a string')
        else:
            # Обробляємо текст за допомогою моделі
            doc = self.model(text)
            # Витягуємо іменовані сутності з тексту та повертаємо їх у вигляді словника
            return {ent.text: ent.label_ for ent in doc.ents}
