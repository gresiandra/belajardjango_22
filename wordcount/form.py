from django import forms

class wordcountForm(forms.Form):

    words = forms.CharField(
        label = 'Input your words here:',
        widget = forms.Textarea(
                    attrs = {
                        'class':'form-control',
                        'placeholder':'input words here'
                    }
            )
    )