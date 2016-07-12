from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView
from .models import News
from .serializer import (
    NewsSerializer,
    NewsDetailSerializer,
    NewsCreateSerializer
)
from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from .pagination import NewsLimitOffsetPagination, NewsPageNumberPagination
from .permissions import IsOwnerOrReadOnly


# Create your views here.


class NewsCreateAPIView(CreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    #    def form_valid(self, request):
    #        object.owner = self.request.user
    #        print(object.owner.id)
    # object.save()
    # return super(NewsCreateAPIView, self).form_valid(form)

'''
class NewsDeleteAPIView(DestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer
'''

# Detail + Update + Delete


class NewsDetailAPIView(DestroyModelMixin, UpdateModelMixin, RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]

    #  def perform_update(self, serializer): #for RetrieveUpdateAPIView
    #      serializer.save(user=self.request.user)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class NewsListAPIView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = NewsPageNumberPagination
    #permission_classes = [AllowAny]


'''
class NewsUpdateAPIView(DestroyModelMixin, UpdateModelMixin, RetrieveAPIView):

    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
  #  def perform_update(self, serializer): #for RetrieveUpdateAPIView
  #      serializer.save(user=self.request.user)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

'''
# class UserFormView(View):
#     form_class = UserForm
#     template_name = 'GetFeeds/registration_form.html'
#
#     def get(self, request):
#         form = self.form_class(None)
#         return render(request, self.template_name,{'form':form})
#
#    def post(self, request):
#       current_user = self.request.user
#       print(current_user.id)

#         form = self.form_class(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user.set_password(password)
#             user.save()
