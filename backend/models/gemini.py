import base64
import time
from typing import Awaitable, Callable, Dict, List
from openai.types.chat import ChatCompletionMessageParam
import google.generativeai as genai
from llm import Completion, Llm


def extract_image_from_messages(
    messages: List[ChatCompletionMessageParam],
) -> Dict[str, str]:
    """
    Extracts image data from OpenAI-style chat completion messages.

    Args:
        messages: List of ChatCompletionMessageParam containing message content

    Returns:
        Dictionary with mime_type and data keys for the first image found
    """
    for content_part in messages[-1]["content"]:  # type: ignore
        if content_part["type"] == "image_url":  # type: ignore
            image_url = content_part["image_url"]["url"]  # type: ignore
            if image_url.startswith("data:"):  # type: ignore
                # Extract base64 data and mime type for data URLs
                mime_type = image_url.split(";")[0].split(":")[1]  # type: ignore
                base64_data = image_url.split(",")[1]  # type: ignore
                return {"mime_type": mime_type, "data": base64_data}
            else:
                # Handle regular URLs - would need to download and convert to base64
                # For now, just return the URI
                return {"uri": image_url}  # type: ignore

    # No image found
    raise ValueError("No image found in messages")


async def stream_gemini_response(
    messages: List[ChatCompletionMessageParam],
    api_key: str,
    callback: Callable[[str], Awaitable[None]],
    model_name: str,
) -> Completion:
    start_time = time.time()

    # Get image data from messages
    image_data = extract_image_from_messages(messages)

    # Configure the API key
    genai.configure(api_key=api_key)
    
    # Create the model
    model = genai.GenerativeModel(model_name)
    
    full_response = ""

    # Prepare the content with text and image
    content = [
        messages[0]["content"],  # type: ignore
        {
            "mime_type": image_data["mime_type"],
            "data": base64.b64decode(image_data["data"])
        }
    ]

    # Generate content with streaming
    response = model.generate_content(
        content,
        generation_config=genai.types.GenerationConfig(
            temperature=0,
            max_output_tokens=8000,
        ),
        stream=True
    )

    for chunk in response:
        # Check if chunk has valid parts and text content
        if hasattr(chunk, 'parts') and chunk.parts:
            for part in chunk.parts:
                if hasattr(part, 'text') and part.text:
                    full_response += part.text
                    await callback(part.text)
        # Fallback: try to access text directly if parts are not available
        elif hasattr(chunk, 'text'):
            try:
                if chunk.text:
                    full_response += chunk.text
                    await callback(chunk.text)
            except ValueError as e:
                # Handle cases where text accessor fails (e.g., blocked content)
                print(f"Gemini chunk text access failed: {e}")
                # Check if there's a finish_reason indicating why it failed
                if hasattr(chunk, 'candidates') and chunk.candidates:
                    for candidate in chunk.candidates:
                        if hasattr(candidate, 'finish_reason'):
                            print(f"Finish reason: {candidate.finish_reason}")
                            if candidate.finish_reason == 2:  # SAFETY
                                raise Exception("Content was blocked by Gemini safety filters")
                            elif candidate.finish_reason == 3:  # RECITATION
                                raise Exception("Content was blocked due to recitation concerns")
                            elif candidate.finish_reason == 4:  # OTHER
                                raise Exception("Content was blocked for other reasons")
                continue

    completion_time = time.time() - start_time
    return {"duration": completion_time, "code": full_response}
