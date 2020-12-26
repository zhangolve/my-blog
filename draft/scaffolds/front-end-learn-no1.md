为了实现一个类似于这个页面：https://codepen.io/FreeCodeCamp/full/YqLyXB/ 的效果，我开始从头开始设计，最初我想的是做个列表，后来发现可以用表格形式。如果使用列表的话，大概是这样的。
	
	  <div class="col-md-4">  
	  <p id=signature><a src="https://about.me/zhangolve">zhang olve</a></p>
	   </div>
	  <div class="col-md-8">
	    <ul>
	    <li>
	    <p id="aboutme">about me</p>
	    </li>
	     <li>dddd</li> 
	      </ul>
	    </div>

但是这些做法都并不简洁，表格的做法无法就是一行之内然后分出几个格子。这几个格子就代表了，后来是看了bootstrap的官方的例程。其实也用到了列表，只是这其实是一种横向的列表了

之后用到了页面内的跳转，其实是要用ID了。

	<a src="#ID">about</a>
比如上面这一行代码，about 就是导航栏上的部分，我们点击它就会跳转到对应的位置，这个对应的位置怎么确定呢？在对应的位置加上ID就ok了。比如想要跳转到一个ID为“aboutpart”的部分，就可以写成：
	
		<div id="aboutpart">
		content
		</div>




这样就可以实现跳转了。

