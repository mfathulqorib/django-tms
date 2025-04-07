from apps.delivery.models import Delivery


def undelivered_count(request):
    if request.user.is_authenticated:
        count = Delivery.objects.filter(
            is_delivered=False, person_assigned=request.user
        ).count()
    else:
        count = 0
    return {"undelivered_count": count}
