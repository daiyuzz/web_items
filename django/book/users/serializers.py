from rest_framework import serializers
from .models import UserProfile, Book

"""
Serializer和ModelSerializer两种序列化方式中，前者比较容易理解，适用于新手
后者在商业项目中被使用的更多
ModelSerialize比Serializer更优
"""


class BookSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, max_length=100)
    isbn = serializers.CharField(required=True, max_length=100)
    author = serializers.CharField(required=True, max_length=100)
    publish = serializers.CharField(required=True, max_length=100)
    rate = serializers.FloatField(default=0)


class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"  # 将整个表的所有字段都序列化
        # fields = ("title","isbn","author") # 指定序列化某些字段

