from django import forms



class NumToWordForm(forms.Form):
    number=forms.IntegerField(label="enter number",widget=forms.NumberInput(attrs={"class":"form-control"}))
