
from django.db.models import Model
from django.db.models.query import QuerySet


class PrivateModelViewSetQuerySetGetter:
    model: Model

    def get_queryset(self) -> QuerySet:
        user = self.request.user
        return self.model.objects.filter(user=user)