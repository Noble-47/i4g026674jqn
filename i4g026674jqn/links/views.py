from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)

from links.models import Link
from links.serializers import LinkSerializer

from blog.models import Post

# Create your views here.


class PostListApi(ListAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer


class PostCreateApi(CreateAPIView):
    model = Post
    serializer_class = LinkSerializer


class PostUpdateApi(CreateAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer


class PostDetailApi(RetrieveAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer


class PostUpdateApi(UpdateAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer


class PostDeleteApi(DestroyAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer
