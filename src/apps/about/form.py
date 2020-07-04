from django.contrib.auth import get_user_model
from django.forms import ModelForm

from apps.about.models import CarInfo
from apps.onboarding.models import Profile

User = get_user_model()


class NewCarAddForm(ModelForm):
    class Meta:
        model = CarInfo
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        user = kwargs.get("user", None)
        super(NewCarAddForm, self).__init__(*args, **kwargs)
        self.fields["user"].initial = user

    #
    # def __init__(self, *args, **kwargs):
    #     user = kwargs.pop('user')
    #     super(NewCarAddForm, self).__init__(*args, **kwargs)
    #
    # def __init__(self, user):
    #     self.user = self.request.user
    #     self.fields['user'].default = Profile.objects.get(user_id=user.id)
