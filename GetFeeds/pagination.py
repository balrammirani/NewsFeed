from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination


class NewsLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 10


class NewsPageNumberPagination(PageNumberPagination):
    page_size = 2
