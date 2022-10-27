from django import forms

class login(forms.Form) :
    name = forms.CharField(required=False)
    password = forms.CharField(required=False, widget = forms.PasswordInput())

class insertProduct(forms.Form) : # 新增商品
    name = forms.CharField(required=False, label = '商品名稱')
    price = forms.CharField(required=False, label = '商品價格')
    amount = forms.CharField(required=False, label = '商品數量')

class delProduct(forms.Form) : # 刪除商品
    pId = forms.CharField(required=False, label = '商品代號')

class updateProduct(forms.Form) : # 更新商品
    pId = forms.CharField(required=False, label = '商品代號')
    name = forms.CharField(required=False, label = '商品名稱')
    price = forms.CharField(required=False, label = '商品價格')
    amount = forms.CharField(required=False, label = '商品數量')

class insertCart(forms.Form) : # 新增至購物車
    pId = forms.CharField(required=False, label = '商品代號')
    amount = forms.CharField(required=False, label = '商品數量')

class delCart(forms.Form) : # 刪除商品
    cId = forms.CharField(required=False, label = '購物車代號')

class countCart(forms.Form) : # 刪除商品
    cId = forms.CharField(required=False, label = '購物車代號')
