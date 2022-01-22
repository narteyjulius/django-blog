from django import forms
from django.conf import settings
from django.core.mail import send_mail
# from django.forms import fields
from .models import Comment, Post

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'body', 'image', 'tags', 'status')



class EmailForm(forms.Form):
    recipient = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)



class ContactForm(forms.Form):
    name = forms.CharField(max_length=120,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Full Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'E-mail'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter phone number'}))
    # inquiry = forms.CharField(max_length=70)
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Please Input Your Message'}))

    def get_info(self):
        """
        Method that returns formatted information
        :return: subject, msgut
        """
        # Cleaned data
        cl_data = super().clean()

        name = cl_data.get('name').strip()
        from_email = cl_data.get('email')
        subject = cl_data.get('phone_number')

        msg = f'{name} with email {from_email}'
        msg += f'\nPhone Number: {subject}\n\n'
        msg += cl_data.get('message')

        return subject, msg

    def send(self):

        subject, msg = self.get_info()

        send_mail(
            subject=subject,
            message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER]
        )
