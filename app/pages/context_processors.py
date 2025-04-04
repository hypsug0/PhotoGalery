from django.conf import settings
from user.models import User


def owner_to_base(request):
    """Global template settings"""
    owner = User.objects.filter(is_photographer=True).first()
    return {"owner": owner, "title": settings.TITLE}
