# Import of Forms
from django import forms
from django.forms import ModelForm, Form, ModelChoiceField, CharField, TextInput


# Importación de Módulos
from datetime import datetime
from django.forms import widgets
from django.utils import timezone

from .models import Category, Estados, Locality, Province, client, Production, Sale

# Functions
from .functions import(
    alphabet_category_name,
    alphabet_name,
    alphabet_name2,
    alphabet_number_size,
    alphabet_surname,
    alphabet_department,
    alphabet_province,
    cod_postal,
)

# FORM CATEGORY / TIPO DE PRENDA
class CategoryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #     form.field.widget.attrs['class'] = 'form-control'
        #     form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Type of garment',
                    'autocomplete':'off',
                }
            ),
            'categorysize': forms.TextInput(
                attrs={
                    'placeholder':'Size',
                    'class': 'form-control',
                }
            ),
        }
    
    def clean_name(self):
        tipo_producto = self.cleaned_data["name"]
        alfabeto = tipo_producto.upper()
        flag = alphabet_category_name(alfabeto)
        if flag == True:
            return alfabeto
        else:
            raise forms.ValidationError('Solo se permiten letras o espacios.')
    
    def clean_categorysize(self):
        talle = self.cleaned_data["categorysize"]
        alfabeto = talle.upper()
        flag = alphabet_number_size(alfabeto)
        if flag == True:
            return alfabeto
        else:
            raise forms.ValidationError('Cantidad: No puede estar vacio. Solo se permiten letras, números o espacios')
    
    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
  

# FORM STATES
class RegisterStatesUpDateForm (ModelForm):
    
    class Meta:
        model = Estados
        fields = (
            'state_type',
        )
        widgets={
            'state_type': forms.TextInput(
                attrs={
                    'placeholder':'Tipo de Estado',
                    'class':'form-control',
                }
            ),

        }


# FORM LOCALITY / DEPARTMENT / PARTIDO (BsAs)
class LocalityForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #     form.field.widget.attrs['class'] = 'form-control'
        #     form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Locality
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Department',
                    'class':'form-control',
                }
            ),
        }
    
    def clean_name(self):
        localidad = self.cleaned_data["name"]
        alfabeto = localidad.upper()
        flag = alphabet_name(alfabeto)
        if flag == True:
            return alfabeto
        else:
            raise forms.ValidationError('Solo se permiten letras o espacios.')
    
    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
    
    # def clean_department(self):
    #     departamento=self.cleaned_data["department"]
    #     departamento_upper=departamento.upper()
    #     return departamento_upper

    #     # largo=len(departamento)
    #     # if largo>0:
    #     #     alfabeto = departamento.upper()
    #     #     flag = alphabet_department(alfabeto)    
    #     #     if flag == True:
    #     #         return alfabeto
    #     #     else:
    #     #         raise forms.ValidationError('Departamento: Solo se permiten letras o espacios.')
    #     # elif largo==0:
    #     #     alfabeto = ''


# FORM PROVINCE
class ProvinceForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #     form.field.widget.attrs['class'] = 'form-control'
        #     form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Province
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Province',
                    'class':'form-control',
                }
            ),
        }
    
    def clean_name(self):
        provincia = self.cleaned_data["name"]
        alfabeto = provincia.upper()
        flag = alphabet_name(alfabeto)
        if flag == True:
            return alfabeto
        else:
            raise forms.ValidationError('Solo se permiten letras o espacios.')
    
    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

    # def clean_province(self):
    #     province = self.cleaned_data["province"]
    #     province_upper = province.upper()
    #     return province_upper
    #     # largo = len(province)
    #     # if largo>0:
    #     #     alfabeto = province.upper()
    #     #     flag = alphabet_province(alfabeto)
    #     #     if flag == True:
    #     #         return alfabeto
    #     #     else:
    #     #         raise forms.ValidationError('Provincia: Solo se permiten letras o espacios.')
    #     # elif largo==0:
    #     #     alfabeto = ''
    #     # return alfabeto


