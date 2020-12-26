在Ajax中A代表的是异步（**asynchronous**），这意味着发送请求（或者是接收相应）是在正常的程序流之外的，比如，$.ajax 很快地返回了，下一个状态是return result;这条命令被执行是在你传递这个方法之前，这个时候success 已经被调用了。

同步的情况是这样的：

想象你正在给一个朋友打电话问他一些事情，由于它需要一定的时间，所以你需要等在电话机旁，直到你的朋友给你所需要的答案。

http://stackoverflow.com/questions/14220321/how-do-i-return-the-response-from-an-asynchronous-call



http://cnn237111.blog.51cto.com/2359144/1038080