import os
import json
import pandas as pd
import traceback
import streamlit as st
from dotenv import load_dotenv
from src.mcqgenerator.utilis import read_file, get_table_data
from langchain.callbacks import get_openai_callback
from src.mcqgenerator.logger import logging
from src.mcqgenerator.MCQGenerator import generate_evaluate_chain


with open('C:\Users\HP\PycharmProjects\Generative_AI\response.json', 'r') as file:
