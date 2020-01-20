from rest_framework import serializers
from accounts.models import Account, JobDetail, SocialLink
from django.http.request import HttpRequest


class SocialLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = SocialLink
        fields = '__all__'
        read_only_fields = (
            'accounts',
            'user',
        )


class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobDetail
        fields = '__all__'
        read_only_fields = (
            'accounts',
            'user'
        )


class ProfileCardSerializer(serializers.ModelSerializer):

    name = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()
    department_full_name = serializers.SerializerMethodField()
    profile_picture_link = serializers.SerializerMethodField()

    class Meta:
        model = Account
        fields = (
            'profile_picture_link',
            'username',
            'name',
            'session',
            'graduation_year',
            'intake',
            'phone_number',
            'department',
            'department_full_name'
        )

    @staticmethod
    def get_name(obj: Account):
        return f'{obj.first_name} {obj.last_name}'

    @staticmethod
    def get_username(obj: Account):
        return obj.user.username

    @staticmethod
    def get_department_full_name(obj: Account):
        return obj.get_department_display()

    def get_profile_picture_link(self, obj: Account):
        protocol = 'https'
        request: HttpRequest = self.context['request']
        if request.is_secure() is False:
            protocol = 'http'
        return f'{protocol}://{request.get_host()}/{obj.profile_picture.url}'


class ProfileSerializer(serializers.ModelSerializer):

    name = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()
    jobs = JobSerializer(many=True, read_only=True)
    social = SocialLinkSerializer(many=False, read_only=True)
    department_full_name = serializers.SerializerMethodField()
    profile_picture_link = serializers.SerializerMethodField()

    class Meta:
        model = Account
        fields = (
            'profile_picture',
            'profile_picture_link',
            'username',
            'name',
            'session',
            'graduation_year',
            'intake',
            'phone_number',
            'department',
            'department_full_name',
            'email',
            'present_address',
            'permanent_address',
            'birth_date',
            'social',
            'jobs',
        )
        extra_kwargs = {
            'profile_picture': {'write_only': True}
        }

    @staticmethod
    def get_name(obj: Account):
        return f'{obj.first_name} {obj.last_name}'

    @staticmethod
    def get_username(obj: Account):
        return obj.user.username

    @staticmethod
    def get_department_full_name(obj: Account):
        return obj.get_department_display()

    def get_profile_picture_link(self, obj: Account):
        if obj.profile_picture is None:
            obj.profile_picture.url = None
        protocol = 'https'
        request: HttpRequest = self.context['request']
        if request.is_secure() is False:
            protocol = 'http'
        return f'{protocol}://{request.get_host()}/{obj.profile_picture.url}'


class AlumniSerializer(serializers.ModelSerializer):

    name = serializers.SerializerMethodField()
    department_full_name = serializers.SerializerMethodField()
    profile_picture_link = serializers.SerializerMethodField()

    class Meta:
        model = Account
        fields = (
            'profile_picture_link',
            'name',
            'session',
            'graduation_year',
            'intake',
            'phone_number',
            'department',
            'department_full_name',
        )

    @staticmethod
    def get_department_full_name(obj: Account):
        return obj.get_department_display()

    @staticmethod
    def get_name(obj: Account):
        return f'{obj.first_name} {obj.last_name}'

    def get_profile_picture_link(self, obj: Account):
        if obj.profile_picture is None:
            obj.profile_picture.url = None
        protocol = 'https'
        request: HttpRequest = self.context['request']
        if request.is_secure() is False:
            protocol = 'http'
        return f'{protocol}://{request.get_host()}/{obj.profile_picture.url}'


class AlumniSingleSerializer(serializers.ModelSerializer):

    name = serializers.SerializerMethodField()
    jobs = JobSerializer(many=True)
    social = SocialLinkSerializer(many=False, read_only=True)
    department_full_name = serializers.SerializerMethodField()
    profile_picture_link = serializers.SerializerMethodField()

    class Meta:
        model = Account
        fields = (
            'profile_picture_link',
            'name',
            'session',
            'graduation_year',
            'intake',
            'phone_number',
            'department',
            'department_full_name',
            'social',
            'jobs'
        )

    @staticmethod
    def get_department_full_name(obj: Account):
        return obj.get_department_display()

    @staticmethod
    def get_name(obj: Account):
        return f'{obj.first_name} {obj.last_name}'

    def get_profile_picture_link(self, obj: Account):
        if obj.profile_picture is None:
            obj.profile_picture.url = None
        protocol = 'https'
        request: HttpRequest = self.context['request']
        if request.is_secure() is False:
            protocol = 'http'
        return f'{protocol}://{request.get_host()}/{obj.profile_picture.url}'
