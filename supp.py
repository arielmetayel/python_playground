import Entities.File as File
from collections import Counter
​
number_of_chunks = 2
file_chunks = 20
common_words_limit = None
chunk = 0
​
​
class UniqueText:
​
    def __init__(self, supplier_id: int):
        """
        :param supplier_id:
        """
        self.supplier_id = supplier_id
        self.file_model = File.File
        self.chunk = chunk
​
    def next_page(self):
        self.chunk = + 1
        return self.get_common_words()
​
    def get_common_words(self):
        """
        :return:
        """
        flat_list = self.get_content_as_words()
        counter = Counter(flat_list)
        count_common_words = counter.most_common(common_words_limit)
        common_words = []
        for common in count_common_words:
            # if common[1] > 1:
            common_words.append(common[0])
​
        return common_words
​
    def get_content_as_words(self):
        """
        Returns a list with all words in the file_content for this Supplier
        :param chunk:
        :return:
        """
        supplier_files = self.file_model.query() \
            .join('file_contents', 'file_contents.file_id', '=', 'files.id') \
            .where('user_id', '=', self.supplier_id) \
            .limit(file_chunks * number_of_chunks) \
            .get() \
            .chunk(file_chunks)
        if supplier_files is None:
            return False
        full_text = []
        for files in supplier_files[self.chunk]:
            full_text.append(files.text.splitlines())
​
        flat_list = []
        for sublist in full_text:
            for item in sublist:
                if len(item) < 1:
                    continue
                flat_list.append(item)
        return flat_list
​
    @staticmethod
    def intersection(lst1, lst2, reverse: bool = False):
        """
        :param lst1:
        :param lst2:
        :param reverse:
        :return:
        """
        lst3 = [value for value in lst1 if value in lst2] if not reverse \
            else [value for value in lst1 if value not in lst2]
        return lst3
