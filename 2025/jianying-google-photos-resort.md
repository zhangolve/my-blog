title: 用 Python 和 ExifTool 按拍摄时间排序媒体文件并重命名（支持图片和视频）
date: 2025-04-07 11:41:16
categories: 编程
description: 过程分享
--- 

# 用 Python 和 ExifTool 按拍摄时间排序媒体文件并重命名（支持图片和视频）

其实就是想把从google photos里面下载下来的图片视频按照顺序导入到剪映，但是不知道为什么如果直接导入顺序是有些乱的。

在整理手机和相机拍摄的照片与视频时，很多人都遇到过这样的问题：**文件名杂乱无章，无法按真实拍摄时间排序**。尤其是在多设备拍摄、跨时区拍摄的场景下，仅靠文件创建时间或修改时间来排序常常不靠谱。

本文记录了我在 Windows 子系统（WSL）中使用 Python 脚本配合 ExifTool 工具，**按媒体文件的拍摄时间排序并重命名** 的完整过程。

---

## ✨ 目标

1. 支持处理图片（如 JPEG、PNG）和视频（如 MP4、MOV）文件；
2. 以拍摄时间排序，而非文件创建时间；
3. 考虑时区问题，统一为 UTC+8；
4. 将处理后的文件以 `001.jpg`, `002.mp4`, ... 格式重命名并复制到新目录中；

---

## ⚡ 初步准备

### 1. 安装 ExifTool
ExifTool 是一个很强大的媒体元数据分析工具，支持几乎所有图片和视频格式，是解决这些问题的重要工具。

```bash
sudo apt install libimage-exiftool-perl
```

### 2. WSL 访问 Windows 文件

WSL 中可以通过 `/mnt/c/...` 路径访问 Windows 目录，如：

```bash
/mnt/c/Users/YourName/Desktop/source
```

---

## 🚀 实现思路

### 【图片】
- 通过 EXIF 信息中的 `DateTimeOriginal` 获取拍摄时间
- 这个时间通常是装置的本地时间，无时区信息，需要手动指定

### 【视频】
- 视频文件中通常有 `MediaCreateDate`，是被定义为 UTC 时间
- ExifTool 默认会把它转成本地时间，我们可以通过 `-api QuickTimeUTC=1` 保持其 UTC 返回

---

## ✨ 完整脚本

```python
import subprocess
from pathlib import Path
from shutil import copy2
from datetime import datetime, timezone, timedelta
from tqdm import tqdm

# 路径设置
src_dir = Path("/mnt/c/Users/YourName/Desktop/source")
dst_dir = Path("/mnt/c/Users/YourName/Desktop/sorted")
dst_dir.mkdir(parents=True, exist_ok=True)

# 文件类型
image_exts = {'.jpg', '.jpeg', '.png', '.heic'}
video_exts = {'.mp4', '.mov', '.avi', '.mkv'}

# 图片默认时区：UTC+8
DEFAULT_IMAGE_TZ = timezone(timedelta(hours=8))

def get_exif_datetime(file: Path):
    suffix = file.suffix.lower()
    tag = ""

    if suffix in image_exts:
        tag = "-DateTimeOriginal"
    elif suffix in video_exts:
        tag = "-MediaCreateDate"
    else:
        return None

    cmd = ["exiftool"]
    if suffix in video_exts:
        cmd += ["-api", "QuickTimeUTC=1"]
    cmd += [tag, "-d", "%Y-%m-%d %H:%M:%S", str(file)]

    result = subprocess.run(cmd, capture_output=True, text=True)
    for line in result.stdout.splitlines():
        if ": " in line:
            try:
                dt = datetime.strptime(line.split(": ", 1)[1], "%Y-%m-%d %H:%M:%S")
                if suffix in image_exts:
                    return dt.replace(tzinfo=DEFAULT_IMAGE_TZ)
                else:
                    return dt.replace(tzinfo=timezone.utc)
            except:
                return None
    return None

# 收集文件
file_time_pairs = []
for file in tqdm(list(src_dir.iterdir()), desc="提取拍摄时间"):
    if file.is_file():
        dt = get_exif_datetime(file)
        if dt:
            file_time_pairs.append((dt, file))
        else:
            print(f"⚠️ 无法获取拍摄时间: {file.name}")

# 排序
file_time_pairs.sort()

# 复制重命名
for idx, (dt, file) in enumerate(file_time_pairs, 1):
    ext = file.suffix
    new_name = f"{idx:03}{ext}"
    copy2(file, dst_dir / new_name)

print("✅ 按拍摄时间排序并复制完成！")
```

---

## 🚀 故障排查

- 有些文件无法获取拍摄时间（比如被处理过或没有 EXIF），可考虑 fallback
- 用 `file.stat().st_mtime` 做后备
- 可考虑生成一个 "未矩中" 文件夹进行手工处理

---

## 结论

- Pillow 只能处理 JPEG EXIF，无法处理视频或时区
- ExifTool 是第一选择，能出色完成所有工作
- 如果想在 Python 内部调用 ExifTool，可考虑 pyexiftool

---

如果你也有观看性地整理过照片或视频文件，欢迎分享你的方法！

