ppt第1页


13
00:00:28,366 --> 00:00:31,266
大家好
很高兴，今天第一个来进行这个hackathon
我就抛砖引玉
介绍下我对当前咱们微前端的两点思考吧
今天呢我的这个主题叫God and Father
And 前后的两个词
分别对应着我的每个想法
我想挨个说一下吧


ppt 第二页

首先说第一个
先说一下上下文
就是我们其实是通过 webpack 这样一个工具
对微前端项目进行打包
也是用这个工具来
帮助我们进行本地开发
我们使用webpack的时候
也进行了大量的自定义配置
如图中所列
我找到了这样几个微前端项目
可以看到他们都有一个scripts目录

这个 scripts 目录
就放着这样的一些工具
是我们对webpack的自定义配置
你也能够发现
他们其实就是用 ctrl c ctrl 为复制粘贴的方式去做的
其实他们这些项目一开始这个目录
里面的东西差不多是相同的
但是后来呢，由于每个项目
还有他们各自的特殊性
所以各个项目在维护的时候呢
就又增加了一些个性的配置


ppt第三页

51
00:02:10,766 --> 00:02:12,200
我在这里也列了一张图

52
00:02:12,233 --> 00:02:14,400
其实是问题就是说的

53
00:02:15,033 --> 00:02:16,266
就类似于这种人

54
00:02:16,266 --> 00:02:18,200
类迁徙的这样一件事情当你

55
00:02:18,700 --> 00:02:21,000
把你时时间越来越长

56
00:02:22,000 --> 00:02:23,733
大家可能一开始都是来自非洲

57
00:02:23,733 --> 00:02:25,100
可能时间越来越长

58
00:02:25,466 --> 00:02:27,100
有有有人去了欧洲

59
00:02:27,100 --> 00:02:29,133
有人去了亚洲有人去了北美洲

60
00:02:29,133 --> 00:02:31,300
然后后来变成了黄种人黑

61
00:02:31,766 --> 00:02:34,600
有色人种什么黑

62
00:02:34,966 --> 00:02:37,300
那个棕色人种白种人

63
00:02:37,566 --> 00:02:40,100
然后最后大家语言也不一样啊

64
00:02:40,100 --> 00:02:41,466
文化也不一样然后

65
00:02:42,366 --> 00:02:44,266
想要和平就就很困难吗

66
00:02:44,266 --> 00:02:46,533


67
00:02:47,300 --> 00:02:49,100
嗯所以我没看

68
00:02:49,166 --> 00:02:49,800
其实我

69
00:02:49,800 --> 00:02:51,500
我刚才就通过这样一个例子

70
00:02:51,500 --> 00:02:52,433
想表明什么呢

71
00:02:52,433 --> 00:02:54,533
就是这种复制粘贴的方式其实

72
00:02:55,400 --> 00:02:56,833
会带来很多问题

73
00:02:56,833 --> 00:02:58,866
对吧这些问题其实是我们开发

74
00:02:59,433 --> 00:03:01,200
都能感知到的一些问题

75
00:03:01,566 --> 00:03:03,933
所以我在这也不详细说了

77
00:03:05,933 --> 00:03:08,100
我认为复制粘贴肯定是不好的

回到第二页

79
00:03:09,866 --> 00:03:10,700
这本来也不算是啥问题
但是呢，
最近这一个时期

93
00:03:42,033 --> 00:03:43,833
我们紧接着要对 webpack进行升级
我们要把他升级到webpack5

94
00:03:44,533 --> 00:03:47,966
升级之后，会有一些好处，这个不是我今天要谈的话题
我想谈的是，伴随着这种breaking change
就会出来一些问题

96
00:03:50,100 --> 00:03:53,500
应该是已经有team在做这件事情


105
00:04:17,366 --> 00:04:18,166
所以

106
00:04:19,200 --> 00:04:20,033
这个时候就

107
00:04:20,300 --> 00:04:21,800
就又面临着这样一个问题

108
00:04:21,800 --> 00:04:24,866
就是升级 webpack 5可能就比较困难


114
00:04:35,900 --> 00:04:38,033
但是困难之处在哪呢就是

115
00:04:41,033 --> 00:04:43,300
你需要去找出来
每个项目的交集
还有他们的特性
如果有一个所谓的最佳实践的话
那么我们需要把前面我的集合交集这部分替换成最佳实践中的写法
怎么做的呢，还是复制粘贴
又要做一遍复制粘贴的工作
之后，我们每个项目比较个性的那部分
也需要针对webpack5进行适配


第四页

167
00:07:12,766 --> 00:07:14,633
所以我想到了这样一句话

