from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    highlight = serializers.HyperlinkedIdentityField(
        view_name="snippet-highlight", format="html"
    )

    class Meta:
        model = Snippet
        fields = [
            "url",
            "id",
            "highlight",
            "owner",
            "title",
            "code",
            "linenos",
            "language",
            "style",
        ]

class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(
        many=True,
        view_name="snippet-detail",
        read_only=True
    )
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ["url", "id", "username", "password", "snippets"]

    def create(self, validated_data):
        user = User(
            username=validated_data["username"]
        )
        user.set_password(validated_data["password"])  # hash password
        user.save()
        return user
