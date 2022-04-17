from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        for current_category in self.categories:
            if current_category.id == category_id:
                current_category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        for current_topic in self.topics:
            if current_topic.id == topic_id:
                current_topic.topic = new_topic
                current_topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        for current_document in self.documents:
            if current_document.id == document_id:
                current_document.file_name = new_file_name

    def delete_category(self, category_id):
        for current_category in self.categories:
            if current_category.id == category_id:
                self.categories.remove(current_category)

    def delete_topic(self, topic_id):
        for current_topic in self.topics:
            if current_topic.id == topic_id:
                self.topics.remove(current_topic)

    def delete_document(self, document_id):
        for current_document in self.documents:
            if current_document.id == document_id:
                self.documents.remove(current_document)

    def get_document(self, document_id):
        for current_document in self.documents:
            if current_document.id == document_id:
                return current_document

    def __repr__(self):
        return '\n'.join([c_d.__repr__() for c_d in self.documents])
