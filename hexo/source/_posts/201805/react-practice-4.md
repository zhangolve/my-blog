title:  React开发实践--4嵌套路由的应用
date: 2018-05-29  18:24:49 
categories: 前端
tags: [前端] 
description: 


---


![](http://7ktu2f.com1.z0.glb.clouddn.com/react.png)

---


嵌套路由的应用

我们知道React-router v4中，可以实现嵌套路由。有了这样一个机制，我们不必将所有的路由完全放到一个统一的位置进行管理，而可以根据情况去对路由进行拆分。坦白讲，我一直认为在一个地方统一管理，要比四散开来维护起来更加简单（可能有点像中央集权和诸侯国各自为政的感觉）。但是最近有个实际应用，让我发现，嵌套路由的价值还是很大的。只是以前我们一直没有合理使用。

# 先说一下实际使用场景。

我做的电商应用中，有一个叫做“爱逛店”的功能。（由于该应用主打线上线下融合，线下发展其实更好），每次从首页点击“爱逛店”图标进入“爱逛店”的门店展示列表，由于展示门店列表的过程是：

获取当前用户地理位置坐标=》后端根据地理位置远近排序=》将排好序的门店列表给到前端=》前端展示

造成展示门店列表的过程其实是相对比较慢的。为了能够有一个尽量好的体验，我们在展示门店列表前，会有一个loading的动画效果。而由于采用路由统一管理的机制，原来的门店列表的组件和门店详情的组件之间是并列关系，导致每次从某一个门店详情页面返回到门店列表页面，都会造成门店详情页面组件生命周期结束，门店列表页面进入下一个生命周期。进入下一个生命周期意味着什么呢？意味着它又需要重新走一遍上面的流程，尽管有了这个loading的动画效果，但是体验上还是会差很多。而且，更影响用户体验的是：这个loading效果本来是好意，能够让用户在等待期间看到些东西，但是由于浏览器的机制，这个时候，浏览器判定你初始页面高度只有100%（屏幕高度）这么高，则一旦门店列表列出来之后，浏览器不会再将页面滚动到上一次这个页面滚动到的位置了。这意味着，你从门店详情页面返回到门店列表页面，每次先看到loading效果，然后每次看到的都是最顶上的三五个门店，而不是你上次浏览到的门店，这体验，当然就更差了。

有什么解决办法吗？当然了。使用嵌套路由，上面的问题就都不是问题了啊。

首先明确我们的需求，由于我们的用户看到的门店列表是基于地理位置的，他的大致地理位置短时间内是不会改变的。（我指的是用户点进门店详情页面时在北京，点返回后就来到了上海），门店的数量短时间内也是几乎不会改变的。（我指的是用户点进门店详情页面时有100家门店，点返回后就有105家）。正是基于这样的一个判断，我们或者可以将这些门店的数据暂时存储起来。每次用的时候，直接取出来用就好了。那么这个时候问题来了，我们应该将这些门店的数据存储在哪里呢？浏览器的本地存储（localStorage，sessionStorage）? 又或者是代码里？

# 解决办法

不绕圈子了。我的办法是不如增加一个"爱逛店"管理组件。采用嵌套路由的方式来实现，门店数据的存储。先在主路由配置处（我的项目是app.js）写上：

            <RouteWithLayout path="/stores" hideFooter={false} loader={() => import('./Store/Store')} />

然后先看下面这段代码：

            <Store>
                    <Switch>
                        <RouteWithLayout exact path={`${this.props.match.url}`} hideFooter={false} loader={() => import('./StoreList')} stores={this.state.data} withLayout={false} />
                        <RouteWithLayout exact path={`${this.props.match.url}/:storeId`} hideFooter={false} loader={() => import('./StoreDetail')}  withLayout={false} />
                    </Switch>
            </Store>

从上面代码我们可以看出来，无论用户想要浏览某一个门店（StoreDetail），还是说想要浏览门店列表（StoreList），都需要先进入Store这个管理组件。我可以用这个管理组件来做什么呢？很简单，以前没有这个管理组件的时候，从`/stores`这个路由切换到`/stores:storeId`这个路由，第一个组件生命周期结束，第二个组件生命周期开始。而由于我把获取门店列表的方法写在了`StoreList`这个组件里，因此每次从门店详情页点返回都会重新去找门店列表。现在，我要做的是，把获取门店列表的方法提到上一层，提到Store这个组件当中。

这个时候，我们再来看看。如果`/stores`这个路由切换到`/stores:storeId`这个路由

组件 | 生命周期
---- | ---
Store | didupdate
StoreList |  unmount
StoreDetail |  didmount

而如果`/stores:storeId`这个路由切换到`/stores`这个路由呢？

组件 | 生命周期
---- | ---
Store | didupdate
StoreList |  didmount
StoreDetail |  unmount

没错，无论哪种场景，`Store`这个组件都只会update，而不会进入下一个生命周期。因为在一开始我就配置好了。


            <RouteWithLayout path="/stores" hideFooter={false} loader={() => import('./Store/Store')} />

因为在`/stores`这个路由的模糊匹配下，我任意切换路由，都只会让Store这个组件更新，不会触发didmount，那么我干脆把获取门店列表的方法写到他的componentDidMount()之中不就好了么，然后门店列表作为一个state值存储在这个组件的状态里，之后每次切换路由都能够立刻获取门店列表，无需loading，浏览器也能够记住上次这个页面滚动到的位置，返回后，还是原来的位置。

那位又说了，可是我要是直接在浏览器上输入某个门店的url，直接访问某个门店。你是不是还要把这个门店列表也给我获取到呢？那是不是得不偿失，更加影响用户体验呢？说的很对，所以我的策略是，在获取门店列表的方法中进行判断，只有`exact match path="/stores"`这个路由的时候，我才去从服务端获取门店列表。那位又说了，那你这时候如果，如果点击页面上的返回导航，你回到门店列表页，由于在`Store`组件`didmount`阶段你没有获取门店列表，这个时候肯定会出错啊。是的，那我就不返回门店列表呗。反正用户你也不是从门店列表进入的我某个门店页面的，我直接让你回我的APP 首页就好了嘛！


除了用户体验的提升外，另外的好处是：随着你项目的扩大，这个对路由的分拆也能够便于管理。毕竟如果你的主路由配置里有一两百行路由配置，看起来也会很不舒服，类似的哲学是从中央不直接管辖所有的地级市（中国有338个地级市）而将这些市根据地理位置，由省来管理。中央只管理省一级。


# 总结

前面说的很具体，具体的东西好处是便于理解。坏处可能就是，不能做到举一反三。所以我这还是来总结一下。


**如果你有一个应用场景：数据不会频繁更新，数据的请求过程影响用户体验，你的用户需要频繁地从子路由到孙子路由或孙子路由到子路由之间来还切换。那么可以考虑在子路由组件中，进行嵌套路由的配置，将请求数据的方法写在子路由组件当中，这样一来，用户体验会有一个很好的提高。**