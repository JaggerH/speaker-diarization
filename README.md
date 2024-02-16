# pyannote-audio 安装指南

本指南将引导您完成安装 `pyannote-audio` 的过程，包括设置虚拟环境、安装CUDA、安装PyTorch和`pyannote-audio`。

## 步骤 1: 设置虚拟环境

使用 Python 的 `venv` 模块创建一个新的虚拟环境，并激活它。打开命令行或终端并运行以下命令：

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

这些命令将创建一个名为 .venv 的新虚拟环境，并激活它。在 Windows 上，激活脚本位于 .\\.venv\Scripts\activate，而在 Unix 或 MacOS 上，您应该使用 source .venv/bin/activate。

## 步骤 2: 安装 CUDA
访问 [NVIDIA CUDA 下载页面](https://developer.nvidia.com/cuda-downloads) 并根据您的操作系统下载并安装合适的CUDA版本。

确保下载与您的硬件和操作系统兼容的CUDA版本。


## 步骤 3: 安装 PyTorch
根据您安装的 CUDA 版本，访问 [PyTorch 官方网站](https://pytorch.org/) 以生成相应的安装命令。

在 PyTorch 网站的安装部分，选择与您的环境匹配的配置选项（包括您的CUDA版本），网站将为您提供用于安装PyTorch的具体 pip 命令。

在您的虚拟环境中运行生成的安装命令。


## 步骤 4: 安装 pyannote-audio和pydub
在您的虚拟环境中，使用 pip 安装 [pyannote.audio](https://github.com/pyannote/pyannote-audio#installation)：


```bash
pip install pyannote.audio pydub
```
这将安装 pydub, pyannote.audio 及其所有依赖项。

## 步骤 5: 下载ffmpeg.exe和ffprobe.exe至根目录
## 步骤 6: 配置config.yaml
复制config.yaml.backup为config.yaml,将HUGGINGFACE_ACCESS_TOKEN_GOES_HERE改为你的。
## 步骤 7: 运行代码
```
python SpeakerDiarization.py "C:\path\to\your\audiofile.mp3"
```