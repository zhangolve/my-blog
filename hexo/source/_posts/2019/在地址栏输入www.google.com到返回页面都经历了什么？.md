title: 在地址栏输入www.google.com到返回页面都经历了什么？
date: 2019-09-23 20:43:58
categories: 简述

--- 



路径

- 硬件角度
- 网络安全角度
- 后端角度
- 前端角度
科普，用最简洁的语言说明复杂的原理。

# 硬件角度

1. 输入到识别

每次输入的过程，都是硬件之间交互的过，是键盘与显示终端交互的过程。如果有外接键盘的话，情况会更加复杂一些。外接键盘，又分为有线键盘和蓝牙无线键盘等。具体来说，无论是有线键盘，还是蓝牙键盘，都需要在电脑上安装驱动程序，让计算机能够识别到这个键盘的存在。只是说蓝牙键盘，这个设备并没有直接与计算机产生联系，而是通过另一种网络来传递信号。这个时候，传递的速度，可能赶不上有线键盘那么快。

键盘的输入，是电信号。电信号需要转化成数字信号，才能够最终被计算机识别，再呈现在显示屏上面。以前我们说，计算机主要由四个部分组成，主机，显示器，键盘，鼠标，其中，显示器，键盘，鼠标都是外部设备，只有主机才是核心设备。主机又可以细分为CPU，硬盘，显卡，内存，散热器等等。我们键盘输入，最后文字显示在显示器上面的过程，其实是包含了主机计算的过程，由键盘先到主机，再到显示器。

输入结束之后，接下来，如果我们按下了回车键，这个时候，就又与前端知识相关联了。

## 浏览器

浏览器是个啥，浏览器是一个电脑应用程序，它的作用就是展示网页。网页，也就是HTML，超文本标记语言，我们按照约定,这个约定就是这门语言，HTML，这个约定告诉我们应该怎样书写，才能够实现我们想要的布局，排版。网页作为一个载体，需要承载的内容会非常多，非常全面，它需要支持文字，视频，音频等众多媒体形式，这也就决定了浏览器需要支持这些内容的展示。于是，如果你细心的话，你会发现：如果你的电脑上没有安装视频播放器或者图片预览器，那么随便找一个MP4格式的视频，或者一jpeg格式的图片，直接将他们拖动到浏览器中，都是能够播放或查看的。注意，我这里特别强调了视频或图片的格式，并不是所有的视频格式的视频都能够在浏览器上面播放，浏览器并不是专业的视频播放器，它还要好多其他的重要任务，因此它只约定播放某些特定格式的视频资源。

当我们按下回车键的时候，浏览器就认为你的输入已经完成，可以跳转到输入的网址了。



一旦建立起了通信，这个时候，服务端得到了客户端的请求了.但是还有一个问题，就是我们在浏览器地址栏输入的其实是域名，而服务器真正认识的是ip地址，这里就有一个DNS的过程了。所谓的DNS，就是domain name system。我在写到这里的时候，以为是domain name service，只是一个服务，而不是一个系统了。因为DNS确实也只是做了一件事情，那就是把域名解析为ip地址。

浏览器又做了什么事情呢，在此过程之中？

一、浏览器解析域名一般包含以下步骤。

1.浏览器查询自身的DNS缓存。没找到继续。

2.浏览器向本机查询域名对应ip地址。windows操作系统的域名和IP的映射关系存在host文件中。没找到继续。

3.本机向本地的DNS服务器请求解析。本地的服务器一般指公司，学校或者运营商的DNS。没找到继续。

4.本地的DNS服务器向根服务器发起解析请求，返回顶级国际域名服务器解析地址。继续。

5.本地的DNS服务器向顶级域名服务器地址请求解析，返回域名服务商的解析地址。继续。

6.本地的DNS服务器向域名服务商请求解析，得到对应的ip，告知浏览器。

本地域名服务器 (本地DNS) 是什么鬼？我们通过网络属性看一看↓↓↓

