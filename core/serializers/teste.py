from rest_framework.serializers import ModelSerializer

from core.models import Teste

class TesteSerializer(ModelSerializer):
    class Meta:
        model = Teste
        fields = "__all__"
        # fields = ["id", "teste"]