from django import  forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProduct(forms.Form):
    #限制用户选择的数量1-20个之间
    quality=forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    #update用于是在原理基础上修改还是之间替代原来的数量
    #forms.HiddenInput把这个字段隐藏
    update=forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