![v2-727c5491ef9501f7f7a53efdec8ed969_hd.jpg](https://upload-images.jianshu.io/upload_images/48180-024ec64f805c3bb0.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


通过DNS的过程，找到ip地址。

但是这个过程其实是相对的，客户端当然想去找到一个ip地址，但是服务端也当然希望找到一个能够让客户端访问速度最快的ip给到客户端。现在很多大型网站，都有很多的ip地址。把访问最快的ip给到客户端当然最好。


DNSPod 是一款免费智能DNS产品。DNSPod 可以为同时有电信、网通、教育网服务器的网站提供智能的解析，让电信用户访问电信的服务器，网通的用户访问网通的服务器，达到互联互通的效果。能够让使用 双线路或拥有多镜像的网站站长轻松实现智能DNS解析，让用户仅用单域名即可访问到最快速的镜像。

这个问题，也跟国情有关系，我国的网络情况，再我天朝，各个运营商控制的网络之间进行通信，往往速度会差很多。单个运营商网络内部的通信，才能够保证速度。因此，如果我们留心发现，也能够看到在一些资源下载网站，时至今日还会在下载的位置提供多个下载按钮，每一个按钮对应一条线路，也就对应了一个下载服务器，其原因，也是想优化用户的体验。然而，其实说起来，大部分用户都是小白，他们可能也就随便找条线路下载罢了。

总之，DNS的过程是双向的，客户端在努力去找到访问最好的服务端线路，服务端也想提供一条最好的线路给客户端 。

现在DNS的问题解决了，我们已经能够根据地址栏上输入的www.google.com 去找到它的真实ip地址了。这个时候，还有一个小问题，假如我们输入的是http://www.google.com ，那么如果是在chrome最新版浏览器(version 76)上，会优先去寻找它的https站点，从地址栏上可以看到这些变化，地址栏上去掉了http://www.这部分内容，在google.com前面加了一把锁，指示这时候已经用上了https。

我们可以进一步拓展一下，


https有证书。

http 默认监听80端口
https 默认监听443端口。在http下加入了ssl层，https的安全基础是https。

如果攻击者截取了web浏览器和网站服务器之间的传输报文，就可以直接读懂其中的信息。


https的缺点：

https证书需要钱，https连接缓存不如http高效，会增加数据开销和功耗。https握手阶段比较费时，会使页面加载时间延长，会更耗电。


* http承载层是tcp层,https是在http协议之上加了一个ssl，tsl安全协议层。

* http的默认端口号是80端口，https协议的默认端口号是443端口

为什么说https更加安全呢，普通的架构在http协议之上的网站，他是可以通过运营商劫持来给网站注入内容的，运营商或者其他人也是可以直接来得到你的访问的具体内容。如果你在这个网站有用户名密码等信息，很有可能会泄漏。但是https的话，是不存在运营商挟持的问题的。整个数据的传输过程，只有你和站点才有密钥。


像chrome这样的浏览器，在推动着web安全的发展，之前也是chrome最早将非https的站点，标记为不安全的。这样看来，https是大势所趋。

有了https，可以简单地理解为报文非明文传输，而是在传输过程中经过了一层加密。


## 请求

好了，好了，现在双方已经建立起了桥梁，可以互相通信了。


随着网络情况越来越好，浏览器上出现的空白页非常短，随即就展示了谷歌的网站首页。那么浏览器又是怎么做到的呢？这就牵扯到了另外一门计算机课程，《计算机网络》。

计算机科学的发展，是建立在种种的协议和标准之上的。到我们现在要谈论的这个话题上，用到了TCP/IP 协议，这个协议规定了两台计算机之间如何通信。下面具体来说一说，所谓的TCP/IP协议，分为两部分，TCP协议规定了中间过程的实现，IP协议规定了怎样找到对方，给对方发送信息。

知道了这些，就可以详细点来解答我们的问题了。首先，当你在浏览器上完成输入，敲击回车键的时候，随即浏览器作为客户端，就向服务端发送了一条请求，希望能够得到谷歌首页的网页响应。

对于新同学来讲，可能又懵逼了。这些客户端，服务端又是啥。毫无疑问，这也是计算机科学里面的术语。他们都描述了计算机的状态，如果换到我们经常使用的场景来看，如果你玩《和平精英》这样的游戏的话，那么我们自己的每一台手机都是客户端，相对应的，在腾讯那里，也将会有数不清的服务端机器，也就是服务器来做支撑，确保我们的游戏体验顺畅。客户端和服务端就像是它们各自的名字所描述的那样，一个负责服务他人，一个负责享受服务。其实有点像是你去餐馆吃饭，点菜的过程，就是客户端向服务端发送请求的过程，服务端当然也会有应答，也会最终上来一大桌美食。

切回到我们说的实际工作，客户端与服务端之间要进行通信，服务端才能够将信息发送给客户端。然而，客户端与服务端又不能是简单通信，需要进行三次握手，这是一个授信的过程，目的就是确保我信任你。


七层的协议。那么又在第几层呢？又经历了三次握手，最后才终于建立了联系。

TCP协议，


## 返回内容

报文的内容是怎样的呢？

请求头，请求的body

HTTP Request
HTTP 的请求报文分为三个部分 请求行、请求头和请求体。

其中请求头说的是请求的基本信息，请求体说的是携带的大量信息。请求行

具体的可以参见这篇文章： [https://segmentfault.com/a/1190000006689767](https://segmentfault.com/a/1190000006689767)


有请求，当然也要有响应。

响应也是如是一样，分为响应头，响应体。

在响应头，又有很多常规的字段，来说明一些常规事情，比如响应状态，status 200 ok等等。为什么要设计成响应头和响应体这样的区分开来的响应结构呢？我们可以结合实际调用来看，如果我们有一个接口，一般来说，我们会把结构的返回值，放到响应体中，而把其他的信息放到响应头之中，有个响应头，我们可以鉴权，可以判断响应是否正常，而把这两部分分开有助于我们代码的书写。




## 回传部分

这里涉及到一些网页基础知识。前面其实已经简单介绍了浏览器，接下来就说一说网页，我们必须承认今天看到的网页，已经远比20年前要更加复杂了，这种复杂度，从表面上看来，体现在网页更加酷炫，现代化，而从更深层次来看，则体现了网页前端技术的变革。然而，我也不打算在这里再拓展到前端技术变革的话题，我想说的是，无论技术如何变革，网页这个诞生三十年左右的事物，也始终是核心是由三部分组成。即HTML,JS,CSS，这三部分是网页技术的核心。

一般来说，每一个网页，就是一个html页面。HTML是基本，JS和CSS只不过是潜入在HTML页面内部而已，只不过相比于其他的潜入资源，比如视频，音频，图片等多媒体资源用于作为内容来进行展示，JS和CSS的作用并不是作为内容，而是辅助内容去进行展示，甚至是进行交互。(展示还只是UI层面，交互就是UE层面的事情了)。

如果我们探寻，网页技术的历史，很有意思。网页（HTML）的发明是在20世纪90年代初

根据维基百科：

[HTML](https://zh.wikipedia.org/wiki/HTML "HTML")规范虽然规定了网页中的标题、段落应该使用的标签，但是没有涉及这些内容应该以何种样式(比如大小、位置、间距、缩进等属性)呈现在浏览器中。从1990年代初HTML被发明开始，[样式表](https://zh.wikipedia.org/wiki/%E6%A0%B7%E5%BC%8F%E8%A1%A8 "样式表")就以各种形式出现了。不同的浏览器结合了它们各自的样式语言，读者(也就是浏览网页的用户)可以使用这些样式语言来调节网页的显示方式。一开始样式表是给读者用的，最初的HTML版本只含有很少的显示属性，读者来决定网页应该怎样被显示。

1993年，Robert Raisch提出了一种名为“RRP”的样式规则建议。但这个RRP只允许网页使用1个样式表，不像现在的CSS能支持同时加载多个。不久后出现的[Mosaic](https://zh.wikipedia.org/wiki/Mosaic "Mosaic")浏览器就采用增加新种类的HTML标签实现样式的表达，以满足设计师的要求，这也与现在的CSS设计原则不符。随着HTML自带的样式功能的增加，外来定义样式的语言逐渐减弱了。1993年发布的这个Mosaic浏览器是第一款用户界面，并支持书签、图标按钮和图片显示。<sup>[[8]](https://zh.wikipedia.org/wiki/%E5%B1%82%E5%8F%A0%E6%A0%B7%E5%BC%8F%E8%A1%A8#cite_note-8)</sup>之前的浏览器都是纯文字浏览器。即使在今天，只使用操作系统命令行自带的[Telnet](https://zh.wikipedia.org/wiki/Telnet "Telnet")命令，也可以查看网页的源代码。<sup>[[9]](https://zh.wikipedia.org/wiki/%E5%B1%82%E5%8F%A0%E6%A0%B7%E5%BC%8F%E8%A1%A8#cite_note-9)</sup>

后来，台湾人[魏培源](https://zh.wikipedia.org/wiki/%E9%AD%8F%E5%9F%B9%E6%BA%90 "魏培源")开发的[ViolaWWW](https://zh.wikipedia.org/wiki/ViolaWWW "ViolaWWW")浏览器使用了一种规则具有层次嵌套性的样式表，并第1个支持通过`<link>`标签引用外部样式表。FOSI最早支持以相对尺寸值来表示字体大小。函数式风格的DSSSL语言支持在样式表中进行定义变量、继承变量、定义函数等功能，但是语法复杂。1994年，万维网之父[蒂姆·伯纳斯-李](https://zh.wikipedia.org/wiki/%E8%92%82%E5%A7%86%C2%B7%E4%BC%AF%E7%BA%B3%E6%96%AF-%E6%9D%8E "蒂姆·伯纳斯-李")在欧美众多[高能物理](https://zh.wikipedia.org/wiki/%E9%AB%98%E8%83%BD%E7%89%A9%E7%90%86 "高能物理")研究者和技术人员的支持下，于美国[麻省理工学院](https://zh.wikipedia.org/wiki/%E9%BA%BB%E7%9C%81%E7%90%86%E5%B7%A5%E5%AD%A6%E9%99%A2 "麻省理工学院")创立了[万维网联盟](https://zh.wikipedia.org/wiki/%E4%B8%87%E7%BB%B4%E7%BD%91%E8%81%94%E7%9B%9F "万维网联盟")（W3C），其职责是提供网络标准化建议。<sup>[[10]](https://zh.wikipedia.org/wiki/%E5%B1%82%E5%8F%A0%E6%A0%B7%E5%BC%8F%E8%A1%A8#cite_note-%E7%AB%99%E9%95%BF%E4%B9%8B%E5%AE%B6_Web%E6%A0%87%E5%87%86%E6%BC%94%E5%8C%96-10)</sup>1994年，Håkon W Lie提出层叠HTML样式表（Cascading HTML Style Sheets，CHSS）。CHSS既支持用户自定义样式表，也支持网页作者样式表，而且可以满足不同规则以百分比的方式组合使用。它的权重规则计算方式不够直观，当不同规则混合时会得到什么实际效果并不容易从代码中看出。1996年，出现了与CSS语法很像的表现指明语言（Presentation Specification Language，简称"PSL 96"）。PSL 96除表达样式外，也支持条件判断等功能，还可根据对浏览器信息的判断来使用不同的样式，但未获得青睐。

其实可以看出来，如果简单地去认为，CSS是实现UI层面地内容，JS是实现UE层面的内容，那么也就不难理解，这三者的诞生顺序了。当然是先要有基础的HTML，先要能够展示内容，无论美丑，之后是一个视觉上UI层面的提升，最后才是UE层面的完善（JS语言在1996年发明），有兴趣的同学，可以自行看一下《javascript高级程序设计》，这本书的前几章，就是在介绍网页技术的历史，还是蛮有趣的。

回来说，网页，遍历，渲染，浏览器的工作，最后呈现出来页面的内容。


现在，我们想想，我们已经完成了这么多的工作了。

