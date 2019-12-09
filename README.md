## 1.引用
### 1)比赛地址
[智能盘点—钢筋数量AI识别](https://www.datafountain.cn/competitions/332/details)
### 2)引用的代码 https://github.com/SHERLOCKLS/detect_steel_darknetyolo
修改内容: 
	(1)原来的代码少了data文件夹，
	(2)使用的yolo-spp.cfg并不能用，改回yolo.cfg.
	(3)makefile 解开了一些mkdir创建文件夹的注释。

### 3)数据集链接 https://pan.baidu.com/share/init?surl=OgRtidoP9k4tSpsxVSe8JQ  提取码: hm9i


----------
## 2. 依赖
`pandas`, `tqdm` , `numpy`, `opencv`


----------
## 3.使用方法
安装:

    git clone https://github.com/tutan123/detect_steel_yolov3_darknet.git
    cd detect_steel_darknetyolo
    make -j
    pip install -r requirements.txt
下载数据并解压,训练和测试图像分别放到train目录和test目录,目录结构如下:

    - detect_steel_darknetyolo
	    train_labels.csv
	    train/
	    test/
      
生成训练的label文件

    - python gen_labels.py

将label/文件夹下的文件拷贝到train/目录
	  
	- cp -r label/* train/

训练:

    ./get_weight.sh
    ./train.sh
预测:

    python infer.py

单张照片预测:

	./darknet detector test voc.data cfg/yolov3.cfg backup/yolov3_final.weights test/FF5AE15C.jpg


## 4. 效果:
线上 0.96+


----------


## 5. 参考

> [darknet-yolo](https://github.com/pjreddie/darknet)


    
    
    
