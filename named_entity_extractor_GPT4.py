"""A module for extracting named entities and their types from text.

This module uses the spacy library and the uk_core_news_sm model to perform
named entity recognition on Ukrainian text. It defines a class NamedEntityExtractor
that has a static method load_model and an instance method get_extract_entities.
"""

import spacy

class NamedEntityExtractor:
    """A class for extracting named entities and their types from text.

    Attributes:
        nlp: a spacy model object that performs natural language processing.
    """

    def __init__(self):
        """Initializes the NamedEntityExtractor with a None nlp attribute."""
        self.nlp = None

    @staticmethod
    def load_model(model_name):
        """Loads a spacy model by its name and returns it.

        Args:
            model_name: a string that represents the name of the spacy model.

        Returns:
            A spacy model object if the model name is valid, or None otherwise.
        """
        try:
            return spacy.load(model_name)
        except Exception as e:
            print(f"Error loading model {model_name}: {e}")
            return None

    def get_extract_entities(self, text):
        """Extracts named entities and their types from a given text.

        Args:
            text: a string that represents the text to be analyzed.

        Returns:
            A dictionary that maps each named entity to its type.

        Raises:
            TypeError: if the text is not a string.
        """
        # Use logical operator or instead of if statement
        text = text or ""
        # Use isinstance() instead of type()
        if not isinstance(text, str):
            raise TypeError("text must be a string")
        # Use logical operator or instead of if statement
        self.nlp = self.nlp or self.load_model("uk_core_news_sm")
        doc = self.nlp(text)
        # Use list comprehension instead of for loop
        entities = {ent.text: ent.label_ for ent in doc.ents}
        return entities
