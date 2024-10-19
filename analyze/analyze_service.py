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
                        "text": "Based on the user's physical attributes and the clothing material, assess if the outfit in the image would fit and suit the user. The user is 174cm weighs 64kg, and has sensitive skin. Analyze how well the outfit in the image will fit the user's body, if the material will be suitable for their skin sensitivity, and if the clothing size is appropriate. Also, determine if the style complements the user's physique. Respond in Korean.",
                        # Provide detailed descriptions of clothing in photos for visually impaired individuals in Korean.
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
