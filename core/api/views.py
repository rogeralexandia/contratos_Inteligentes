from rest_framework.generics import ListAPIView

from core.api.serializers import CategorySerializers
from core.pos.models import Category


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
