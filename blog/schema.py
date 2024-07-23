import graphene
from graphene_django import DjangoObjectType

from blog.models import Author, Post


class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields = "__all__"


class AuthorType(DjangoObjectType):
    is_active = graphene.Boolean()
    just_text = graphene.String()

    class Meta:
        model = Author
        fields = "__all__"

    def resolve_is_active(self, info):
        return True

    def resolve_just_text(self, info):
        return "Just a text"


class CreateAuthor(graphene.Mutation):
    class Arguments:
        name = graphene.String()

    author = graphene.Field(AuthorType)

    def mutate(self, info, name):
        author = Author(name=name)
        author.save()

        return CreateAuthor(author=author)


class CreatePost(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        content = graphene.String()
        author_id = graphene.ID()

    post = graphene.Field(PostType)

    def mutate(self, info, title, content, author_id):
        post = Post(title=title, content=content, author_id=author_id)
        post.save()

        return CreatePost(post=post)


class Query(graphene.ObjectType):
    all_authors = graphene.List(AuthorType)
    all_posts = graphene.List(PostType)

    def resolve_all_authors(self, info):
        return Author.objects.all()

    def resolve_all_posts(self, info):
        return Post.objects.all()


class Mutation(graphene.ObjectType):
    create_author = CreateAuthor.Field()
    create_post = CreatePost.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
