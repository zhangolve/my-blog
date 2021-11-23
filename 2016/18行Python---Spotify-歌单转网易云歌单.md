# 动机

最近一直在用Spotify在线听歌，Spotify的好处在于能够发现更多好听的歌曲。然而，它的订阅实在是太贵了，因此也就不能够离线下载，而虽然我在用Spotify，但是也没有抛弃网易云音乐，用它来下载歌曲也很不错，网易云音乐的评论区也往往欢乐多多，因此，我就有了这个想法，想要将Spotify的歌单转到网易云音乐歌单。

# 思路

上网google了一番之后，发现确实有很多的中文用户乃至于外国用户在纠结着怎样导出Spotify的歌单甚至是下载整个歌单的歌曲。我首先找到了[Exportify](https://rawgit.com/watsonbox/exportify/master/exportify.html) 这个网站，它是能够通过接入Spotify的API来将Spotify的歌单找到并支持导出为CSV格式的文件。

而我们知道，网易云音乐也是支持导入歌单的，但仅限于酷狗或酷我的歌单，而酷狗的歌单文件是.kgl格式的，因此如果要想将Spotify歌单转到网易云音乐歌单，我们就首先需要将这种CSV格式的文件转成kgl格式的文件。

本来我是想着用JS的，因为最近一段时间都在用JS，但是从操作文件的角度上讲，我觉得Python还是更有优势的。虽然Python已经很久没用了，但是还是想尝试一下。

# 过程

## 1.导出Spotify歌单
使用刚才提到的[Exportify](https://rawgit.com/watsonbox/exportify/master/exportify.html)  导出歌单，在此过程中，需要Spotify的授权。

![](http://7ktu2f.com1.z0.glb.clouddn.com/exportify.jpg)

授权之后经过分析会出现类似上面的界面，这个时候你只需要挑选你想要导出的歌单并导出之即可。

## 2.CSV转JSON

用记事本打开CSV文件(你也可以打开试试)，发现使用Python对它直接处理并不是很方便。因此，想到首先对之转化为JSON格式文件。

用记事本(或其他文本编辑器均可)打开CSV文件，然后全选其中的内容,把内容复制到[csv2json](http://www.csvjson.com/csv2json)进行转换：

![](http://7ktu2f.com1.z0.glb.clouddn.com/csv2json.jpg)

转换完成之后如上图所示，这个时候我们看到已经出现了JSON。

## 3.Python文件操作

### 3.1 分析KGL 文件

为了分析KGL文件，我从网络上下载了一个酷狗歌单，它的基本结构是：

<?xml version="1.0" encoding="windows-1252"?>
<List ListName="默认列表">
<File>
		<MediaFileType>0</MediaFileType>
		<FileName>邓紫棋 - 泡沫.mp3</FileName>
		<FilePath>.</FilePath>
		<FileSize>4186975</FileSize>
		<Duration>258000</Duration>
		<Hash>36542b20231db1633eea72f7d6b27492</Hash>
		<Lyric>F:\KuGou\Lyric\邓紫棋 - 泡沫-36542b20231db1633eea72f7d6b27492.krc</Lyric>
		<Bitrate>128000</Bitrate>
		<MandatoryBitrate>0</MandatoryBitrate>
	</File>
	<File>
		<MediaFileType>0</MediaFileType>
		<FileName>灌篮高手 - 好想大声说我爱你.mp3</FileName>
		<FilePath>.</FilePath>
		<FileSize>1618124</FileSize>
		<Duration>231000</Duration>
		<Hash>34e31be84ce3d7c0cfad66e28c0b8220</Hash>
		<Lyric>F:\KuGou\Lyric\灌篮高手 - 好想大声说我爱你-34e31be84ce3d7c0cfad66e28c0b8220.krc</Lyric>
		<Bitrate>56000</Bitrate>
		<MandatoryBitrate>128000</MandatoryBitrate>
	</File>
	<File>
		<MediaFileType>0</MediaFileType>
		<FileName>筷子兄弟 - 小苹果.mp3</FileName>
		<FilePath>.</FilePath>
		<FileSize>3382542</FileSize>
		<Duration>211000</Duration>
		<Hash>fcd49446e26461d95433e9eea5c7a790</Hash>
		<Lyric>F:\KuGou\Lyric\筷子兄弟 - 小苹果-fcd49446e26461d95433e9eea5c7a790.krc</Lyric>
		<Bitrate>128000</Bitrate>
		<MandatoryBitrate>128000</MandatoryBitrate>
	</File>
</List>

经过反复地修改并导入到网易云音乐中进行测试最终发现，一个简化的KGL文件需要是类似这样的：
<?xml version="1.0" encoding="windows-1252"?>
<List ListName="默认列表">
<FileName>邓紫棋 - 泡沫.mp3</FileName>
<FileName>筷子兄弟 - 小苹果.mp3</FileName>

甚至结尾的</List>也可以去掉