# FORM CLIENTS
class RegisterClientsAddForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['surname'].widget.attrs['autofocus'] = True
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = client
        fields = (
            'surname',
            'name',
            'gender',
            'mobile',
            'phone',
            'email',
            'address',
            'department',
            'neighborhood',
            'localities',
            'province',
            'postal_code',
            'others',
        )

        widgets ={
            'surname': forms.TextInput(
                attrs={
                    'placeholder':'Surname',
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'placeholder':'Name',
                }
            ),
            'mobile': forms.NumberInput(
                attrs={
                    'placeholder':'Mobile',
                }
            ),
            'phone': forms.NumberInput(
                attrs={
                    'placeholder':'Phone',
                }
            ),
            'email':forms.EmailInput(
                attrs={
                    'placeholder':'Email',
                }
            ),
            'address': forms.TextInput(
                attrs={
                    'placeholder':'Address',
                }
            ),
            'department': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'neighborhood': forms.TextInput(
                attrs={
                    'placeholder':'Neighborhood',
                }
            ),
            'localities': forms.TextInput(
                attrs={
                    'placeholder':'Locality',
                }
            ),
            'province': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'postal_code': forms.NumberInput(
                attrs={
                    'placeholder':'Postal Code',
                }
            ),
            'others': forms.Textarea(
                attrs={
                    'placeholder':'Otros datos sobre el cliente',
                    'rows': '3',
                }
            ),
        }

    # GUARDADO DE DATOS
    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

    # VALIDACIONES
    def clean_surname(self):
        surname = self.cleaned_data["surname"]
        alfabeto = surname.upper()
        flag = alphabet_surname(alfabeto)
        if flag == True:
            return alfabeto
        else:
            raise forms.ValidationError('Apellido: Solo se permiten letras o espacios.')

    def clean_name(self):
        name = self.cleaned_data["name"]
        alfabeto = name.upper()
        flag = alphabet_name(alfabeto)
        if flag == True:
           return alfabeto
        else:
            raise forms.ValidationError('Nombre: Solo se permiten letras o espacios.')   

    # def clean_mobile(self):
    #     mobile = self.cleaned_data["mobile"]
    #     if len(mobile) <=20:
    #         return mobile
    #     else:
    #         raise forms.ValidationError( 'Móvil: Ha superdo los 20 caractéres. ')

    # def clean_phone(self):
    #     phone=self.cleaned_data[ "phone"]
    #     if len(phone) <=20:
    #         return phone
    #     else:
    #         raise forms.ValidationError( 'Teléfono: Ha superdo los 20 caractéres. ')

    # def clean_email(self):
    #     email= self.cleaned_data["email"]
    #     return email

    # def clean_postal_code(self):
    #     codigo_postal = self.cleaned_data["postal_code"]
    #     flag = cod_postal(codigo_postal)
    #     if flag == True:
    #         return codigo_postal
    #     else:
    #         raise forms.ValidationError('Código Postal: Solo se permiten números')

    def clean_address(self):
        direccion=self.cleaned_data["address"]
        direccion_upper=direccion.upper()
        return direccion_upper
    
    def clean_neighborhood(self):
        barrio = self.cleaned_data["neighborhood"]
        barrio_upper = barrio.upper()
        return barrio_upper
        
    def clean_localities(self):
        localidad = self.cleaned_data["localities"]
        localidad_upper = localidad.upper()
        return localidad_upper

    
# FORM PRODUCCIÓN
class RegisterProductionAddForm (ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True
            
    class Meta:
        model = Production
        fields = (
            'cat',
            'name',
            'size',
            'observation',
            'amount',
            'state',
            'product_price',
            'today_date',
            'due_date',
            'image',
        )
        widgets={
            'cat': forms.Select(
                attrs={
                    'class': 'select2',
                    'style': 'width: 100%'
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'placeholder':'Product Description',
                    'class': 'form-control',
                }
            ),
            'size': forms.TextInput(
                attrs={
                    'placeholder':'Size',
                    'class': 'form-control',
                }
            ),
            'observation': forms.Textarea(
                attrs={
                    'placeholder':'Observation',
                    'class': 'form-control',
                    'rows': '3',
                }
            ),
            'amount': forms.NumberInput(
                attrs={
                    'placeholder':'Amount',
                    'class': 'form-control',
                }
            ),
            'today_date': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'value': datetime.now().strftime('%Y-%m-%d'),
                    'autocomplete': 'off',
                    'class': 'form-control datetimepicker-input',
                    'id': 'today_date',
                    'data-target': '#today_date',
                    'data-toggle': 'datetimepicker'
                }
            ),
            'due_date': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'value': datetime.now().strftime('%Y-%m-%d'),
                    'autocomplete': 'off',
                    'class': 'form-control datetimepicker-input',
                    'id': 'due_date',
                    'data-target': '#due_date',
                    'data-toggle': 'datetimepicker'
                }
            ),            
        }
    
       #tipo_producto = self.cleaned_data["product_type"]
       #largo = len(tipo_producto)

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

    def clean_name(self):
        descrip_product = self.cleaned_data["name"]
        alfabeto = descrip_product.upper()
        flag = alphabet_name2(alfabeto)
        if flag == True:
            return alfabeto
        else:
            raise forms.ValidationError('Tipo Prenda: Solo se permiten letras, números, espacios, -, +, . , ( )')

    def clean_size(self):
        talle = self.cleaned_data["size"]
        alfabeto = talle.upper()
        flag = alphabet_number_size(alfabeto)
        if flag == True:
            return alfabeto
        else:
            raise forms.ValidationError('Cantidad: No puede estar vacio. Solo se permiten letras, números o espacios')
    
    def clean_amount(self):
        cantidad = self.cleaned_data["amount"]
        return cantidad
    

    #def clean_today_date(self):
    #    fecha_hoy = timezone.now().date().strftime("%d-%m-%Y")   
    #   return fecha_hoy


