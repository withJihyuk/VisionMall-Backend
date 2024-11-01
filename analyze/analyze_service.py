from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("GPT_API_KEY"))


def analyze_image(base64_image):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Provide detailed descriptions of clothing in photos for visually impaired individuals in Korean."
                    },
                    {
                        "type": "image_url",
                        "image_url": {"url": f"{base64_image}"},
                    },
                ],
            }
        ],
        max_tokens=600,
    )
    return response.choices[0].message.content
