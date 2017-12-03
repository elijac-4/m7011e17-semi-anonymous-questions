from .models import Text
from rest_framework import serializers


class TextSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    extra_kwargs = {'text_response': {'required': False}}

    class Meta:
        model = Text
        fields = ('text_response', 'topic_field', 'text_field', 'owner')

