import graphene
from graphene_django import DjangoObjectType

from blog.models import Author, Post


class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields = "__all__"


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = "__all__"


class CreateAuthor(graphene.Mutation):
    class Arguments:
        name = graphene.String()

    author = graphene.Field(AuthorType)

    def mutate(self, info, name):
        author = Author(name=name)
        author.save()

        return CreateAuthor(author=author)


class Query(graphene.ObjectType):
    all_authors = graphene.List(AuthorType)
    all_posts = graphene.List(PostType)

    def resolvev_all_authors(self, info):
        return Author.objects.all()

    def resolve_all_posts(self, info):
        return Post.objects.all()


class Mutation(graphene.ObjectType):
    create_author = CreateAuthor.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
