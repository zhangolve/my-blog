title: 一个YouTube视频搬运工的教训
date: 2019-01-13 13:07:07
categories: 简述

--- 


# 起因

我在11月底的时候，在知乎上看过一个帖子，讲的是某人通过搬运Ｂ站上面的视频，获取了很大的经济收益。我当然是很羡慕的，后来简单研究了一下，发现YouTube 有API供开发者调用，这意味着上传的工作完全可以由计算机来完成。我很快想到，既然别人能够搬运Ｂ站上面的视频，可能这些人，还没有技术，只是靠手动搬运。那么我是不是可以通过代码来实现，视频的全自动搬运呢？

我觉得这是个不错的点子，后来又经过研究，**得知YouTube上的视频，大概每千次观看量，视频的所有者可以得到大概5元人民币的收益(已经过换算)**。而内容的影响力又是绵延不绝的，只要是好的内容，接下来就是躺着挣钱了。我当然是看好YouTube和他的收益情况的，毕竟我要做的，也不是自己制作视频，而是靠搬运。但紧接着，我又发现，谷歌对于YouTube频道的收益有一个门槛，只有达到了**在过去的一年里，有1000个订阅者，4000个小时的累计播放量**，才能够申请通过广告分成的方式获取收益。经过简单的计算，我发现，实际上，只需要每天10个小时的播放量，就可以达到4000小时累计播放量这个门槛，而只要有几个爆款视频，订阅者也会越来越多，这个门槛并没有多难以跨过。

#　说干就干

接下来就是写代码了。甚至不想看代码思路的直接跳过此部分。

说一下，我搬运视频的代码思路。这种做法，毕竟是侵权的。

