import graphene
from graphene_django.types import DjangoObjectType
from .models import *


class BookType(DjangoObjectType):
    class Meta:
        model = Book


class Query(object):
    all_books = graphene.List(BookType)

    def resolve_all_books(self, info, **kwargs):
        return Book.objects.all()


class Mutation(object):
    pass
