from django.conf.urls import url
from subjects.views import (SubjectAutocomplete,
                            CageLabelAutocomplete,
                            SubjectNicknameAutocomplete,
                            )

urlpatterns = [
    url(
        r'^subjects/$',
        SubjectAutocomplete.as_view(),
        name='subject-autocomplete',
    ),
    url(
        r'^cage-label/$',
        CageLabelAutocomplete.as_view(),
        name='cage-label-autocomplete',
    ),
    url(
        r'^subject-nickname/$',
        SubjectNicknameAutocomplete.as_view(),
        name='subject-nickname-autocomplete',
    ),
]