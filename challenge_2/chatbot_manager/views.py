from django.shortcuts import render

import requests
import json

import os
from dotenv import load_dotenv
import json

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"
api_key = "YOUR_API_KEY"

# Create your views here.
def ask(request):
    