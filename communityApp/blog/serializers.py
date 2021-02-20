from rest_framework import serializers
from .models import Blog, Comment

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
    
    def create(self, validated_data):
        return Blog(**validated_data)

    def update(self, instance, validated_data):
        instance.blog_date_created = validated_data.get('blog_date_created', instance.blog_date_created)
        instance.blog_title = validated_data.get('blog_title', instance.blog_title)
        instance.blog_content = validated_data.get('blog_content', instance.blog_content)
        instance.blog_image = validated_data.get('blog_image', instance.blog_image)
        instance.blog_likes = validated_data.get('blog_likes', instance.blog_likes)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.user = validated_data.get('user', instance.user)
        return instance

    
    class CommentSerializer(serializers.ModelSerializer):
    class meta:
        model = Blog
        fields = '__all__'

        def create(self,validated_data):
            return Comment(**validated_data)

        def update(self, instance, validated_data):
            instance.date = validated_data.get('date',instance.date)
            instance.body = validated_data.get('body',instance.body)
            instance.likes =validated_data.get('likes',instance.likes)
            instance.user = validated_data.get('user',instance.user)
            instance.blog = validated_data.get('blog',instance.blog)
            return instance
    
    
