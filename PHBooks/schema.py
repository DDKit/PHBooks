import graphene
import apps.schema
import books.schema
import users.schema


class Query(
    apps.schema.Query,
    books.schema.Query,
    users.schema.Query,
    graphene.ObjectType
):
    pass


class Mutation(graphene.ObjectType):
    create_app = apps.schema.CreateApp().Field()



schema = graphene.Schema(query=Query, mutation=Mutation)
