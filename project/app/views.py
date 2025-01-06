from django.shortcuts import render

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate


import os 
from dotenv import load_dotenv
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")



genai.configure(api_key=api_key)

# Create your views here.


FRONTEND_BOT_TEMPLATE = """
You are a frontend development expert. Your goal is to analyze the provided code: {code}, identify any errors, and provide the corrected code only.

Rules for output:
- Provide ONLY the corrected code in HTML, CSS, JavaScript, or Bootstrap as applicable.
- DO NOT include markdown backticks (`) or any other surrounding symbols (e.g., ```html, ```, etc.).
- NO explanations or comments.
- The output must start directly with the HTML code and end with the closing tags, with no extra formatting or symbols.
- Maintain proper indentation.

"""

llm=  ChatGoogleGenerativeAI(model='gemini-1.5-pro', api_key=api_key)

prompt = ChatPromptTemplate.from_template(FRONTEND_BOT_TEMPLATE)

chain = LLMChain(llm=llm, prompt=prompt)


default = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Awais Shakeel - AI Frontend Engineer</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body, html {
            margin: 0;
            padding: 0;
            height: 100%;
            font-family: 'Arial', sans-serif;
            overflow: hidden;
        }

        /* Linear gradient background changing animation */
        @keyframes gradientChange {
            0% { background: linear-gradient(135deg, #6a11cb, #2575fc); }
            25% { background: linear-gradient(135deg, #00b4db, #0083b0); }
            50% { background: linear-gradient(135deg, #ff7e5f, #feb47b); }
            75% { background: linear-gradient(135deg, #2b5876, #4e4376); }
            100% { background: linear-gradient(135deg, #6a11cb, #2575fc); }
        }

        /* Apply background gradient change animation */
        .background {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            animation: gradientChange 15s infinite ease-in-out;
        }

        /* Floating bubbles animation */
        .bubble {
            position: absolute;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.7);
            animation: float 10s ease-in-out infinite;
        }

        @keyframes float {
            0% {
                transform: translateY(100vh) scale(0.5);
                opacity: 1;
            }
            100% {
                transform: translateY(-100vh) scale(1);
                opacity: 0;
            }
        }

        /* Centered text styling */
        .center-text {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            color: white;
            font-size: 3rem;
            font-weight: bold;
            text-align: center;
            z-index: 10;
            animation: fadeIn 3s ease-out forwards;
        }

        @keyframes fadeIn {
            0% { opacity: 0; }
            100% { opacity: 1; }
        }

        /* Random animation delay and sizes for bubbles */
        .bubble:nth-child(1) { width: 60px; height: 60px; left: 10%; animation-duration: 12s; animation-delay: 2s; }
        .bubble:nth-child(2) { width: 50px; height: 50px; left: 30%; animation-duration: 15s; animation-delay: 4s; }
        .bubble:nth-child(3) { width: 70px; height: 70px; left: 50%; animation-duration: 13s; animation-delay: 6s; }
        .bubble:nth-child(4) { width: 90px; height: 90px; left: 70%; animation-duration: 17s; animation-delay: 8s; }
        .bubble:nth-child(5) { width: 80px; height: 80px; left: 20%; animation-duration: 18s; animation-delay: 10s; }
        .bubble:nth-child(6) { width: 55px; height: 55px; left: 40%; animation-duration: 16s; animation-delay: 12s; }
        .bubble:nth-child(7) { width: 50px; height: 50px; left: 60%; animation-duration: 14s; animation-delay: 14s; }

    </style>
</head>
<body>

    <!-- Background color animation -->
    <div class="background"></div>

    <!-- Floating bubbles -->
    <div class="bubble"></div>
    <div class="bubble"></div>
    <div class="bubble"></div>
    <div class="bubble"></div>
    <div class="bubble"></div>
    <div class="bubble"></div>
    <div class="bubble"></div>

    <!-- Centered Text -->
    <div class="center-text">
         <br>
        AI Frontend Engineer
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>

'''


def home(request):
    response = None
    if request.method == 'POST':
        query = request.POST.get('query')  # Use .get() to handle missing 'query'
        if query:
            response = chain.run(code=query).strip()
            
            
    return render(request, 'preview.html', {'response': response , 'default':default})
