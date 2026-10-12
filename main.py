from PIL import Image, ImageDraw, ImageFont
import os


# ======================
# 配置
# ======================

template = "images/template.png"

output_dir = "output"

font_path = "fonts/SourceHanSerif-Medium.ttc"


# 添加姓名的位置
# 根据你的邀请函调整
NAME_POSITION = (866, 330)


# 字体大小
FONT_SIZE = 38


# ======================
# 初始化
# ======================

if not os.path.exists(output_dir):
    os.makedirs(output_dir)


font = ImageFont.truetype(
    font_path,
    FONT_SIZE
)


# ======================
# 读取名单
# ======================

# ======================
# 读取名单，过滤已完成的姓名
# ======================

with open("names.txt", "r", encoding="utf-8") as f:
    names = []

    for line in f:
        line = line.strip()

        if not line:
            continue

        # 以空格 + 1 结尾，表示已经完成
        if line.endswith(" 1"):
            print(f"跳过已完成: {line}")
            continue

        names.append(line)

# ======================
# 批量生成
# ======================

for name in names:

    img = Image.open(template).convert("RGB")

    draw = ImageDraw.Draw(img)


    draw.text(
        NAME_POSITION,
        name,
        font=font,
        fill=(255,255,255)
    )


    save_path = os.path.join(
        output_dir,
        f"{name}.jpg"
    )


    img.save(
        save_path,
        quality=95
    )


    print(
        f"生成完成: {save_path}"
    )


print("全部完成")