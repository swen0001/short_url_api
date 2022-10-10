from django.shortcuts import redirect, render
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListCreateAPIView, RetrieveDestroyAPIView

from django.views import View
from django.conf import settings
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .models import Link
from .serializer import LinkSerializer


class ShortenerAPIView(ListCreateAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = (IsAuthenticated, )


class ShortenerAPIUpdate(UpdateAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = (IsAuthenticated,)


class ShortenerCreateAPIView(CreateAPIView):
    serializer_class = LinkSerializer
    permission_classes = (IsAuthenticated,)


class ShortenerDeleteAPIView(RetrieveDestroyAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = (IsAdminUser,)


class Redirector(View):
    def get(self, request, *args, **kwargs):
        short_link = settings.HOST_URL + '/' + self.kwargs['short_link']
        get_obj = Link.objects.filter(short_link=short_link).first()
        redirect_link = get_obj.original_link
        counter = get_obj.counter
        new_counter = Link.objects.filter(short_link=short_link).update(counter=counter + 1)
        return new_counter and redirect(redirect_link)


