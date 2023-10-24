# from elasticsearch_dsl import Document, Text
# from django_elasticsearch_dsl import Index
#
# from administrator.models import Student
#
# student_index = Index('students')
#
#
# @student_index.doc_type
# class StudentIndex(Document):
#     username = Text()
#
#     class Django:
#         model = Student
#
#     def prepare_username(self, instance):
#         return instance.username
