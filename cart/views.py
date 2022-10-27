from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
from .form import login, insertProduct, delProduct, updateProduct, insertCart, delCart, countCart

def loginPage(request) :
    cursor = connection.cursor()
    cursor.execute("select `no`, `pwd`, `title` from users;")
    all_users = cursor.fetchall()
    form_login = login(request.POST)
    if request.method == 'POST' :
        if form_login.is_valid():
            name = request.POST['name']
            pwd = request.POST['password']
            for i in range(len(all_users)):
                if (str(all_users[i][0]) == name and str(all_users[i][1]) == pwd) : # 帳密正確
                    request.session['user'] = all_users[i][0]
                    request.session['title'] = all_users[i][2]
                    if (all_users[i][2] == 'cus') :
                        return redirect('/cusMain')
                    if (all_users[i][2] == 'boss') :
                        return redirect('/bossMain')
                    #return render(request, 'main.html') 
    context = {"form_login" : form_login}
    return render(request, 'login.html', context); 

def cusMain(request) : # 顧客主頁面
    user = request.session.get('user')
    title = request.session.get('title')
    error = []
    if (user and title == 'cus') : # 是顧客
        cursor = connection.cursor()
        insert = insertCart(request.POST)
        delete = delCart(request.POST)
        count = countCart(request.POST)
        if request.method == 'POST' : # POST
            if 'insert' in request.POST : # 新增商品
               pId = request.POST['pId'] # 商品代號
               amount = request.POST['amount'] # 要多少件商品
               cursor.execute("select `stock` from product where `no` = %s", (pId,))
               product_amount = cursor.fetchone()
               if (product_amount[0] >= int(amount)) : # requirement not over the stock
                   cursor.execute("insert into shop_cart(`uId`, `pId`, `amount`) values(%s, %s, %s)", (user, pId, amount,))
               else :
                   error.append('stock is not sufficient')
            if 'delete' in request.POST : # 新增商品
               cId = request.POST['cId'] # 商品代號
               if (0 == cursor.execute('delete from shop_cart where `no` = %s and `uId` = %s', (cId, user,))) : 
                   error.append('can not delete, as no this id in your cart')
            if 'count' in request.POST : # 新增商品
               cId = request.POST['cId'] # 商品代號
               if (0 == cursor.execute('update shop_cart set `paid` = 1 where `no` = %s', (cId,))) : 
                   error.append('can not update, as no this id in your cart')
               else : # count successful
                   cursor.execute('select `pId`, `amount` from shop_cart where `no` = %s', (cId,))
                   cart_product = cursor.fetchone()
                   cart_product_pId = cart_product[0] # no of product
                   cart_product_amount = cart_product[1] # num of buying
                   cursor.execute('select `stock` from product where `no` = %s', (cart_product_pId,)) # find the stock
                   product_stock = cursor.fetchone()[0] # this product original stock
                   changed_num = product_stock - cart_product_amount # original stock - are buy
                   cursor.execute('update product set `stock` = %s where `no` = %s', (changed_num, cart_product_pId,))
        cursor.execute("select * from shop_cart where `uId` = %s and `paid` = 0", (user,)) # 該使用者還沒刪除的購物車商品
        cart_products = cursor.fetchall()
        cursor.execute("select * from product where `stock` > 0") # 還有庫存的商品
        all_products = cursor.fetchall()
        context = {'count' : count, 'delete' : delete, 'error' : error, 'user' : user, 'title' : title, 'all_products' : all_products, 'insert' : insert, 'cart_products' : cart_products}
        return render(request, 'cusMain.html', context) 
    else :
        return loginPage(request)

def bossMain(request) : # 管理者主頁面
    user = request.session.get('user')
    title = request.session.get('title')
    if (user and title == 'boss') : # 是管理者
        cursor = connection.cursor()
        insert = insertProduct(request.POST)
        delete = delProduct(request.POST)
        update = updateProduct(request.POST)
        if request.method == 'POST' :
            if 'insert' in request.POST : # 新增商品
                name = request.POST['name']
                price = request.POST['price']
                amount = request.POST['amount']
                cursor.execute("insert into product(`name`, `price`, `stock`) values(%s, %s, %s)", (name, price, amount,))
            if 'del' in request.POST : # 刪除商品
                pId = request.POST['pId']
                cursor.execute("delete from product where `no` = %s", (pId,))
            if 'update' in request.POST : # 刪除商品
                pId = request.POST['pId']
                name = request.POST['name']
                price = request.POST['price']
                amount = request.POST['amount']
                cursor.execute("update product set `price` = %s, `stock` = %s, `name` = %s where `no` = %s", (price, amount, name, pId,))
            #cursor.execute("select `no`, `name`, `title` from product;")
            #all_users = cursor.fetchall()
        cursor.execute("select * from product")
        all_products = cursor.fetchall()
        context = {'user' : user, 'title' : title, 'insertProduct' : insert, 'delProduct' : delete, 'updateProduct' : update, "all_products" : all_products}
        return render(request, 'bossMain.html', context) 
    else :
        return loginPage(request)


