import re


class CountVectorizer:
    """
    Class that allows to count words in a cluster of texts.
    Words are stored in lexicographically ordered feature_names list.
    Every text is represented by a list of word counts of words
    from feature_names.
    """

    def __init__(self):
        self.feature_names = list()
        self.dt_matrix = list()

    def fit_transform(self, texts: list[str]) -> list[list]:
        """
        Builds by the given corpus of texts list of present words and
        the document-term matrix.

        :param texts: list of strings to analyze
        :return: document-term matrix of texts
        """
        words_set = set()

        transformed_texts = list()
        for text in texts:
            text_words = re.sub("[.,:;?!()]", "", text).lower().split()
            transformed_texts.append(text_words)

        for text_words in transformed_texts:
            for word in text_words:
                words_set.add(word)
        self.feature_names = sorted(list(words_set))

        for text_words in transformed_texts:
            text_count = {word: 0 for word in words_set}
            for word in text_words:
                text_count[word] += 1
            self.dt_matrix.append([text_count[word] for word in self.feature_names])

        return self.dt_matrix

    def get_feature_names(self) -> list[str]:
        """
        Gets feature_names list.

        :return: lexicographically ordered word list from corpus
        of texts on which fit_transform method has been applied.
        If fit_transform method was not called, returns empty list.
        """
        return self.feature_names


if __name__ == "__main__":
    corpus = [
        "Crock Pot Pasta Never boil pasta again",
        "Pasta Pomodoro Fresh ingredients Parmesan to taste",
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)
