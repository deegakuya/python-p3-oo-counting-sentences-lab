class MyString:
    def __init__(self, value=""):
        # Verify that the value is a string before assigning it
        self._value = None  # Use a private variable to store the value
        self.value = value  # Use the property to set the value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            raise ValueError("The value must be a string.")
        self._value = new_value

    def is_sentence(self):
        # Check if the value ends with a period
        return self.value.endswith('.')

    def is_question(self):
        # Check if the value ends with a question mark
        # This method is similar to is_sentence, but checks for a question mark
        return self.value.endswith('?')

    def is_exclamation(self):
        # Check if the value ends with an exclamation mark
        return self.value.endswith('!')

    def count_sentences(self):
        # Replace commas with periods, split on periods, and filter out empty strings
        sentences = [sentence for sentence in self.value.replace(',', '.').split('.') if sentence]
        return len(sentences)
