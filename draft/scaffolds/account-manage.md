账户管理系统



# 要求

- 能够实现账户的管理


- 账户基本属性：编码；名称，备注；状态；创建时间；账号类型等。


- 账户基本操作：增加；删除；修改；查询；封存；启封


- 查询条件：编码(模糊匹配)；名称(模糊匹配)；注册时段(开始，结束时间)；账号类型


- 基本约束：编码不能相同，不能为空

  ​

# 总体思路

- 使用Jquery和Bootstrap作为主要技术栈，通过Ajax来进行前后端的数据传递，由于我只负责前端，并没有后端服务器及相关知识，因此在这里使用了一个公开的可以进行get和post以及delete等常规操作的[API](http://rest.learncode.academy/api/learncode/friends/)。
- 在post到后端时，明确JSON对象中每一个元素的属性，在这里根据要求我设置了编码、名称、备注、创建时间、账号类型这五个属性。
- 由于要能够使用注册时段来作为查询条件，因此选用[daterangepicker](http://www.daterangepicker.com/)来进行时间段选择，根据需要也使用moment.js 来获取当前时间。
- 由于有账号类型这一条件，因此还要在账号增加时对账号类型进行选择，这里使用[select2.js](https://select2.github.io/examples.html) 进行选择。

















删除datatables中的一行：

https://datatables.net/examples/api/select_single_row.html



后来看到了这个可以增加、删除、编辑

https://editor.datatables.net/examples/api/triggerButton.html

但是有些代码看不太懂。

现在已经实现了删除，但是编辑这一块，还是不行，主要是那些代码有的没看懂，要结合后端。

在github上找到了这个库：https://github.com/ejbeaty/CellEdit 说是可以实现编辑，试试看。



在basic.html文件里看到了一行这样的代码：

<script src="https://code.jquery.com/jquery-1.12.2.min.js" integrity="sha256-lZFHibXzMHo3GGeehn1hudTAP3Sc0uKXBXAzHX1sjtk=" crossorigin="anonymous"></script>

我把那一行改成了：

<script src="http://apps.bdimg.com/libs/jquery/2.1.4/jquery.min.js"></script>

还有这样一行：

<script src="../js/dataTables.cellEdit.js"></script>

在上一级文件夹中的js文件夹里有一个dataTables.cellEdit.js



把上面的脚本放到我的项目目录下，在index.js 中增加这样一段代码：



```javascript
 var table = $('#myTable').DataTable();

table.MakeCellsEditable({
 "onUpdate": myCallbackFunction
});
```
在chrome中运行，发现错误。

​    index.js:36 Uncaught ReferenceError: myCallbackFunction is not defined



将ajax的载入数据作为注释去掉后，另外增加了一段手动填写的表格代码之后，能够实现编辑，则说明是与ajax的载入之后不能相应有关。

后来，我手动添加了一行数据，又使用Ajax导入数据，这个时候，在浏览器上呈现出来的虽然既包括我手动添加在index.html中的数据，也有后端导入的数据，但是只有手动添加的那些数据能够编辑，而调出chrome的console之后，将鼠标点击到后端导入的数据上时，console显示的是；

dataTables.cellEdit.js:93 Uncaught TypeError: Cannot read property 'column' of undefined



这说明还是JS加载顺序的问题，当dataTables.cellEdit.js 加载的时候，只有手动添加到那一行数据被赋值，进行了相关操作。具体来说：

```javascript
if (table != null) {
    // On cell click
    $(table.body()).on('click', 'td', function () {

     var currentColumnIndex = table.cell(this).index().column;
```

因为是首先加载的这个js文件，加载这个文件的时候，还没有加载我们另外一个js文件，也就还没有数据导入进来，因此这个时候表格是空的。



此路不通，再看datatables文档

看到了可以不用使用jqury的Ajax的get命令，而使用datatable这种：



    $(document).ready(function() {
    $('#example').DataTable( {
        "ajax": '../ajax/data/arrays.txt'
    } );
    } );
我之前的做法是使用jquery的$.getJSON(),然后是进行for遍历,再将获得的数据通过选择器添加到表格当中。但是这个datatables的方式很明显让代码量降低了。

但是通过看

它的JSON数据结构是这样的：

	{
	  "data": [
		[
		  "Tiger Nixon",
		  "System Architect",
		  "Edinburgh",
		  "5421",
		  "2011/04/25",
		  "$320,800"
		],
		[
		  "Garrett Winters",
		  "Accountant",
		  "Tokyo",
		  "8422",
		  "2011/07/25",
		  "$170,750"
		]]
	
	}



与我自己的JSON想要的数据结构是不符的：

```
[{"number":"2","name":"tom","note":"awnag","type":"","day":"07/19/2016","id":"578d7e061067740100bf5831"},{"number":"3","name":"lias","note":"33","type":"","day":"07/19/2016","id":"578d7edf1067740100bf5833"}]
```



在github上开issue求助，得到回复建议直接使用datatables的ajax API,因此开始做测试。

在本地建了一个data.json文件，在里面填入类似前一张图的json格式，仿写datatables的ajax调用方法，但是这时候出现Cross origin requests 不被支持。

了解到：

看HTTP访问控制(CORS)   https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Access_control_CORS

















先看一下radiogroup的相关：

```html
<form>
  <fieldset id="group1">
    <input type="radio" value="" name="group1">
    <input type="radio" value="" name="group1">
</fieldset>

<fieldset id="group2">
    <input type="radio" value="" name="group2">
    <input type="radio" value="" name="group2">
    <input type="radio" value="" name="group2">
</fieldset>
</form>
```


这是能够使用的radio button的。radio button就是用来选择的。而radiogroup就是一组radio buttons

> A group of radio buttons. Only one radio button inside the group can be selected at a time. The `radio` buttons may either direct children of the `radiogroup` or descendants. Place the `radiogroup` inside a `groupbox` if you would like a border or `caption` for the group. The `radiogroup` defaults to vertical orientation.

使用radiogroup需要用到group

来看一看例子，

```html
<groupbox>
  <caption label="Settings"/>
  <radiogroup>
    <radio label="Black and white"/>
    <radio label="Colour"/>
  </radiogroup>
  <checkbox label="Enabled"/>
</groupbox>
```

然而上面的代码也不能直接运行，需要了解XUL。他们都属于XUL范畴之内，来看看那xul定义。



> **XUL** 是一个Mozilla使用XML来描述用户界面的一种技术，使用XUL你可以快速的创建出跨平台，基于因特网的应用程序。基于XUL技术的应用程序可以很方便的使用好看的字体、图形以及方便的界面布局，而且也更容易部署和定制。如果程序员已经熟悉了Dynamic HTML ([DHTML](https://developer.mozilla.org/cn/DHTML))，那学习XUL将是更容易的事，也可以更快的开发基于XUL的应用程序.



这个XUL里的radiogroup不是我想要的。

应该还是指的一组radio buttons http://www.tuicool.com/articles/zYJvmu





其他：

- 在chrome dev console上输入指令，会输出相应的结果。比如输入某一个对象名，输出这个对象的内容。
- 可以在全局执行的内容包括全局对象（window）和this以及外部环境。什么是全局的呢？就是不在任何一个子的function里面。

