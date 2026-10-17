import os

# Get the absolute path to the project root (the folder containing this config.py)
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

speech_file = os.path.join(PROJECT_ROOT, "1. Langchain", "Document_files", "speech.txt")
pdf_file = os.path.join(PROJECT_ROOT, "1. Langchain", "Document_files", "attention.pdf")
text_file = os.path.join(PROJECT_ROOT, "1. Langchain", "Document_files", "Gen AI Terminlogies.txt")

dummy_var_1 = "This is a dummy variable"
dummy_var_2 = "This is another dummy variable"