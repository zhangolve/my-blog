转载自： http://www.blogbus.com/pptaddins-logs/33661236.html
主要有下面几种方式：

（1）用压缩类的工具，把PPT文档打包成一个可执行自解压的Exe文件。

（2）把PPT文档作为资源，在程序设计语言中一同编译进Exe文件中。

（3）先把PPT文档用某个密钥进行二进制流式加密，再把它作为资源封装到Exe文件中。

（4）用专门的封装工具把PPT文档封装到Exe文件中。
exe资源提取器，或者7z。前者能提取各种资源，但是工具不好找，而且大多不是免费的。后者应用有限，只局限于打包式的exe。
exescope  MultiExtractor  都无效。

visiul basic  可以实现mp3到exe的封装。
http://www.cnblogs.com/michaelhuwei/archive/2009/12/25/1632129.html
需要编写一个exe文件，而其中嵌入了一段我设计好的音乐，打开exe后音乐自动播放。最重要的是除了 exe 文件外不能有额外的附加文件，将这个exe拷到其他（安装有framework的）电脑上，需要能正常运行。 

1.资源嵌入

   这个比较简单，vs2008 提供了非常方便的方法，新增一个项目后，打开 Properties 文件夹下的 Resources.resx 文件， 然后点击 添加资源--》添加现有文件，选择你要加入的 mp3， 就可以了， vs2008 会自动在 Resources 类中增加一个以 mp3 文件名命名的属性，例如我添加的“美梦成真.mp3”, 则自动生成的属性如下：

internal static byte[] 美梦成真 { 
    get { 
        object obj = ResourceManager.GetObject("美梦成真", resourceCulture); 
        return ((byte[])(obj)); 
    } 
}

该属性可以用 Properties.Resources.美梦成真  来访问， 非常方便。

2. 播放 mp3

   通常使用 media player 控件来播放，但如果添加了 media player 控件的话会增加一个 wmp.dll 文件， 不符合要求， 所以这里使用一个 API 函数来播放.

[DllImport("winmm.dll")] 
static extern Int32 mciSendString(String command, 
  StringBuilder buffer, Int32 bufferSize, IntPtr hwndCallback);

该函数的具体用法可以查看 msdn , 写的非常详尽， 我们这里只需要封装3个命令就可以了， open \play \ close.

///打开媒体文件

void OpenMedia(string path) 
{ 
    mciSendString("open " + path + " alias media", null, 0, Handle);  // 使用open 命令打开文件 
    mciSendString("play media", null, 0, Handle); //使用 player 命令播放 
}

///关闭所有打开的媒体文件

void CloseMedia() 
{ 
    mciSendString("close all", null, 0, Handle);  //使用 close 命令关闭 
}

3. 释放嵌入的 mp3 资源以供播放

   由于嵌入的资源是以 byte[] 的形式访问的， 所有需要先将它存为一个实体文件，然后才能播放

private string GetResMp3() 
{ 
    string path = Path.Combine(Application.StartupPath, "美梦成真.mp3"); 
    FileStream fs = new FileStream(path, FileMode.Create); 
    fs.Write(Properties.Resources.美梦成真, 0, Properties.Resources.美梦成真.Length);  //将 byte[] 内的内容全部写入到文件即可。 
    fs.Close(); 
    return path; 
}

有了以上三步， 播放内嵌的 mp3 就很容易了， 以下为完整的代码

public partial class Form1 : Form 
{ 
    [DllImport("winmm.dll")] 
    static extern Int32 mciSendString(String command, 
      StringBuilder buffer, Int32 bufferSize, IntPtr hwndCallback);

    public Form1() 
    { 
        InitializeComponent(); 
    }

    private void Form1_Load(object sender, EventArgs e) 
    { 
        string path = GetResMp3(); 
        OpenMedia(path); 
    }

    private string GetResMp3() 
    { 
        string path = Path.Combine(Application.StartupPath, "美梦成真.mp3"); 
        FileStream fs = new FileStream(path, FileMode.Create); 
        fs.Write(Properties.Resources.美梦成真, 0, Properties.Resources.美梦成真.Length); 
        fs.Close(); 
        return path; 
    }

    void OpenMedia(string path) 
    { 
        mciSendString("open " + path + " alias media", null, 0, Handle); 
        mciSendString("play media", null, 0, Handle); 
    }

    void CloseMedia() 
    { 
        mciSendString("close all", null, 0, Handle); 
    }

    private void Form1_FormClosed(object sender, FormClosedEventArgs e) 
    { 
        CloseMedia(); 
    } 
}

