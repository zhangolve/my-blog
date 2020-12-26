
title:  闲话OAUTH
date: 2018-12-01  09:24:49 
categories: 后端
tags: [后端] 
description: 


---



# 前面

作为一面全栈工程师(偏重前端)，对待老大交代下来的后端任务也是需要认真完成的。前段时间，有个工作，要通过淘宝的OAUTH进行授权，进而获取到access_token，通过access_token来作为授权码，进行所有需要登录权限的API访问，这些API 包括但不限于用户，商品，交易，评价，物流等API.

## 过程
在这里也无须去科普OAUTH2.0协议到底是什么了,感兴趣的可以自己去查wiki.

我来说的仍然是我自己的理解,所以OAUTH到底做了什么呢?它是一直验证机制,这个机制实现了两步验证,仍然以淘宝API获取access_token为例,淘宝认为开发者访问用户的信息,是以应用为单位的,每一个应用需要一个app_id,app_secret,我们是先要通过app_id 来置换到一个叫做code的字段,这个字段只是作为一个过渡,我们能够通过code值,再调取一个api,才能够最终获取到access_token.

拿实际例子来说,


**、授权操作步骤**

    此处以正式环境获取acccess_token为例说明，如果是沙箱环境测试，需将请求入口地址等相关数据换成沙箱对应入口地址，操作流程则同正式环境一致。
    实际进行授权操作时，测试的数据 client_id、client_secret、redirect_uri 均需要根据自己创建的应用实际数据给予替换，不能拿示例中给出的值直接进行测试，以免影响实际测试效果。下图为Server-side flow 授权方式流程图，以下按流程图逐步说明。
![授权步骤](http://upload-images.jianshu.io/upload_images/48180-daa679ca3643bb11.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

**1）拼接授权url**
拼接用户授权需访问url ，示例及参数说明如下：
https://oauth.taobao.com/authorize?response_type=code&client_id=23075594&redirect_uri=http://www.oauth.net/2/&state=1212&view=web

| 参数说明 |
| --- |
| 名称 | 是否必选 | 参数值 | 参数释义 |
| client_id | 必选 |   | 等同于appkey，[创建应用](http://open.taobao.com/doc2/detail.htm?spm=a219a.7629140.0.0.cNQJxi&treeId=1&articleId=103232&docType=1#s2)时获得。 |
| response_type | 必选 | code | 授权类型 ，值为code。 |
| redirect_uri | 必选 | 可填写应用注册时回调地址域名。 | redirect_uri指的是应用发起请求时，所传的回调地址参数，在用户授权后应用会跳转至redirect_uri。要求与应用注册时填写的回调地址域名一致或顶级域名一致 。 |
| state | 可选 | 可自定义，如1212等； | 维持应用的状态，传入值与返回值保持一致。 |
| view | 可选 | web,可选web、tmall或wap其中一种，默认为web。 | Web对应PC端（淘宝logo）浏览器页面样式；Tmall对应天猫的浏览器页面样式；Wap对应无线端的浏览器页面样式。 |

**2）引导用户登录授权**
引导用户通过浏览器访问以上授权url，将弹出如下登录页面。用户输入账号、密码点“登录”按钮，即可进入授权页面。
![授权](http://upload-images.jianshu.io/upload_images/48180-bdff42029bd50cbc.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

**3）获取code**
上图页面，若用户点“授权”按钮后，TOP会将授权码code 返回到了回调地址上，应用可以获取并使用该code去换取access_token；
若用户未点授权而是点了“取消”按钮，则返回如下结果，其中error为错误码，error_description为错误描述。分别如下图所示：![错误](http://upload-images.jianshu.io/upload_images/48180-784ed87b1c50d9ea.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

**4）换取access_token**

方式1（推荐）：

通过taobao.top.auth.token.create api接口获取access_token（授权令牌）。api服务地址参考[http://open.taobao.com/docs/doc.htm?docType=1&articleId=101617&treeId=1](http://open.taobao.com/docs/doc.htm?spm=a219a.7386781.3.7.tO1lHe&docType=1&articleId=101617&treeId=1)

## 最后

说起来,我最早使用OAUTH进行登录或者授权操作,还是早些年在用微博的时候,如果OAUTH的应用已经非常广泛了,了解它对我们,无论前端开发还是后端开发都有很多好处.

# 参考链接

http://open.taobao.com/doc.htm?docId=102635&docType=1

http://open.taobao.com/api.htm?docId=285&docType=2