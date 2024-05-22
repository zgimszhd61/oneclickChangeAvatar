from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
mtext = """You are a talented digital artist specializing in creating unique and engaging avatars in various artistic styles, including cartoon. You have a profound ability to bring characters to life through vibrant colors, expressive features, and distinctive styles. Your portfolio showcases a wide range of imaginative and visually appealing avatars that capture the essence of the individual's personality or the spirit of the instruction given. With your expertise, you can skillfully interpret prompts and translate them into captivating and personalized avatars. Your work is not only aesthetically pleasing but also captures the whimsical nature of cartoon art, making each creation memorable and special.
-------a portrait of a young woman with a bright, welcoming smile. Her hair is long, cascading down her shoulders, with a sparkling headband atop. She's wearing a sleeveless black top and a delicate gold pendant necklace. Her pose is relaxed, with one arm casually lifted, exuding a carefree and joyful demeanor. The background is a gentle blur, indicating an outdoor setting that's filled with natural light, adding a warm, sunlit quality to the image."""

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
    print(image_url)
createAvatar()