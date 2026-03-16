import vertexai
from vertexai.generative_models import GenerativeModel, Part, Image, Content
import sys

def analyze_bouquet_image(project_id: str, location: str):
    # Initialize Vertex AI
    vertexai.init(project=project_id, location=location)
    
    # Load the Gemini multimodal model (2.0 as requested)
    model = GenerativeModel("gemini-2.0-flash-001")
    
    # Load image part and make sure the image file is correct and matches this code as image.jpeg
    image_path = "/home/student/image.jpeg"
    image_part = Part.from_image(Image.load_from_file(image_path))
    
    # Initial image analysis with streaming
    print("📷 Image Analysis: ", end="", flush=True)
    response_stream = model.generate_content(
        [
            image_part,
            Part.from_text("What is shown in this image?")
        ],
        stream=True
    )
    
    # Print streamed response
    full_response = ""
    for chunk in response_stream:
        if chunk.text:
            print(chunk.text, end="", flush=True)
            full_response += chunk.text
    print("\n")
    
    # Start chat with proper history format
    # Include the initial Q&A in chat history
    chat_history = [
        Content(role="user", parts=[image_part, Part.from_text("What is shown in this image?")]),
        Content(role="model", parts=[Part.from_text(full_response)])
    ]
    
    chat = model.start_chat(history=chat_history)
    
    print("\n🎤 Chat with Gemini (type 'exit' to quit):")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        
        try:
            # Send message with streaming
            response_stream = chat.send_message(user_input, stream=True)
            print("Gemini: ", end="", flush=True)
            
            for chunk in response_stream:
                if chunk.text:
                    print(chunk.text, end="", flush=True)
            print()  # New line after complete response
            
        except Exception as e:
            print(f"Error: {e}")
            break

# Set your project and location
project_id = "<PROJECT-ID>" <----------- SUBSTITUA AQUI
location = "<REGION>" <---------------SUBSTITUA AQUI

# Run the function
analyze_bouquet_image(project_id, location)
