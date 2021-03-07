from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
    
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
