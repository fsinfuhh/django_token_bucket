A token bucket implementation for Django to implement rate limiting
on individual user actions, for example submitting a form.

Installation
############

Insatall:

    pip install django-token-bucket

add it to your installed apps:

    INSTALLED_APPS = [
        '...',
        'django_token_bucket'
    ]

run migrations:

    ./manage.py migrate django_token_bucket


Examples
########

example for consuming a token on Form validation:

    INVITATION_MAX_TOKENS = 5
    INVITATION_FILL_RATE = 300  # a token each 300 seconds

    def clean(self):
        cleaned_data = super(InvitationForm, self).clean()
        bucket = TokenBucket.get(identifier='invitations_sent',
                           ref_object=self.user,
                           max_tokens=INVITATION_MAX_TOKENS,
                           fill_rate=INVITATION_FILL_RATE,
                           whatfor='invitations')
        try:
            bucket.consume(1)
        except bucket.TokensExceeded as e:
            raise forms.ValidationError(str(e))
        return cleaned_data
