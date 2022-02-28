形態記得要轉成uint8

```python
# to gray
img = cv2.cvtColor(np.float32(img), cv2.COLOR_BGR2GRAY)

img = np.around(img)
img = np.clip(img,0,255)
img = np.array(img,np.uint8)
                       # w, h, w * channel(1)
qimg = QImage(img, img.shape[1], img.shape[0], img.shape[1], QImage.Format_Indexed8)

self.ui.gray_block.setPixmap(QPixmap(qimg))
```