168
00:07:14,766 --> 00:07:16,633
西方有这样一个谚语

169
00:07:17,533 --> 00:07:18,333
嗯

170
00:07:18,900 --> 00:07:21,733
用中文来说其实应该很多人都听过

171
00:07:21,733 --> 00:07:23,600
叫做上帝的归上帝

172
00:07:23,600 --> 00:07:24,766
凯撒的归子凯撒
他其实就是说各司其职

173
00:07:24,766 --> 00:07:25,866


174
00:07:27,766 --> 00:07:29,266

对应着我们开发也是一样

175
00:07:29,400 --> 00:07:31,066
既然各个项目之间有

176
00:07:31,300 --> 00:07:32,733
有很多公用的东西

177
00:07:32,733 --> 00:07:34,000
有很多相同的东西

178
00:07:34,000 --> 00:07:34,833
那为什么

179
00:07:35,266 --> 00:07:36,000
我就

180
00:07:36,000 --> 00:07:38,700
我为什么不把它抽出来

181
00:07:39,000 --> 00:07:41,333
然后让他单独拿出来去去用呢


第五页


182
00:07:42,500 --> 00:07:43,300
所以

183
00:07:43,733 --> 00:07:45,933
换个角度来说谁是上帝呢

184
00:07:46,100 --> 00:07:49,766
就是谁是谁能够承担上帝让一个世界

185
00:07:50,066 --> 00:07:54,233
角色呢我认为 ktv fdp 他是他们人上帝

186
00:07:56,700 --> 00:07:58,533
ktv 做了很多的工作

187
00:08:00,200 --> 00:08:00,600
然后呢

188
00:08:00,600 --> 00:08:03,133
我们可能只需要在各自的微服务当中

189
00:08:03,533 --> 00:08:04,300
简单的配置

190
00:08:04,300 --> 00:08:07,133
然后就就我的微服务就能跑起来

191
00:08:07,266 --> 00:08:08,266
原因是什么呢

192
00:08:08,266 --> 00:08:09,366
原因是 kdp,fdp

193
00:08:11,000 --> 00:08:13,300
把大部分工作都揽过去了

194
00:08:13,733 --> 00:08:15,333
所以我在想其实

195
00:08:15,333 --> 00:08:18,833
可以有一个工具 webpack tools

196
00:08:19,400 --> 00:08:21,533
我暂时起这样一个名字

197
00:08:23,033 --> 00:08:25,600
他的作用其实就是把把我的 k

198
00:08:27,000 --> 00:08:28,200
和 ktk 蕾丝

199
00:08:28,466 --> 00:08:31,266
然后也能够把大部分这个所谓 ipad

200
00:08:31,766 --> 00:08:32,666
的配置东西

201
00:08:34,466 --> 00:08:35,666
放在他他

202
00:08:36,366 --> 00:08:37,300
放在他里面

203
00:08:37,300 --> 00:08:38,233
这样的话呢

204
00:08:38,700 --> 00:08:41,800
我各个项目只维持自己的一些属于各自项目的配置

205
00:08:43,066 --> 00:08:45,166
只需要进行简单的配置

208
00:08:49,166 --> 00:08:52,466
我就可以很方便快捷地
完成微前端项目的本地开发和打包这样的工作
以后再有一些升级呢，
对这个工具进行升级。
也能够很清楚对知道哪些是共性哪些是特性

209
00:08:53,866 --> 00:08:54,933
然后说干就干吧

210
00:08:54,933 --> 00:08:56,833
然后我就我就我就写了这样一个

211
00:08:57,466 --> 00:08:58,733
webpack tools这样一个工具

212
00:08:59,466 --> 00:09:00,733
写了这样一个私有库

213
00:09:00,733 --> 00:09:02,633
去实现这样一个效果

214
00:09:05,066 --> 00:09:06,600
然后最终的效果是什么呢

215
00:09:06,600 --> 00:09:07,533
其实就是我

216
00:09:07,700 --> 00:09:09,700
我也我刚才提到了我也是

217
00:09:09,766 --> 00:09:12,533
我是用一个 star 的是用一个 biu 的吗

218
00:09:13,100 --> 00:09:15,166
然后这样的话那我我我只需要

219
00:09:15,733 --> 00:09:17,066
只需要去

220
00:09:18,566 --> 00:09:20,400
简单的做一些改改动啊

221
00:09:20,400 --> 00:09:21,433
把我原来用

222
00:09:21,900 --> 00:09:24,266
in rose creeps 这个末路下面的

223
00:09:25,400 --> 00:09:26,200
配置的

