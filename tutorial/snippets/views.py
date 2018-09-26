from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from django.http import Http404
from django.contrib.auth.models import User
from rest_framework import generics, permissions


class SnippetList(generics.ListCreateAPIView):
    '''スニペットのリスト
    get: スニペットのリストを取得
    post: スニペットを追加
    '''
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    '''スニペット詳細
    '''
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permissions_class = (permissions.IsAuthenticatedOrReadOnly)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
