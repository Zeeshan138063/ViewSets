from rest_framework.pagination import (
LimitOffsetPagination,
PageNumberPagination
)

class PostPageNumberPagination(PageNumberPagination):
    page_size = 5
    # display_page_controls = True
