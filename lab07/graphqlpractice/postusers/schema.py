from graphene_django import DjangoObjectType
import graphene
from postusers.models import Post as PostModel
from postusers.models import Author as AuthorModel


class Post(DjangoObjectType):
    class Meta:
        model = PostModel
        fields = ["id", "title", "body", "author"]


class Author(DjangoObjectType):
    class Meta:
        model = AuthorModel
        fields = ["id", "name", "posts"]

    def resolve_posts(self, info):
        return PostModel.objects.filter(author=self)

    @classmethod
    def get_node(cls, info, id):
        return Author.objects.get(id=id)


class Query(graphene.ObjectType):
    authors = graphene.List(Author)
    posts = graphene.List(Post)

    def resolve_authors(self, info):
        return AuthorModel.objects.all()

    def resolve_posts(self, info):
        return PostModel.objects.all()


schema = graphene.Schema(query=Query)
