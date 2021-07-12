from .models import Profile, Relationship


def profile_pic(request):
    if request.user.is_authenticated:
        profile_obj = Profile.objects.get(user=request.user)
        picture = profile_obj.avatar
        return {'picture': picture}
    return {}


def invatations_received_no(request):
    if request.user.is_authenticated:
        profile_obj = Profile.objects.get(user=request.user)
        qs_count = Relationship.objects.invatations_received(profile_obj).count()
        return {'invites_num': qs_count}
    return {}
