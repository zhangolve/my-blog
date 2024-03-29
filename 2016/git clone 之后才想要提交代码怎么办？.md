title: git clone 之后才想要提交代码怎么办？
date: 2016-09-24 17:24:20
categories: 简述
  --- 


#问题： git clone 之后才想提交代码怎么办？

我相信很多同学跟我一样有过这样类似的经历，在github上看到一个项目，觉得很感兴趣，想要研究一番，最开始也只是star一下，这样方便以后查找，但是这样还是不过瘾，看源码还是不方便，因此就想到了git clone，将项目仓库克隆到本地观看，但是看源码的过程中发现，源码很是巧妙，不时要做一番注解，以便帮助理解，尤其是看老外的代码更是如此，毕竟注解都是英文的(所以程序猿确实要学好英语啊)。有时候，又不满足于光阅读和添加注解，还想能够在功能上做一些改动。这时候，这个仓库与之前相比已经有很大的差别了。我们还不满足于这个项目仓库只存在于我们的本地，也希望这些改动能够放到github上，虽然这些改动和注解对项目本身不会有什么帮助，但是一来方便自己以后阅读二来也有可能帮助其他学习这个项目的人。

那么现在问题就来了，由于事先考虑不周，没有采取预防措施（听起来好怪啊这句话），我们是通过 git clone命令来将该仓库下载到本地的，这个时候的remote其实是原项目地址，我们当然是不能直接git push的，因为我们并没有这样的权限。那么怎么做呢？

# git remote remove origin

通过刚才的分析，我们已经提到了，主要的问题来自于git remote的地址问题，那么我们要做的首先应该是将本地与当前远程remote切断联系，这里我参考了[ git中本地与远程库的关联与取消](http://blog.csdn.net/wsycsdn19930512/article/details/50574217) 这篇文章中提到的方法。

# fork 原项目，为本地仓库添加远程remote
到了这一步，思路就逐渐明朗了，我们刚刚切断了远程，那么现在就需要添加一个新的远程仓库，这个新的仓库从何而来呢？就需要我们对原仓库进行fork了，之后就是使用刚刚文章中提到的添加远程的方法。

    git remote add origin git@github.com:git_username/repository_name.git

# git push origin master

最后，我们就可以按照原来熟悉的套路来提交代码了。

    git add -A
    git commit -m 'what your comment is '
    git push origin master

我们知道如果我们在clone代码库到本地的时候，采用SSH加密的方式的话，在git push的时候是无须输入远程仓库的github账户密码的，SSH的写法就像下面这样：

    git@github.com:git_username/repository_name.git

但是由于我们的前提条件，并没有给我们那样的机会。因此到了git push的时候，自然还是需要我们老老实实输入账号密码的。