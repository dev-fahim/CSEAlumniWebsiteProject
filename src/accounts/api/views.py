from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from accounts.api.serializers import ProfileCardSerializer
from accounts.models import Account


class ProfileCardDetailsAPIView(GenericAPIView):

    def get_serializer(self, *args, **kwargs):
        return ProfileCardSerializer(context={'request': self.request}, many=False)

    def get_queryset(self):
        return Account.objects.get(user=self.request.user)

    def get(self, *args, **kwargs):
        return Response(data=self.get_serializer().data)
