from rest_framework import serializers
from .models import Blog, Comment

class CustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = None
        related_fields = None
    
    def get_field_names(self, declared_fields, info):
        expanded_fields = super(CustomSerializer, self).get_field_names(declared_fields, info)

        if getattr(self.Meta, 'extra_fields', None):
            return expanded_fields + self.Meta.related_fields
        else:
            return expanded_fields

class BlogSerializer(CustomSerializer):
    username = serializers.SerializerMethodField()
    user_email = serializers.SerializerMethodField()

    def get_username(self, obj: Blog):
        return f"{obj.user.first_name} {obj.user.last_name}"
    
    def get_user_email(self, obj: Blog):
        return obj.user.email
    class Meta:
        model = Blog
        exclude = ['user', ]
        related_fields = ['username']
    
    def create(self, validated_data):
        return Blog.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.blog_date_created = validated_data.get('blog_date_created', instance.blog_date_created)
        instance.blog_title = validated_data.get('blog_title', instance.blog_title)
        instance.blog_content = validated_data.get('blog_content', instance.blog_content)
        instance.blog_image = validated_data.get('blog_image', instance.blog_image)
        instance.blog_likes = validated_data.get('blog_likes', instance.blog_likes)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.user = validated_data.get('user', instance.user)
        instance.save()
        return instance

class CommentSerializer(CustomSerializer):
    pass
