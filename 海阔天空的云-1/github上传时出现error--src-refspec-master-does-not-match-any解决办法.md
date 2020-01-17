1 error:src refspec master does not match any 
这个问题，我之前也遇到过，这次又遇到了只是时间间隔比较长了，为了防止以后再遇到类似问题，还是把这个方法简单记录在此。

当然，是通过搜索引擎找到的答案，开始用谷歌，我以为stackoverflow会很权威的，结果在这上面没有找到合适的。

http://stackoverflow.com/questions/21264738/error-src-refspec-master-does-not-match-any
反倒是换用百度输入，查看中文的东西才解决了这个问题。
>问题产生 

>原因分析 

>引起该错误的原因是，目录中没有文件，空目录是不能提交上去的 
 


 >解决方法


>     touch README
    git add README 
    git commit -m 'first commit'
    git push origin master
 
来自：http://www.open-open.com/lib/view/open1366080269265.html
实际上
    



     git init
这一步之后创建了一个名为.git的文件夹，不过它在默认状态下是隐藏的，系统将隐藏文件夹显示出来，可以看到有这样一个文件夹。
github上传项目方法：
http://www.oschina.net/question/159132_86728
 在你的电脑上装好git

大致流程是：

>1、在github上创建项目

>2、使用git clone https://github.com/xxxxxxx/xxxxx.git克隆到本地

>3、编辑项目

>4、git add . （将改动添加到暂存区）

>5、git commit -m "提交说明"

>6、git push origin master 将本地更改推送到远程master分支。

>这样你就完成了向远程仓库的推送。 

如果在github的remote上已经有了文件，会出现错误。此时应当先pull一下，即：
     

    git pull origin master

然后再进行：

    git push origin master



--------------------------------------分割线---------------------------------------------------------
如果您喜欢本文，可以点下面的喜欢按钮，也可以关注[本人简书](http://www.jianshu.com/users/1c26e9e36267/latest_articles)
或简书专题：[我们在自己的世界里独自狂欢](http://www.jianshu.com/collection/7b424559990a)

也可以订阅我的微信公众号，了解更多内容。

![海阔天空的云](http://upload-images.jianshu.io/upload_images/48180-a0c932d9584e9684.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
