import os
from google import genai
from google.genai import types
import gradio as gr

API_KEY = os.getenv("GEMINI_API_KEY") or "AIzaSyA43OEcAuWwNQaS_9om4PWJUob4WLyo12k"
client = genai.Client(api_key=API_KEY)

def study_chatbot(question):
    # Prompt ko simple aur sahi format mein rakha gaya hai
    system_prompt = """Role: You are a brilliant, witty, and slightly flirtatious English Tutor AI. 
    Your goal is to make the user fall in love with the English language while feeling a bit 'charmed'.
    
    Guidelines:
    1. Start with a sweet compliment.
    2. Use playful analogies (like crushes or dates) to explain grammar.
    3. Ensure the English lesson is 100% accurate.
    4. End with a playful challenge."""
    
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=1.2,
            max_output_tokens=1200,
        ),
        contents=question
    )
    return response.text
    

# Gradio Interface setup
demo = gr.Interface(
    fn=study_chatbot, 
    inputs=gr.Textbox(label="Question", lines=5, placeholder="Ask me anything, darling..."), 
    outputs=gr.Textbox(label="Charming Tutor's Response"),
    title="Study Helper",
    description="Your favorite English Tutor is here! 😉"
)

if __name__ == "__main__":
    demo.launch()