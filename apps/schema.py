import graphene
from graphene_django.types import DjangoObjectType
from .models import *


class AppType(DjangoObjectType):
    class Meta:
        model = App


class Query(object):
    all_apps = graphene.List(AppType)

    def resolve_all_apps(self, info, **kwargs):
        return App.objects.all()


class AppInput(graphene.InputObjectType):
    name = graphene.String(required=True)


class CreateApp(graphene.Mutation):
    class Arguments:
        app_data = AppInput(required=True)

    ok = graphene.Boolean()
    app = graphene.Field(AppType)

    def mutate(self, info, app_data):
        app = App.objects.create(name=app_data["name"])
        ok = True
        return CreateApp(app=app, ok=ok)
