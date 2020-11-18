from rest_framework.generics import UpdateAPIView
from rest_framework.serializers import ModelSerializer
from .models import B


class BSerializer(ModelSerializer):
    class Meta:
        model = B
        fields = '__all__'


class BUpdateAPIView(UpdateAPIView):
    serializer_class = BSerializer
    queryset = B.objects.all()
