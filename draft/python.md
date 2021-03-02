# python 打包概念

https://cloud.tencent.com/developer/article/1566619

wheel文件
wheel是一种制作分发格式，由PEP427定义。wheel志在取代egg格式。pip支持wheel.  
 关于wheel和egg的区别，参见这篇文章 
 安装wheel文件：

pip install /path/to/xxx.whl 
打包成wheel文件：

python setup.py bdist_wheel
wheel的优点：

更快速地安装纯Python包和native C extension包。
在安装时避免武断的代码执行（避免setup.py）
C extension的安装并不要求在Windows和MacOS平台上有编译器。
为测试和持续集成（CI）提供了更好的缓存。
创建.pyc文件作为安装的一部分，以保证它们符合Python解释器的使用。
更好的跨平台。

