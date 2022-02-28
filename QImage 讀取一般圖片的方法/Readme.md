```python
# original img
# 讀取包含中文路徑的方法
img = cv2.imdecode( np.fromfile( file = filename, dtype = np.uint8 ), cv2.IMREAD_COLOR ) 
                            # w, h, w * channel(3)
qimg = QImage(img, img.shape[1], img.shape[0], img.shape[1]*img.shape[2], QImage.Format_RGB888).rgbSwapped()
self.ui.img_block.setPixmap(QPixmap(qimg))
```
