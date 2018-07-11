# django_token_bucket

A token bucket implementation for Django to implement rate limiting
on individual user actions, for example submitting a form.

example for consuming a token on Form validation:

    INVITATION_MAX_TOKENS = 5
    INVITATION_FILL_RATE = 300  # a token each x seconds

    def clean(self):
        cleaned_data = super(InvitationForm, self).clean()
        bucket = TokenBucket.get(identifier='invitations_sent',
                           user=self.user,
                           max_tokens=INVITATION_MAX_TOKENS,
                           fill_rate=INVITATION_FILL_RATE,
                           whatfor='invitations')
        try:
            bucket.consume(1)
        except bucket.TokensExceeded as e:
            raise forms.ValidationError(e.get_message())
        return cleaned_data
