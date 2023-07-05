

ffmpeg -re -i "1.mp4" -vcodec copy -acodec aac -b:a 192k \
-f flv
2022-01-16 11:14:48
ffmpeg -re -i "1.mp4" -vcodec copy -acodec aac  \
-f flv "rtmp://live-push.bilivideo.com/live-bvc/?streamname=live_545096419_4265304&key=a481670b44d83bba3498684ec7964cf7&schedule=rtmp&pflag=1"
2022-01-16 11:30:42
Bilibili推流总中断/ffmpeg
2022-01-16 12:55:37
#TODO ffmpeg 倍速视频生成
2022-02-26 08:04:17
https://blog.csdn.net/ternence_hsu/article/details/85865718
#ffmpeg 视频的倍速播放与慢速播放
2022-02-26 11:11:19
ffmpeg -i input.mkv -filter_complex "[0:v]setpts=0.5*PTS[v];[0:a]atempo=2.0[a]" -map "[v]" -map "[a]" output.mkv
视频，音频视频同时倍速播放。
2022-02-26 11:21:56
https://www.bilibili.com/read/cv1551723
ffmpeg 降噪
2022-03-16 15:11:39
如果有一台虚拟机专门干这个就行了。
https://storage.googleapis.com/13823zxw.appspot.com/AQADlrQxG02QYFZ-.jpg
2022-07-12 08:44:32.263000+08:00
ffmpeg -stream_loop -1 -i input.mp4 -i input.mp3 -map 0:v:0 -map 1:a:0 -c:v copy -c:a aac -b:a 192k   -c:s mov_text -metadata:s:s:0 language=eng -shortest output.mp4
2023-04-10 16:13:35
ffmpeg -i output.mp4 -vf "subtitles=input.srt:force_style='Alignment=2,MarginV=10'" -c:v libx264 -c:a copy output2.mp4
2023-04-12 17:23:39
ffmpeg -i output.mp4 -vf "subtitles=input.srt:force_style='Alignment=10,MarginV=10'" -c:v libx264 -c:a copy output2.mp4
2023-04-12 17:24:20
ffmpeg -i input1min.mp4 -vf "subtitles=input.srt:force_style='Alignment=10,MarginV=10,PrimaryColour=&#fc5603&,Outline=1,OutlineColour=&H000000&'" -c:v libx264 -c:a copy output2.mp4
2023-04-12 17:57:20
https://stackoverflow.com/questions/53631819/is-it-possible-to-add-stroke-to-text-in-ffmpeg
2023-04-12 17:57:23
ffmpeg -i input1min.mp4 -vf "subtitles=input.srt:force_style='Alignment=10,MarginV=10,PrimaryColour=&H0000ff&'" -c:v libx264 -c:a copy output2.mp4
2023-04-12 18:07:31
ffmpeg -i input.mp4 -vf ‘scale=-1:720,pad=1280:720:(1280-iw)/2:0:black’ -c:v libx264 -crf 21 -preset veryfast -aspect 16:9 -c:a copy -f mp4 output.mp4 -y
抖音风格
2023-04-12 20:05:52
ffmpeg -i input1min.mp4 -vf "subtitles=input.srt:force_style='Alignment=10,MarginV=10,FontFile=SourceHanSansCN-Normal.otf,FontSize=24,PrimaryColour=&H00A
5FF&,OutlineColour=&H000000&'" -c:a copy output.mp4
2023-04-13 00:00:31
ffmpeg -i output.mp4 -filter_complex "[0:v]scale=iw*min(720/iw\,1280/ih):ih*min(720/iw\,1280/ih), pad=720:1280:(720-iw*min(720/iw\,1280/ih))/2:(1280-ih*min(720/iw\,1280/ih))/2:black" -c:v libx264 -crf 21 -preset veryfast -aspect 9:16 -c:a copy -f mp4 -y output2.mp4
还不完美
https://storage.googleapis.com/13823zxw.appspot.com/AgACAgUAAxkBAAIvO2Q22NP3KFXo-0JZoC42P_9DHMN8AAKxuzEbjVq5Va5w8pdrZgABdAEAAwIAA3kAAy8E.jpg
2023-04-13 00:14:14
ffmpeg -stream_loop -1 -i input.mp4 -i input.mp3 -map 0:v:0 -map 1:a:0 -c:a aac -b:a 192k -shortest -vf "subtitles=new.srt:force_style='Alignment=10,MarginV=10,FontSize=24,PrimaryColour=&HFFA500&,OutlineColour=&H000000&'" output.mp4

Stop
Copy
这个命令的作用是将输入视频循环播放直到匹配音频文件的长度，并将音频文件和字幕文件合并到输出视频文件中。

具体参数的解释如下：

-stream_loop -1：循环输入视频直到匹配音频时结束
-i input.mp4：指定输入视频文件
-i input.mp3：指定输入音频文件
-map 0:v:0：将输入视频中的第一个视频流映射到输出文件
-map 1:a:0：将输入音频中的第一个音频流映射到输出文件
-c:a aac -b:a 192k：表示将音频流转成 AAC 格式，比特率为 192k
-shortest：将输出文件长度设置为最短输入流的长度（即音频长度）
-vf "subtitles=new.srt:force_style='Alignment=10,MarginV=10,FontSize=24,PrimaryColour=&HFFA500&,OutlineColour=&H000000&'"：指定字幕文件，并通过 force_style 参数设置字幕样式。这里的字幕文件为 new.srt，Alignment=10 表示字幕居中，MarginV=10 表示字幕距离视频顶部的距离为 10 个像素，FontSize=24 表示字幕大小为 24，PrimaryColour=&HFFA500& 表示字幕颜色为橙色，OutlineColour=&H000000&
2023-04-13 11:25:47
非常抱歉，我之前的回答有误。您是正确的，我的建议会导致图像被裁剪。以下是一个可以保持图像不被裁剪的FFmpeg命令，可以将图像的宽高比改为3:4：

ffmpeg -i input.jpg -vf "scale=w=trunc(ih*3/4/2)*2:h=trunc(ih/2)*2, pad=w=ih*3/4:h=ih:x=(ow-iw)/2:y=(oh-ih)/2:color=black" output.jpg
不被裁剪
2023-04-13 14:05:47
3.5调半天的东西，4直接通过了。。。
https://storage.googleapis.com/13823zxw.appspot.com/AgACAgUAAxkBAAIv0mQ-VnF7bPc8pNRfl84stVv9QpJ-AALwtTEbqszxVfCmYLwWLLQ2AQADAgADeQADLwQ.jpg
2023-04-18 16:36:17.655000+08:00
ffmpeg -i output.mp4 -c copy -
map 0 -segment_time 00:05:00 -f segment -reset_timestamps 1 output%03d.mp4
ffmpeg 将视频分成多个长度更小的视频
2023-04-19 14:30:12
ffmpeg
