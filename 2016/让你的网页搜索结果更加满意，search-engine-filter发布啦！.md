# 功能

- 默认过滤搜索页上来自 www.jb51.net 的结果
- 可以通过往输入框中添加过滤网站，形式如 www.jb51.net ,www.abc.com 等，无须使用http:// 作为开头。也可以过滤掉特定的内容来源，比如百度文库(wenku.baidu.com )



# 安装

安装方法
这是油猴脚本，所以请首先安装 tempermonkey

Firefox 用户请戳 https://addons.mozilla.org/en-US/firefox/addon/tampermonkey/
chrome 用户请戳 https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo?hl=en

然后安装： https://greasyfork.org/zh-CN/scripts/25788-search-engine-filter

# 使用方法

安装好后，在打开百度搜索或谷歌搜索，进入搜索页面后会自行根据过滤规则进行过滤，默认的过滤规则是过滤掉来自www.jb51.net ，也就是垃圾脚本之家的内容。用户可以通过在输入框中输入自定义的过滤规则，将自己讨厌的不想看到的搜索内容过滤掉。

具体的使用方法，请看GIF。图示为百度搜索时的使用方法，谷歌搜索类似。

![](http://upload-images.jianshu.io/upload_images/48180-dd46d2eddfae040e.gif?imageMogr2/auto-orient/strip)

# Github

https://github.com/zhangolve/search-engine-filter  

喜欢的可以给个star

# 其他



# 题外话


## 为什么会开发这个脚本（扩展）

之所以会写这个脚本，最早来源于我讨厌在百度搜索页面出现的脚本之家的内容，该网站排版差，内容质量差，却依靠着SEO 和不为人知的套路，总是能够占据技术类搜索词汇首页的位置，每次通过百度点开这个网站都让我后悔不已，浪费了我的时间。这个时候，你可能就会问了，你为啥不用谷歌呢，我想说在大多数的技术问题搜索上，谷歌当然是很牛的，但是有些情况下，百度也有他的优势。因此，我就动了想要写一个在百度搜索页面过滤来自脚本之家网站内容脚本的念头。后来，做了这个简单的功能之后，给它起了一个简单粗暴的名字,fuckjb51 。

之后，又陆续给这个脚本添加了几个小功能，比如能够添加自定义的过滤url，搜索引擎也不再只限制在百度这一个上了，而是拓展到了包括谷歌原站，谷歌日本，谷歌香港等站点，原来的项目名，fuckjb51也就不再适合了，因此改成了现在的名字search-engine-filter（搜索引擎页面内容过滤）

后来，我又想到其实可以做一个 Chrome 扩展，毕竟在百度搜索页展示一个多余的输入框和醒目的按钮并不是很好的设计。而 Chrome 扩展也能方便使用Chrome 的人群。在v1.0.1版本中，仍然采用在搜索结果页面中添加输入框和提交按钮的方式来交互，后期可能会对这一交互方式进行更改。
