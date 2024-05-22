import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
from PIL import Image
import requests
from io import BytesIO
import base64
from pathlib import Path

# 加载环境变量
load_dotenv()

# 定义文本
mtext = """You are a talented digital artist specializing in creating unique and engaging avatars in various artistic styles, including cartoon. You have a profound ability to bring characters to life through vibrant colors, expressive features, and distinctive styles. Your portfolio showcases a wide range of imaginative and visually appealing avatars that capture the essence of the individual's personality or the spirit of the instruction given. With your expertise, you can skillfully interpret prompts and translate them into captivating and personalized avatars. Your work is not only aesthetically pleasing but also captures the whimsical nature of cartoon art, making each creation memorable and special.
-------a portrait of a young woman with a bright, welcoming smile. Her hair is long, cascading down her shoulders, with a sparkling headband atop. She's wearing a sleeveless black top and a delicate gold pendant necklace. Her pose is relaxed, with one arm casually lifted, exuding a carefree and joyful demeanor. The background is a gentle blur, indicating an outdoor setting that's filled with natural light, adding a warm, sunlit quality to the image."""

# 创建头像的函数
def createAvatar():
    client = OpenAI()

    response = client.images.generate(
        model="dall-e-3",
        prompt=mtext,
        size="1024x1024",
        quality="standard",
        n=1,
    )

    image_url = response.data[0].url
    # 从网络API获取图片
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))

    # 显示图片
    st.image(image, caption='图片')
    
    # 下载图片
    return image

# 使用columns来居中按钮
col1, col2, col3 = st.columns([1,1,1])

def doDownload(image):
    # 将图片转换为字节
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    href = f'<a href="data:file/jpg;base64,{img_str}" download="avatar.jpg">下载</a>'
    st.markdown(href, unsafe_allow_html=True)


with col2:
    if st.button("换一张"):
        image = createAvatar()
        doDownload(image)
    else:
        image_url = "photo.jpg"
        image = Image.open(image_url)
        # 在Streamlit应用中显示图片
        st.image(image, caption='更换你的头像')
        doDownload(image)