224
00:09:26,833 --> 00:09:27,733
替换成我

225
00:09:28,566 --> 00:09:30,733
我我的这个 so eb tos tors

226
00:09:31,433 --> 00:09:33,000
这个工具里面的东西

227
00:09:35,100 --> 00:09:36,900
第二点呢我想说的是这个

228
00:09:38,333 --> 00:09:38,866
第二点呢

229
00:09:38,866 --> 00:09:41,733
也是想说这个为钱为钱端这样一个

230
00:09:42,500 --> 00:09:43,500
面临的问题吧

231
00:09:43,500 --> 00:09:44,333
就是其实

232
00:09:46,266 --> 00:09:47,066
微前端

233
00:09:47,866 --> 00:09:49,366
引入微前端之后呢

234
00:09:49,766 --> 00:09:50,566
有一个

235
00:09:51,633 --> 00:09:53,133
小细节吧就是在

236
00:09:55,066 --> 00:09:55,866
当你

237
00:09:56,766 --> 00:09:59,166
当你使用私有库的时候

238
00:10:01,300 --> 00:10:03,133
他的打包方式也比较有讲究

239
00:10:03,133 --> 00:10:05,033
当时就是比较好的方式

240
00:10:05,033 --> 00:10:07,166
其实比较推荐的方式其实是用

241
00:10:07,500 --> 00:10:10,833
es modules 这样一个打包方式

242
00:10:10,833 --> 00:10:11,666
这样的话呢


244
00:10:14,866 --> 00:10:17,866
他能够比较明显的去缩小打包

245
00:10:18,833 --> 00:10:22,233
未前端项目打包出来后的体积大小

246
00:10:22,933 --> 00:10:24,900
然后我在这里也列也列了一张图

247
00:10:24,900 --> 00:10:25,966
就是如果你用

248
00:10:26,733 --> 00:10:29,933
要传统的 commonjs的打包方式去打包的话

249
00:10:30,733 --> 00:10:31,533
去对这个

250
00:10:32,300 --> 00:10:35,166
私有库 us 组建库进行打包的话最后

251
00:10:38,233 --> 00:10:39,900
就是把整个的这样一个

252
00:10:40,966 --> 00:10:44,100
你的引入的东西都给打包进来了

253
00:10:54,066 --> 00:10:55,500
但是呢如果说你用

254
00:10:58,500 --> 00:11:00,466
但是呢如果说你用这个

255
00:11:00,900 --> 00:11:03,066
es module 这样方式呢你就可以

256
00:11:05,533 --> 00:11:06,733
改变这个一切

257
00:11:07,533 --> 00:11:09,833
然后呢我想我想说的第二个方案其

258
00:11:09,833 --> 00:11:11,600
实就是有一个东西叫father

259
00:11:12,533 --> 00:11:14,400
然后这个呢他也是在

260
00:11:15,100 --> 00:11:17,333
我可能不了解前端的同学可能不知道

261
00:11:17,333 --> 00:11:18,133
其实在

262
00:11:19,966 --> 00:11:21,666
我们现在用的 a n t d

263
00:11:21,666 --> 00:11:23,833
他的很多基础组件的打包都是用这个

264
00:11:24,133 --> 00:11:25,300
叫做father

265
00:11:25,766 --> 00:11:26,466
进行打包

266
00:11:26,466 --> 00:11:28,700
然后他想实现的他的他的效果

267
00:11:28,700 --> 00:11:29,500
其实就是

268
00:11:29,900 --> 00:11:31,866
就是能够很方便的去

269
00:11:33,666 --> 00:11:34,633
去进行打包

270
00:11:35,600 --> 00:11:37,066
然后最终实现效果

271
00:11:37,566 --> 00:11:39,700
嗯我们可以也可以看到

272
00:11:40,600 --> 00:11:42,100
刚才那个数字是600多

273
00:11:42,100 --> 00:11:44,300
现在只有变只变成了26

274
00:11:44,333 --> 00:11:46,066
所以效果还是比较明显的

275
00:11:46,500 --> 00:11:49,633
ok 先先接下来我来做一个demo


有一点忘记说了，关于我hackathon中提到的webpack tools，它配置项比较多,如果现在想在一个微前端项目中使用,还不能够做到开箱即用,遇到问题也可能调试起来比较麻烦.
我仍然是把它作为一个idea,就是一个hackathon的demo项目,分享出来.

关于第二个前端组件库打包工具
也有它的局限性
如果你要对你的前端组件库有一些个性化的处理
那这个工具也并不适用。
总体来说
还是具体问题
具体分析的
