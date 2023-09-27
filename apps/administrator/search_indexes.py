from elasticsearch_dsl import Document, Text


class MyModelIndex(Document):
    title = Text()
    description = Text()

    class Index:
        name = 'myindex'