首先，通过node爬虫，模拟浏览器的访问，获取到Ｂ站某个up主的所有视频，接下来通过node的child_process来执行[you-get](https://github.com/soimort/you-get) 的命令行命令，使得这个up主的视频能够批量地被下载下来。当然，我并不想竭泽而渔，也觉得老视频没有多少意义，所以每个up主，我最多只爬去最新的100个视频。

接下来，我会将视频通过YouTube接口的方式，批量地上传到指定的频道上面去。

后来，随着我的开发，细节也越来越完善。

- 支持持续订阅某个up主，思路也无非是隔一段时间，爬去最近这段时间内他的上传的视频。

- 支持将同一个up主的视频放到同一个播放列表里，之所以这样做，一则是因为视频更方便管理和浏览。二则是害怕某天突然被告知，我偷了他的视频，这样删除的时候，也只需要找这个播放列表里的视频删除可以了。

- 原有的视频下载和上传的脚本是隔离的，导致做不到自动化。后来，这个工作实现了自动化。只需要在一开始将某个up主进行订阅，之后，下载，上传，长期订阅和上传这个up主的视频都能够自动完成。

坦白讲，写这个代码写得还挺开心，很大一部分因为是以前很少用到js里异步控制的`async await`,但是这次代码写起来，用了很多，也用得很爽吧。另外以前也很少写node的后台服务，最多也就是写两个爬虫，这次却借助这个想法，顺便学了一波node服务的部署和运维(为了做这件事情，也为了科学上网，我当时还买了一台阿里云vps，后来因为科学上网，服务挂了。我又换到了搬瓦工，这才一切稳定)。当然，有人可能会觉得我这种行为侵权，这个话题，我一会儿再聊。

# 过程

我便改进代码，边上传YouTube视频。由于最近六学火热，我最初选取的是Ｂ站上某个知名六学家作为我的实验样本。后来，又在Ｂ站上找到了几个体育类，搞笑类，影视类的up主，来上传他们的视频。我也在这个过程中慢慢发现，YouTube每个频道每天只允许上传最多100个视频。所以我这种bot也不可能像个疯狗一样毫无节制地去上传视频。这也意味着，我要选取尽量符合观众期望的视频来上传。因而，有很多天，我经常会打开YouTube的后台，去看最新的浏览量分析，来看哪些视频更受欢迎。去看最新的搜索词排行，来看到底用户喜欢看哪些视频，以决定我接下来要选取哪个up主作为我下一个订阅者。

我的确从YouTube的后台看到，随着我的视频越来越多，代码功能越来越完备，各项数据也越来越好了。虽然一开始没有爆款的视频，但是凭借着人海战术，还是很快就达到了每天10小时的播放量，接下来，就只差多几个爆款，来增长一波粉丝了。

但是，但是，但是

# 版权是个大问题

搬运视频，不可避免地会碰触到版权这件事。我最初对这件事，做个些简单的调查。当时考虑电视剧电影一定会是版权的高压线，而且在YouTube上搬运这类视频的人也不在少数，我并不想去趟这类混水。所以，我也是将搬运的内容，选择为了短视频，因为的确看到YouTube上面有大量来自国内视频网站的短视频，想到既然别人可以，我为什么不可以呢，于是也就选择了这个领域。

但是，从搬运的前几天起，邮箱里就开始接收来自官方的版权警告。比如下面两个截图，就是我随意从邮箱里YouTube发来的邮件里截取到的。

![版权警告](https://upload-images.jianshu.io/upload_images/48180-a0c1f79b0185840f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![版权警告](https://upload-images.jianshu.io/upload_images/48180-f200760543186769.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

看过越来越多这种版权警告，发现YouTube很智能。这种版权警告，应该完全都是由机器来判断和筛选，因为有些刚刚上传的视频甚至都没有播放量。不过我并没有对这种版权警告有所警惕，只是觉得，既然YouTube很智能，能够帮我查找到哪些视频是侵权的，哪些不是，那我只需要把一些漏网之鱼搬运上去，也就很好了。

但是随着我的频道观看量和订阅量越来越多，也收到了下面这种邮件。
![版权警告](https://upload-images.jianshu.io/upload_images/48180-12b471c560f539c0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![版权警告](https://upload-images.jianshu.io/upload_images/48180-0f372132065a7ae0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

这个视频，其实是这个视频频道刚刚创建之初上传的，YouTube大概反应了一段时间，才把这个视频封锁了，而且还给了我严厉的警告。这是第二次**copyright strike**，当第三次收到这种邮件之后，我那个视频频道就被封锁了，而且很快，我谷歌帐号关联的另外一个我平时看视频的频道，也被封锁了。

我发了两封邮件过去，想要解释我的动机。我解释了我是个程序员，只是为了学习知识，不过，谷歌没有饶过我，截至到现在(2019年１月13日)，我的YouTube帐号仍然处于封锁状态。

![申诉无效](https://upload-images.jianshu.io/upload_images/48180-7bdff2b8ef4f70bb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

# 我侵犯的谁的版权

接下来解释一下这个问题， 我侵犯的谁的版权？

很多读者，可能从一开始就对我这种行为表示不屑，毕竟这涉及到侵犯版权。但我还是要辩解两句，首先，从上面我的侵权截图也可以看出来，我搬运的视频几乎都是影视片段和搞笑类的小视频，之所以侵权，侵的也是那些影视片段原作者的权益。再说明白点，虽然我是从Ｂ站搬运的视频，但YouTube并不认为我对他们有侵权行为，甚至，即便是那些Ｂ站up主把那些他们剪好的小视频发布到YouTube上，他们也依然会侵权。就像是前两年很火的谷阿莫那样，他的确付出了很多时间精力，但实际上他用到的素材也是涉及侵权的，在YouTube一样行不通。当然我也不否认，我的侵权行为，**毕竟你从贼的手里偷到了路人的钱包，难道你就是清白的吗？**

我还记得我那个频道刚刚建立十几天的时候，因为搬运了某个在Ｂ站上有１万+粉丝数量的up主的小视频，因为我的播放列表名字就是这个up主的名字，因而在YouTube上搜索很容易找到。那个up主在我搬运他的最新的一个视频下面留言，说他就是Ｂ站上的谁谁谁。也只是说了这么一句，我也并没有回复他,我又能说什么呢？


# 教训

关于盗版这件事情，我自己的态度一直模凌两可。我不认为这件事完全没有正面价值，不然，我也不会去做这样的事情。在写此文的时候，我甚至会想到13年去世的[亚伦·斯沃茨](https://zh.wikipedia.org/wiki/%E4%BA%9A%E4%BC%A6%C2%B7%E6%96%AF%E6%B2%83%E8%8C%A8) ,他是个反对[禁止网络盗版法案](https://zh.wikipedia.org/wiki/%E7%A6%81%E6%AD%A2%E7%BD%91%E7%BB%9C%E7%9B%97%E7%89%88%E6%B3%95%E6%A1%88 "禁止网络盗版法案")的运动的人，很大程度上，我是欣赏这种黑客精神的。所以，我对版权上的问题，其实是没有多少反思的。因为如果真要较真的话，我搬运的那些Ｂ站视频up主们也毫无例外都有问题。

当然我也要说，是谷歌为了版权方的利益，对YouTube进行了控制，让这个社区更能够良性发展，他也并没有错。只是，在谷歌YouTube这张大的鱼网之下，有的成为了漏网之鱼，因此你还是能够在YouTube看到大量的国内视频网站上的盗版视频。有的成为了网中之鱼，成为了牺牲品。这其中包括了我自己，也包括那个曾经依靠视频广告分成获利颇丰的“B站授权搬运工”。我也许可以做的更好，比如只搬运搞笑类的视频，不搬运视频剪辑类的视频，这都可以让我的视频频道活得更久一些。但是，我并不想那么做了，它终究有一种做贼的感觉。






