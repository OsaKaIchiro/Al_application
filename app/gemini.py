import google.generativeai as genai
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

import google.generativeai as genai

API_KEY =  os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")


text = input("ユーザー >>>")
input_text = f"""

あなたは未来予測の専門家です。
以下の事象が起こるかどうかを予測し、「はい」または「いいえ」のみで答えてください。
{text}という事象は起こると思いますか？

"""


response = model.generate_content(input_text)
print(response.text)