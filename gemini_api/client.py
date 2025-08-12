import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')

def get_car_ai_bio(modelo, marca, ano):
    prompt = f"""
    Gere uma descrição atrativa para venda do carro {marca} {modelo} {ano} em até 250 caracteres.
    Destaque características específicas desse modelo de carro. 
    Descreva especificações tecnicas desse modelo de carro.
    """
    response = model.generate_content(prompt)
    return response.text.strip()
