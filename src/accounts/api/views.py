from rest_framework.generics import (
    RetrieveUpdateAPIView,
    RetrieveAPIView,
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from accounts.api.serializers import (
    ProfileCardSerializer,
    AlumniSerializer,
    ProfileSerializer,
    AlumniSingleSerializer,
    JobSerializer,
    SocialLinkSerializer,
    ProfilePictureSerializer
)
from accounts.models import Account, SocialLink, JobDetail
from django.utils import timezone
from django.shortcuts import get_object_or_404
from rest_framework.parsers import FileUploadParser, ParseError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from PIL import Image


class ProfileCardDetailsAPIView(RetrieveAPIView):

    serializer_class = ProfileCardSerializer

    def get_object(self):
        return get_object_or_404(self.get_queryset(), user_id=self.request.user.id)

    def get_queryset(self):
        return Account.objects.filter(user_id=self.request.user.id)\
            .prefetch_related('jobs')\
            .select_related('social')\
            .select_related('user')


class AlumniProfileListAPIView(ListAPIView):

    serializer_class = AlumniSerializer

    def get_queryset(self):
        query_sets = Account.objects.all()\
            .prefetch_related('jobs')\
            .select_related('social')\
            .select_related('user')
        if self.request.query_params.get('recent', None) == 'true':
            query_sets = query_sets.filter(
                graduation_year__lte=timezone.now().year, graduation_year__gte=timezone.now().year-1
            )
        if self.request.query_params.get('own_batch', None) == 'true':
            query_sets = query_sets.filter(
                intake=self.request.user.account.intake
            )
        return query_sets


class AlumniProfileDetailsAPIView(RetrieveAPIView):

    serializer_class = AlumniSingleSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return Account.objects.all()\
            .prefetch_related('jobs')\
            .select_related('social')\
            .select_related('user')


class ProfileDetailsAPIView(RetrieveUpdateAPIView):

    serializer_class = ProfileSerializer

    def get_object(self):
        return get_object_or_404(self.get_queryset(), user_id=self.request.user.id)

    def get_queryset(self):
        return Account.objects.filter(user_id=self.request.user.id)\
            .prefetch_related('jobs')\
            .select_related('social')\
            .select_related('user')


class SocialLinkDetailsAPIView(RetrieveUpdateAPIView):

    serializer_class = SocialLinkSerializer

    def get_object(self):
        return get_object_or_404(self.get_queryset(), user_id=self.request.user.id)

    def get_queryset(self):
        return SocialLink.objects.filter(user_id=self.request.user.id)


class SocialLinkCreateAPIView(CreateAPIView):

    serializer_class = SocialLinkSerializer

    def get_queryset(self):
        return SocialLink.objects.filter(user_id=self.request.user.id)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, accounts=self.request.user.account)


class JobListAPIView(ListAPIView):

    serializer_class = JobSerializer

    def get_queryset(self):
        return JobDetail.objects.filter(user_id=self.request.user.id)


class JobDetailsAPIView(RetrieveUpdateDestroyAPIView):

    serializer_class = JobSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return JobDetail.objects.filter(user_id=self.request.user.id)


class JobCreateAPIView(CreateAPIView):

    serializer_class = JobSerializer

    def get_queryset(self):
        return JobDetail.objects.filter(user_id=self.request.user.id)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, accounts=self.request.user.account)


class ImageUploadParser(FileUploadParser):
    media_type = 'image/*'


class ProfilePictureUploadAPIView(RetrieveUpdateAPIView):

    parser_class = (ImageUploadParser,)
    serializer_class = ProfilePictureSerializer

    def get_object(self):
        return get_object_or_404(self.get_queryset(), user_id=self.request.user.id)

    def get_queryset(self):
        return Account.objects.filter(user_id=self.request.user.id)\
            .prefetch_related('jobs')\
            .select_related('social')\
            .select_related('user')
