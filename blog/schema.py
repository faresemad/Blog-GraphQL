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


class UpdatePost(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        title = graphene.String()
        content = graphene.String()

    post = graphene.Field(PostType)

    def mutate(self, info, id, title=None, content=None):
        post = Post.objects.get(pk=id)
        if title is not None:
            post.title = title
        if content is not None:
            post.content = content
        post.save()

        return UpdatePost(post=post)


class Query(graphene.ObjectType):
    all_authors = graphene.List(AuthorType)
    all_posts = graphene.List(PostType)
    auther_by_id = graphene.Field(AuthorType, id=graphene.ID())
    post_by_id = graphene.List(PostType, id=graphene.ID())

    def resolve_all_authors(self, info):
        return Author.objects.all()

    def resolve_all_posts(self, info):
        return Post.objects.select_related("author").all()

    def resolve_auther_by_id(self, info, id):
        return Author.objects.get(pk=id)

    def resolve_post_by_id(self, info, id):
        return Post.objects.filter(author=id)


class Mutation(graphene.ObjectType):
    create_author = CreateAuthor.Field()
    create_post = CreatePost.Field()
    update_post = UpdatePost.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