# FORM DESIGN / IMPRESSION / MAKING / SUBLIMATIONS
class EditDesignImpressionMakingSublimationsForm (ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            
    class Meta:
        model = Production
        fields = (
            'cat',
            'name',
            'size',
            'amount',
            'state',
            'observation',
            'image',
        )
        widgets={
            'name': forms.TextInput(
                attrs={
                    'placeholder':'Product Description',
                }
            ),
            'size': forms.TextInput(
                attrs={
                    'placeholder':'Size',
                }
            ),
            'amount': forms.NumberInput(
                attrs={
                    'placeholder':'Amount',
                }
            ),
            'observation': forms.Textarea(
                attrs={
                    'placeholder':'Observation',
                    'rows': '3',
                }
            ),
        }
    
       #tipo_producto = self.cleaned_data["product_type"]
       #largo = len(tipo_producto)

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

    def clean_name(self):
        descrip_product = self.cleaned_data["name"]
        alfabeto = descrip_product.upper()
        flag = alphabet_name2(alfabeto)
        if flag == True:
            return alfabeto
        else:
            raise forms.ValidationError('Tipo Prenda: Solo se permiten letras, números, espacios, -, +, . , ( )')

    def clean_size(self):
        talle = self.cleaned_data["size"]
        alfabeto = talle.upper()
        flag = alphabet_number_size(alfabeto)
        if flag == True:
            return alfabeto
        else:
            raise forms.ValidationError('Cantidad: No puede estar vacio. Solo se permiten letras, números o espacios')
    
    def clean_amount(self):
        cantidad = self.cleaned_data["amount"]
        return cantidad
    

    #def clean_today_date(self):
    #    fecha_hoy = timezone.now().date().strftime("%d-%m-%Y")   
    #   return fecha_hoy
    

# FORM SALE
class SaleForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Sale
        fields = '__all__'
        widgets = {
            'cli': forms.Select(attrs={
                'class': 'form-control select2',
                'style': 'width: 100%'
            }),
            'date_joined': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'value': datetime.now().strftime('%Y-%m-%d'),
                    'autocomplete': 'off',
                    'class': 'form-control datetimepicker-input',
                    'id': 'date_joined',
                    'data-target': '#date_joined',
                    'data-toggle': 'datetimepicker'
                }
            ),
            'iva': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'subtotal': forms.TextInput(
                attrs={
                    'readonly': True,
                    'class': 'form-control',
                }
            ),
            'total': forms.TextInput(
                attrs={
                    'readonly': True,
                    'class': 'form-control',
                }
            )
        }



class SaleProductionStockForm(Form):
    categories = ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control select2',
        'style': 'width: 100%'
    }))

    products = ModelChoiceField(queryset=Production.objects.none(), widget=forms.Select(attrs={
        'class': 'form-control select2',
        'style': 'width: 100%'
    }))

    search = CharField(widget=TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ingrese una descripción'
    }))

    # search = ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={
    #     'class': 'form-control select2',
    #     'style': 'width: 100%'
    # }))




    # cli = forms.Select(attrs={
    #             'class': 'form-control select2',
    #             'style': 'width: 100%'
    # })

    # date_joined= forms.DateInput(
    #             format='%Y-%m-%d',
    #             attrs={
    #                 'value': datetime.now().strftime('%Y-%m-%d'),
    #                 'autocomplete': 'off',
    #                 'class': 'form-control datetimepicker-input',
    #                 'id': 'date_joined',
    #                 'data-target': '#date_joined',
    #                 'data-toggle': 'datetimepicker'
    #             }
    # )

    # iva = forms.TextInput(
    #             attrs={
    #                 'class': 'form-control',
    #             }
    # )
    
    # subtotal = forms.TextInput(
    #             attrs={
    #                 'readonly': True,
    #                 'class': 'form-control',
    #             }
    # )

    # total = forms.TextInput(
    #             attrs={
    #                 'readonly': True,
    #                 'class': 'form-control',
    #             }
    # )