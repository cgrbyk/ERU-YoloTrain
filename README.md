"# ERU-YoloTrain" 

cmd komutları
Play Video
python flow --model cfg/yolo.cfg --load bin/yolov2.weights --demo videofile.mp4 --gpu 0.7 --saveVideo

Train model
python flow --model cfg/yolov2-tiny-voc-1c.cfg --load bin/yolov2-tiny-voc.weights --train --annotation Train_Data/annotations --dataset Train_Data/images --gpu 1 --epoch 1000

Sciptler
videoObjectSelector.py - Hazır olan modeli video üzerinde çalıştırır.
imageObjectSellector.py - Hazır olan modeli Resim üzerinde çalıştırır.
Train-Data
objectsellector.py - images klasörü içindeki resimleri kullanıcıya gösterir ve seçilen alan ve nesne bilgisi ile annotation dosyalarını oluşturur.
generate_xml.py - objectsellector.py içerisinden çağırılır verilen parametreler ile annotation xml dosyasını oluşturur.
 

