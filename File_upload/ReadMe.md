
## 上传文件版本一
定义views.py
```
def upload(request):
    if request.method=="GET":
        return render(request,"upload.html")
    else:
        obj=request.FILES.get("fff")
        # obj.name 文件名
        # obj.chunks 文件块
        f = open(obj.name,'wb')
        for chunk in obj.chunks():
            f.write(chunk)
        f.close()
        return render(request,"upload.html")
```
upload.html
```
<form action="/upload/" method="post" enctype="multipart/form-data">
    {%  csrf_token %}
    <p><input type="file" name="fff"/></p>
    <p><input type="submit" value="提交"/></p>
</form>
```
## 上传文件版本二
form表单上传文件或图片无法做预览，并无法做失败验证及上传文件大小限制，那么就要用到ajax 方式发送。但这种方式兼容浏览器不好。
定义views.py
```
def upload(request):
    if request.method=="GET":
        return render(request,"upload.html")
    elif request.is_ajax():
        obj = request.FILES.get('file_obj')
        print(obj)
        f = open(obj.name, 'wb')
        for chunk in obj.chunks():
            f.write(chunk)
        f.close()
        return HttpResponse("ok")
    else:
		pass
```

```
<h1>ajax upload file</h1>
<input type="file" id="f4"/>
<a  id="btn">提交</a>
<script src="/static/jquery-1.12.4.js"></script>
<script>

    $(function () {
        $("#btn").click(function () {
            var fm=new FormData();
            fm.append('file_obj',$("#f4")[0].files[0]);
           // fm.append('file_obj',document.getElementById("f4").files[0]);
            //document.getElementById("f4")  # dom对象
            // $("#f4")                     # jquery对象
            // $("#f4")[0]                  #jquery对象转dom对象
            $.ajax({
                url:'/upload/',
                type:'POST',
                data:fm,
                processData: false,
                contentType: false,
                success:function (data) {
                    console.log(data);
                }

            })
        })
    })
</script>
```

## 上传文件版本三
伪ajax上传文件是利用form+iframe特性做的，业内都是这么做的，很重要，兼容性非常好。
先来学习下iframe标签
```
<iframe id="ifm" src="http://www.chouti.com"></iframe>
$("#ifm").attr('src', 'http://www.qq.com')  # 修改iframe src属性但页面不刷新，基于这样的特性我们可以上传文件。
```

当form表单以iframe形式发送数据到后端，后端返回的数据会在iframe body里
```
<form  id="ff1" action="/upload/" method="post" enctype="multipart/form-data" target="ifr">
    <p><input   onchange="changeImg();" type="file" name="fff"/></p>
    <p><input id="sb" type="submit" value="提交"/></p> 
</form>
<iframe id="ifm"  name="ifr" onload="sucessBack();" ></iframe>
```

那么如何取出iframe body里的值呢？
```
$("#ifm").html();  # iframe会重新生成一个子document,有html/head/body,这种方法无法取出。
```

```
$("#ifm").find('body').html(); # 有这种想法是好的，这种找只会在当前document里找，但是这样的document嵌套递归查找需要一个额外方法处理.contents()后再查找
```

```
$("#ifm").contents().find('body').html();   # iframe最终正确的方法
```
