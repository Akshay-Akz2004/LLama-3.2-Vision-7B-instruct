import streamlit as st
from openai import OpenAI

# Configure the client with custom base URL and API key
client = OpenAI(
    base_url="https://api.thehive.ai/api/v3/",  # Hive AI's endpoint
    api_key="T4L0n9mDcWPPlaXbPCZK23Xg4v0vY7gu"  # Replace with your API key
)

def get_completion(prompt, image_url, model="meta-llama/llama-3.2-11b-vision-instruct"):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {"url": image_url}
                    }
                ]
            }
        ],
        temperature=0.7,
        max_tokens=1000
    )
    return response.choices[0].message.content

# Streamlit UI
st.title("LLamA 3.2 11b-vision Demo")

image_url = st.text_input("Enter Image URL:", "https://cdn.creati.ai/ai-tools/product-image/hive-ai-detector.webp")
st.image(image_url, caption="Image for Analysis")

prompt = st.text_area("Enter your prompt:", "Describe the scene. Provide only relevant information")

if st.button("Generate Response"):
    with st.spinner("Generating response..."):
        result = get_completion(prompt, image_url)
        st.subheader("Response:")
        st.write(result)