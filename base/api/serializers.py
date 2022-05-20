from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from base.models import Blog, Machine

class BlogSerializer(ModelSerializer):
    class Meta:
        model = Blog 
        fields = "__all__"