from rest_framework import serializers
#from .models import Item
from .models import Post

#class ItemSerializer(serializers.ModelSerializer):
 #   class Meta:
  #      model = Item
   #     fields = ("__all__")

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'content',
            'writer',
        )
        model = Post