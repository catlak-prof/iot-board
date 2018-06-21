from rest_framework import serializers
from data.models import Data

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ('author', 'alan1', 'alan2', 'alan3', 'alan4', 'alan5', 'alan6', 'alan7', 'alan8')



