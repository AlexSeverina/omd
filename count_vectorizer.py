import math
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
            self.dt_matrix.append([text_count[word]
                                   for word in self.feature_names])

        return self.dt_matrix

    def get_feature_names(self) -> list[str]:
        """
        Gets feature_names list.

        :return: lexicographically ordered word list from corpus
        of texts on which fit_transform method has been applied.
        If fit_transform method was not called, returns empty list.
        """
        return self.feature_names


class TfidfTransformer:
    """
    Class that allows to calculate tf-idf metric for words in a cluster
    of texts based on texts count matrix, i.e. every given text is
    represented by a list of word counts of words.
    """

    @staticmethod
    def tf_transform(cnt_matrix: list[list]) -> list[list]:
        """
        Calculates tf metric for words by given count matrix.

        :param cnt_matrix: texts in form of matrix with word counts.
        :return: tf metric for every word in every text
        """
        return [[round(x / sum(row), 3) for x in row] for row in cnt_matrix]

    @staticmethod
    def idf_transform(cnt_matrix: list[list]) -> list[float]:
        """
        Calculates idf metric for words by given count matrix.

        :param cnt_matrix: texts in form of matrix with word counts.
        :return: idf metric for every word in every text
        """
        doc_num = len(cnt_matrix)
        word_num = len(cnt_matrix[0])

        docs_with_word = [[1 if x > 0 else 0 for x in row]
                          for row in cnt_matrix]
        words_cnts = [sum([row[i] for row in docs_with_word])
                      for i in range(word_num)]
        return [
            round(math.log((doc_num + 1) / (word_cnt + 1)) + 1, 3)
            for word_cnt in words_cnts
        ]

    def fit_transform(self, cnt_matrix: list[list]) -> list[list]:
        """
        Calculates tf-idf metric for words by given count matrix.

        :param cnt_matrix: texts in form of matrix with word counts.
        :return: tf-idf metric for every word in every text
        """
        tf_matrix = self.tf_transform(cnt_matrix)
        idf_matrix = self.idf_transform(cnt_matrix)
        return [
            [round(tf * idf, 3) for tf, idf in zip(row, idf_matrix)]
            for row in tf_matrix
        ]


class TfidfVectorizer(CountVectorizer):
    """
    Class that allows to calculate tf-idf metric for words in a cluster of
    texts. Words are stored in lexicographically ordered feature_names list.
    Every text can be obtained in a form of a list of word counts of words
    from feature_names.
    """

    def __init__(self):
        super().__init__()
        self.transformer = TfidfTransformer()

    def fit_transform(self, texts: list[str]) -> list[list]:
        """
        Builds by the given corpus of texts list of present words and
        the document-term matrix and tf-idf matrix.

        :param texts: list of strings to analyze
        :return: tf-idf matrix of texts
        """
        super().fit_transform(texts)
        return self.transformer.fit_transform(self.dt_matrix)


if __name__ == "__main__":
    corpus = [
        "Crock Pot Pasta Never boil pasta again",
        "Pasta Pomodoro Fresh ingredients Parmesan to taste",
    ]

    vectorizer = TfidfVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)
