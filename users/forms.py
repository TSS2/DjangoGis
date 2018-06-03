from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','email') # 指定的字段在模板中会被渲染成表单控件 UserCreationForm默认指定了密码和确认密码