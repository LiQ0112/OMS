from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random
#字体默认路径
font_path = r"D:\baozhang\HYLeMiaoTiW.ttf"
#生成验证码图片的高度和宽度
size=(100,30)
#背景颜色，默认为白色
bg_color=(255,255,255)
#字体颜色，默认为蓝色
font_color=(0,0,255)
#干扰线颜色。默认为红色
line_color=(0,0,0)
#是否要加入干扰线
draw_line=True
#加入干扰线条数的上下限
line_number=(1,5)
#验证码的位数
number = 4
#获取 随机颜色
def get_color():
    color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    return color

#生成验证码
def get_code():
    check_code = ""
    for i in range(number):
        random_number = str(random.randint(0,9))
        random_lower_letter = chr(random.randint(97,122))
        random_upper_letter = chr(random.randint(65,90))
        check_code += random.choice([random_number,random_lower_letter,random_upper_letter])
    return check_code

def gene_line(draw,width,height):
    begin = (random.randint(0, width), random.randint(0, height))
    end = (random.randint(0, width), random.randint(0, height))
    draw.line([begin, end], fill=line_color)

#生成验证码
def gene_code():
    #宽的高
    width,height = size
    #绘制图片
    image = Image.new("RGBA",(width,height),bg_color)
    #验证码的字体
    font = ImageFont.truetype(font_path,25)
    #创建画笔
    draw = ImageDraw.Draw(image)
    #生成字符串
    text = get_code()
    font_width,font_height = font.getsize(text)
    # 填充字符串
    draw.text(((width - font_width)/number,
               (height - font_height)/number),
              text,font=font, fill=get_color())
    #判断是否要加干扰线
    if draw_line:
        gene_line(draw, width, height)
        image = image.transform((width + 20, height + 10), Image.AFFINE, (1, -0.3, 0, -0.1, 1, 0),
                               Image.BILINEAR)  # 创建扭曲
        image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)  # 滤镜，边界加强
        return text,image

