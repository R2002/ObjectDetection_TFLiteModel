# 概要
「TensorFlowLiteモデルメーカーによるオブジェクト検出」の日本語化版です。
https://www.tensorflow.org/lite/tutorials/model_maker_object_detection  
  
コードは下記を参考にしています。  
https://colab.research.google.com/github/google-coral/tutorials/blob/master/retrain_efficientdet_model_maker_tf2.ipynb  
  
作成したモデルはAndroidアプリ（下記例）に利用する想定です。  
https://github.com/ymshun/ObjectDetectionApp

# 実行手順
このリポジトリをダウンロードすると6から開始可能です。  
5までは実行済みのため、補足として記載しておきます。  

## 1. Cloud SDK のインストール
https://cloud.google.com/sdk/docs/install?hl=ja

## 2. CloudSDK環境で、CSVファイルの取得
下記コマンドを実行する。  
> subprocess.call("gsutil cp gs://cloud-ml-data/img/openimage/csv/salads_ml_use.csv .", shell=True)  

ファイルをinputs/sample/salads_ml_use.csvへ移動する。

## 3. CSVファイルのB列をsample_file（inputs/sample/sample_file.txt）へコピー
エクセルファイルからテキストファイルへ、GUI上でコピーした方が早いのでそのようにします。

## 4. CloudSDK環境で、ファイル（1_download.py）の実行
inputs/sample/sample_file.txtに記載がある画像データをダウンロードする。

## 5. Anaconda環境等で、ファイル（2_fileConvert.py）の実行
inputs/sample/salads_ml_use.csvからinputs/sample/sample.csvへ内容を書き直す。

## 6. Anaconda環境等で、Process.ipynbの実行
実行する前に下記コマンドを実行すること。  
> pip install -r requirements.txt

# 備考
## TfLite公開モデルでは物体検出モデルは動作するものの、tflite-model-makerで作成したモデルだとエラーが出る。
1日ほど詰まったので備忘のために記載します。

### 起こるエラーの例  
・Cannot copy from a TensorFlowLite tensor (StatefulPartitionedCall:1) with shape [1, 10] to a Java object with shape [1, 10, 4]  
https://stackoverflow.com/questions/70054904/cannot-copy-from-a-tensorflowlite-tensor-statefulpartitionedcall1-with-shape

### 理由
（なぜか）TensorHubのtfliteファイルのOutputsの順番と、tflite-model-makerのOutputsの順番が違う。  
・TensorHub Efficientdet  
https://tfhub.dev/tensorflow/lite-model/efficientdet/lite4/detection/metadata/2  
・tflite-model-maker Efficientdet  
https://tensorflow.org/lite/tutorials/model_maker_object_detection  
  
出力の順番を確認するにはNetronをお勧めします。  
https://netron.app/  

### 解決策
下記の通り、ObjectDetectorの出力の順番を調整する必要がある。コードの書き方によって対応が違うので注意が必要。
> outputMap.put(0, outputScores);
> outputMap.put(1, outputLocations);
> outputMap.put(2, numDetections);
> outputMap.put(3, outputClasses);

https://discuss.tensorflow.org/t/object-detection-android-app-creates-error-with-model-from-tflite-model-maker-it-had-worked-for-many-weeks-a-until-a-few-weeks-ago/4015/9
