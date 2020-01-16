from rest_framework import serializers
from accounts.models import Account, JobDetail, SocialLink


class ProfileCardSerializer(serializers.ModelSerializer):

    name = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()

    class Meta:
        model = Account
        fields = (
            'profile_picture',
            'username',
            'name',
            'session',
            'graduation_year',
            'intake',
            'phone_number',
            'department'
        )

    def request_user(self):
        return self.context.get('request').user

    @staticmethod
    def get_name(obj: Account):
        return f'{obj.first_name} {obj.last_name}'

    def get_username(self):
        return self.request_user()
