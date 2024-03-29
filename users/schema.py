import graphene
from graphene_django.types import DjangoObjectType
from .models import *


class UserType(DjangoObjectType):
    class Meta:
        model = User


class Query(object):
    all_users = graphene.List(UserType)

    def resolve_all_users(self, info, **kwargs):
        return User.objects.all()


class Mutation(object):
    pass
