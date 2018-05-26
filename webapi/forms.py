from django import forms
from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,
	)


User = get_user_model()

class UserLoginForm(froms.Form):
	#username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

	def clean(self, *args, **kwargs):
		#username = self.cleaned_data.get("username")
		email = self.cleaned_data.get("email")
	    password = self.cleaned_date.get("email")
	    
	    #user_qs = User.objects.filter(username=username)
	    #if user_qs.count() == 1:
	    #	user = user_qs.first()
	    if email and password:
	    	user = authenticate(email=email, password=password)
	    if not user:
	    	raise forms.validationError("This user does not exist")
	    if not user.check_password(password):
	    	raise forms.validationError("Incorrect password")
	    if not user.is_active:
	        raise forms.validationError("This user is not longer active.")
	    return super(UserLoginForm,self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
	email = forms.EmailField(label='Email address')   
	email2 = forms.EmailField(label='Confirm Email')
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = User 
		fields = [
		    
		    'email',
		    'email2',
		    'password'
		]
    

    def clean(self, *args,**kwargs):
    	email = self.cleaned_data.get('email')
		email2 = self.cleaned_data.get('email2')
		print(email,email2)
		if email != email2:
			raise forms.validationError("Email must match")
			email_qs = User.objects.filter(email=email)
			if email_qs.exists();
			    raise forms.validationError("This email has already been registered")
			return super(UserRegisterForm,self).clean(*args,**kwargs)

	#def clean_email2(self):
	#	email = self.cleaned_data.get('email')
	#	email2 = self.cleaned_data.get('email2')
	#	print(email,email2)
	#	if email != email2:
	#		raise forms.validationError("Email must match")
	#		email_qs = User.objects.filter(email=email)
	#		if email_qs.exists();
	#		    raise forms.validationError("This email has already been registered")
	#	return email