
title: pnpm初体验
date: 2022-09-04 06:41:16
categories: 杂谈
description: pnpm初体验
 
--- 



# pnpm

想利用它的一些优势

- 快速 pnpm i --prefer-offline
- workspace 
- publishConfig

整体体验很不错。


之前遇到的问题，我们有一个私有的npm包，这个包里面目前看来，有两块大的内容。

经过我的改造之后，将原来的一个包，改成了多个包，那么他的优势在哪里呢？

# monorepo

monoRepo 这个概念近几年还蛮流行的，几个包，甚至是几个项目，在同一个repo里面管理，共享同一份代码，彼此之间有一定的联系，但是这些项目间又彼此独立。

说起来，我在刚刚来到这个公司大概半年多之后，就有过想要把两个项目放在同一个repo里这样的想法，只是当时没有想到这样的学术名词，也没有一些好的技术方案。

借助pnpm，其实是可以梳理成章地完成这些的。

我们之前要用刚刚说到那两块内容，比如A和B，我们的做法是在webpack里面写Alias，以及在tsconfig里面去做alias，将这两个用alias的方式去作为两个独立的内容去看待。这样做有什么问题呢？当然是有问题的，也就是说业务的项目已经对第三方的包有了感知，这种感知并不是优雅的。这也是我比较不太能够接受的。

而经过我改造之后，虽然我分拆成了多个包，但是我最后还是将这些分拆的包，放在了一个影子包里面。

monorepo借由pnpm的workspace方便地实现，同时也方便我们去进行开发和调试。包与包之间的相互引用，非常方便，我们可以指定直接使用当前workspace下的本地包，这样也方便我们进行开发。

# 分拆包之后，更多的新包出现

原本在一个包里面只有两个包，A和B，但是经过对项目的分析，我又添加了几个新包。每个包，都因为这种monorepo的概念，而显得非常合适。比如新添加的C包，就是一个导出umd，去做微前端项目间进行通讯的包。再来说，新添加的D包，就是一个脚本包，这个脚本包，就能够把几个项目里都用到的脚本整合在这里，避免代码的重复，利于维护。当然，刚才也说了，由于加了这么几个新包，我们也不可能每次加新包，都要去改webpack，tsconfig，这样又再次说明了之前不是一个优雅的解决方案。

# 速度

之前遇到的问题，大概有两点，一个是生成新包的过程略慢，当时测算了一下，每次新包build的过程，大概是6分钟。而通过pnpm去生成新包，这种缓存机制还是很明显的让速度加快的，现在大概一分多钟，就能够将包生成，当然前提是没有deps的更新等其他情况。

另一个问题，当新包生成之后，想要安装这个新包。在 npm i的时候，发现这个过程也是比较慢，经常卡顿的，通过调整代码代码结构，改成monorepo这样，也能够一定程度加速这个过程，当然，需要说明的是，对这个过程改进更明显的，应该是使用 --prefer-offline，这个即便是原生npm也是支持这一参数的。


