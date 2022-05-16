# Requirements
* python >= 3.7.1
* pytorch >= 1.1.0
* torchvision >= 0.3.0 
* pyyaml==3.13
* scikit-image==0.14.1
* numpy==1.15.4
* scipy==1.1.0
* tensorboardX==2.0
* opencv-python==4.1.2.30
* Cython==0.29.2
* matplotlib==3.0.2
* timm == 0.3.2
* apex == 0.1

默认使用多卡分布式训练，请根据实际计算资源配置训练脚本。

# Dataset

可以选择下载已经由我们处理之后的数据集、或自行使用原始的`MS-Celeb-v1c`进行处理，任选其一均可。推荐使用已处理的数据集。

- 已经由我们清理图片、添加口罩、裁剪人脸、重新缩放后的数据集（包括训练集和测试集）。链接：https://pan.baidu.com/s/1ARoSrIlq4gQPEJw2RmhpYA?pwd=zivd 提取码：zivd 
- 原始的`MS-Celeb-v1c`数据集链接：https://pan.baidu.com/s/1bV6fRG4A9LxKT0KTe_ulYA?pwd=6qio 提取码：6qio。需自行处理口罩、裁剪人脸并缩放到224x224。

# Train
## 1. 训练集

`msra_tiny_cropped_resized.zip`为训练集，解压，记录路径。

## 2. 训练

实验分为两个任务：recognition和detection

### Step1. 设置backbone

编辑 [backbone_conf.yaml](./training_mode/backbone_conf.yaml) 文件配置网络参数。默认使用Swin-T，可以自行更改为Swin-S，Swin-B等不同规模的Swin-Transformer模型。

- recognition任务使用`SwinTransformer`或`SwinTransformerNew`
- detection任务使用`SwinTransformerDet`或`SwinTransformerNewDet`

### Step2. 设置head

编辑 [head_conf.yaml](./training_mode/head_conf.yaml) 文件配置head参数。比较推荐使用`MV-Softmax`。

- recognition任务head的`feat_dim`为512
- detection任务head的`feat_dim`为1

### Step3. 设置训练参数

根据具体环境配置 [train_rec.sh](./training_mode/swin_training/train_rec.sh) 或 [train_det.sh](./training_mode/swin_training/train_det.sh)。

### Step4. 开始训练

```bash
cd training_mode/swin_training/

# 训练 recognition
sh train_rec.sh

# 训练 detection
sh train_det.sh
```

如果是多机多卡分布式训练，需要在每个机器都启动训练脚本。

训练完成后在 log/train 目录下存放训练日志文件，按任务分类。

# Evaluation  
## 1. 测试集

`lfw_resized.zip`，`calfw_resized.zip`和`cplfw_resized.zip`为训练集，解压，记录路径。

## 2. 配置

1. [backbone_conf.yaml](./test_protocol/backbone_conf.yaml) 与训练一致
2. [data_conf.yaml](./test_protocol/data_conf.yaml)：
    - pairs_file_path：仅测试recognition模型用到的文件，其中每一行是第一张测试图片的相对路径、第二张测试图片的相对路径、标签。如果两张图片是同一个人则标签为1，反之为0。
    - cropped_face_folder：测试集路径
    - image_list_file_path：测试集中所有图片的相对路径
3. 根据具体环境自行配置 [test_lfw.sh](./test_protocol/test_lfw.sh) 和 [test_det.sh](./test_protocol/test_det.sh)

## 3. 测试

```bash
cd test_protocol

# 测试 recognition
sh test_lfw.sh

# 测试 detection
sh test_det.sh
```

# Model

训练好的模型下载链接：https://pan.baidu.com/s/1eUWe-Qso5JxJ3O9rzFOE3w?pwd=gm8x 提取码：gm8x 

18Epoch，3 warmup
