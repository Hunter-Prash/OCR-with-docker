import easyocr
import os
import time


IMAGE_PATH = "Tesla.png" 

# Check if the image file exists before proceeding
if not os.path.exists(IMAGE_PATH):
    print(f"Error: Image file not found at path: {IMAGE_PATH}")
    print("Please ensure the image file is in the same directory as main.py.")
    exit()

LANGUAGES = ['en']

print("Starting EasyOCR process...")

start_time = time.time()
try:
    # Set gpu=False if you encounter CUDA/GPU errors during local testing
    reader = easyocr.Reader(LANGUAGES, gpu=False) 
    print(f"✅ Model loaded successfully in {time.time() - start_time:.2f} seconds.")
except Exception as e:
    print(f"Error details: {e}")
   

# --- OCR Execution ---
start_time = time.time()
try:
    results = reader.readtext(IMAGE_PATH)
    
    print("\n--- OCR Results ---")
    
    # Extract just the text from the results (results are [bbox, text, confidence])
    extracted_text = " ".join([text[1] for text in results])
    
    print(extracted_text)
    print(f"\nOCR execution time: {time.time() - start_time:.2f} seconds")

    # Optional: Save results to a file for later (will create 'output.txt' in the same folder)
    with open('output.txt', 'w', encoding='utf-8') as f:
        f.write(extracted_text)
        print("Results saved to output.txt")
        
except Exception as e:
    print(f"\n❌ An error occurred during OCR execution: {e}")