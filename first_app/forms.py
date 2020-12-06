from django import forms
from django.core import validators
from first_app import models

class MusicianForm(forms.ModelForm):
    class Meta:
        model = models.Musician
        fields = '__all__' ## creates form for all feilds
        # fields = ('first_name','last_name')  ## tuple of inclusion
        # exclude = ['instrument'] ## list of wxclusion

class AlbumForm(forms.ModelForm):
    release_date = forms.DateField( widget=forms.TextInput(attrs={'type':'Date'}) )
    class Meta:
        model = models.Album
        fields = '__all__'









def age_ccheck(value):
    if value<0 :
        raise forms.ValidationError('Age must positivev.')

def clean(self):
    all_cleaned_data = super().clean()

    user_name = all_cleaned_data['user_name']
    age = all_cleaned_data['age']

class user_form(forms.Form):
    user_name = forms.CharField( validators=[validators.MaxLengthValidator(10), ] ,
                                # label="Full Name", required=False,
                                # widget=forms.TextInput( attrs = { 'placeholder':"Enter your full name",
                                #                                     'style':"width:300px"} )
                                )
    age= forms.IntegerField(validators=[age_ccheck], required=False)
    user_dob = forms.DateField( label="Date of Birth", required=False,
                                widget=forms.TextInput( attrs = { 'type':"date"} )
                                )
    user_email = forms.EmailField( label="email", required=False,
                                    widget=forms.TextInput( attrs = {'placeholder':"Enter a valid email"} )
                                )
    boolean_field = forms.BooleanField( required=False)

    char_field = forms.CharField( max_length=15, min_length=8 , required=False )

    choices=( ('','--select option--'),
                ('1', 'halum'),
                ('2', 'agdum'),
                ('3', 'bagdum') )
    choice_field = forms.ChoiceField( choices=choices )

    choices=( ('','--select option--'),
                ('halum', 'halum'),
                ('agdum', 'agdum'),
                ('bagddum', 'bagdum') )
    choice_field = forms.ChoiceField( choices=choices,
                                        widget=forms.RadioSelect
                                    )

    choices=( ('','--select option--'),
            ('1', 'halum'),
            ('2', 'agdum'),
            ('3', 'bagdum') )
    choice_field = forms.MultipleChoiceField( choices=choices )

    choices=(('1', 'halum'),
            ('2', 'agdum'),
            ('3', 'bagdum') )
    choice_field = forms.MultipleChoiceField( choices=choices, widget=forms.CheckboxSelectMultiple )
