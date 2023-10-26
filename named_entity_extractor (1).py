# Імпортувати бібліотеку SpaCy
import spacy

# Завантажити модель uk_core_news_sm
nlp = spacy.load('uk_core_news_sm')


# Створити клас NamedEntityExtractor
class NamedEntityExtractor:
    """Клас для виявлення іменованих сутностей з тексту за допомогою SpaCy."""

    # Створити статичний метод load_model
    @staticmethod
    def load_model(model_name: str) -> spacy.language.Language:
        """
        Завантажити модель SpaCy за назвою.

        Параметри:
        model_name (str): Назва моделі SpaCy.

        Повертає:
        model (spacy.language.Language): Об'єкт моделі SpaCy або None, якщо модель не існує.
        """
        # Спробувати завантажити модель за допомогою spacy.load
        try:
            model = spacy.load(model_name)
        # Якщо виникає OSError
        except OSError:
            # Повернути None
            return None
        # Повернути модель
        return model

    # Створити метод get_extract_entities
    def get_extract_entities(self, text: str) -> dict:
        """
        Отримати словник іменованих сутностей та їх типів з тексту.

        Параметри:
        text (str): Текст для аналізу.

        Повертає:
        result (dict): Словник іменованих сутностей та їх типів.

        Викликає:
        TypeError: Якщо текст не є рядком.
        """
        # Перевірити тип вводу
        if not isinstance(text, str):
            # Підняти TypeError
            raise TypeError(f"Expecting string object, got {type(text)}")
        # Обробити текст за допомогою моделі nlp
        doc = nlp(text)
        # Створити порожній словник для результату
        result = {}
        # Для кожної іменованої сутності в doc
        for ent in doc.ents:
            # Додати сутність і її тип до результату
            result[ent.text] = ent.label_
        # Повернути результат
        return result
