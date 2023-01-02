from django import forms

from .models import User,Task

class SignupForm(forms.ModelForm):
    #Password field
    pwd = forms.CharField(widget=forms.TextInput(attrs={"type":"password"}))

    required_css_class = "required-field"
    error_css_class = "error-field"
    class Meta:
        #Bringing all data
        model = User
        fields = '__all__'

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        # self.fields["pwd"].widget.attrs.update({"type": "password"})

        label = ["First name","Last name", "Email", "Phone Number","Password"]
        pholder = ["First name...","Last name...", "Email@gmail.com", "1234567890","Your password"]
        i = 0

        for field in self.fields:
            self.fields[str(field)].widget.attrs.update({"class":"form-control mt-2 mb-2 form-control-md"})
            self.fields[str(field)].label = label[i]
            self.fields[str(field)].widget.attrs.update(placeholder = str(pholder[i]))
            i += 1

class LoginForm(forms.ModelForm):
    pwd = forms.CharField(widget=forms.TextInput(attrs={"type":"password"}))

    required_css_class = "required-field"
    error_css_class = "error-field"
    class Meta:
        #Bring the two data to use
        model = User
        fields = ["email","pwd"]

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        # self.fields["pwd"].widget.attrs.update({"type":"password"})

        label = ["Email Adress","Password"]
        pholder = ["sombody@mail.com","Your passowrd"]
        i = 0

        for field in self.fields:
            self.fields[str(field)].widget.attrs.update({"class":"form-control mt-2 mb-2 form-control-md"})
            self.fields[str(field)].label = label[i]
            self.fields[str(field)].widget.attrs.update(placeholder=str(pholder[i]))
            i += 1

class AddTaskForm(forms.ModelForm):
    date = forms.DateTimeField(widget=forms.DateInput(attrs={"type":"date"}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={"type":"time"}))

    required_css_class = "required-field"
    error_css_class = "error-field"
    class Meta:
        model = Task
        fields = ["title","description","date","time"]

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        # self.fields["date"].widget.attrs.update({"type":"date"})
        # self.fields["time"].widget.attrs.update({"type":"time"})
        labels = ["Title", "Description", "Date","Time"]
        i = 0

        for field in self.fields:
            self.fields[str(field)].widget.attrs.update({"class":"form-control mt-2 mb-2 form-control-md"})
            self.fields[str(field)].label = labels[i]
            i += 1
