from django import forms 

class submit(forms.Form):
	sender = forms.EmailField()
	link = forms.CharField(max_length=100)