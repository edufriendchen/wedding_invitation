from PIL import Image
import matplotlib.pyplot as plt


img = Image.open("images/template.png")

plt.figure(figsize=(12,8))
plt.imshow(img)

plt.grid()

def onclick(event):
    print(
        "点击坐标:",
        int(event.xdata),
        int(event.ydata)
    )

plt.connect(
    'button_press_event',
    onclick
)

plt.show()