from django import forms
from .models import Comment, Toon

class ToonForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._widget_update()
    
    class Meta:
        model = Toon
        fields = ["titlename"]
        widgets = {
            'titlename': forms.TextInput(
                attrs={
                    'placeholder': "제목을 입력해주세요."
                }
            )
        }
    
    def _widget_update(self):
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._widget_update()
    
    class Meta:
        model = Comment
        fields = ["comment"]

    def _widget_update(self):
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
