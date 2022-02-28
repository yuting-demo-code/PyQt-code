形態記得要轉成uint8

```python
# to gray
img = cv2.cvtColor(np.float32(img), cv2.COLOR_BGR2GRAY)

# to unit8
img = np.array(img,np.uint8)
                      # w, h, w     
qimg = QImage(img, img.shape[1], img.shape[0], img.shape[1], QImage.Format_Indexed8)
self.ui.fft_block.setPixmap(QPixmap(qimg))
```
