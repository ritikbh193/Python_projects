
'''Title of the Conversation'''
# from PIL import Image, ImageDraw, ImageFont

# # Define conversation parts
# conversations = ["A conversation between Adam and John about improving communication skills. "]

# # Image size and settings
# width, height = 1980, 1080
# background_color = (255, 255, 255)  # White
# text_color = (0, 0, 0)  # Black
# font_size = 60

# # Load a font
# font = ImageFont.truetype("times.ttf", font_size)

# def format_text_with_newlines(text, max_words_per_line=10):
#     words = text.split()
#     lines = []
#     for i in range(0, len(words), max_words_per_line):
#         lines.append(' '.join(words[i:i + max_words_per_line]))
#     return '\n'.join(lines)

# def create_image(text, index):
#     formatted_text = format_text_with_newlines(text)
    
#     # Create a new image with white background
#     img = Image.new('RGB', (width, height), background_color)
#     draw = ImageDraw.Draw(img)
    
#     # Calculate text size and position
#     bbox = draw.textbbox((0, 0), formatted_text, font=font)
#     text_width = bbox[2] - bbox[0]
#     text_height = bbox[3] - bbox[1]
    
#     text_x = (width - text_width) / 2
#     text_y = (height - text_height) / 2
    
#     # Draw text on image
#     draw.text((text_x, text_y), formatted_text, font=font, fill=text_color)
    
#     # Save image
#     img.save(f'conversation_{index}.png')

# # Generate images for each part of the conversation
# for i, conversation in enumerate(conversations):
#     create_image(conversation, i + 1)





'''Conversation'''
# from PIL import Image, ImageDraw, ImageFont

# # Define conversation parts
# conversations = [
#     "Adam: Hey John, I’ve been thinking a lot about how to improve my communication skills. Any tips?",
#     "John: Absolutely, Adam! Communication skills are super important. First off, active listening is key. It’s not just about hearing the words but really understanding what the other person is trying to say.",
#     "Adam: That makes sense. How do you practice active listening?",
#     "John: One way is to focus fully on the speaker. That means putting away distractions like your phone or computer. Also, show that you’re listening through nodding or brief verbal acknowledgments.",
#     "Adam: Got it. And what about speaking clearly? I sometimes feel like I’m not getting my point across.",
#     "John: Clarity is crucial. Try to be concise and organized in your thoughts. It helps to structure what you want to say before you say it. Think of it like giving a mini-presentation.",
#     "Adam: That’s a good idea. Any advice on handling misunderstandings or disagreements?",
#     "John: Definitely. When a misunderstanding arises, stay calm and avoid jumping to conclusions. Ask clarifying questions and paraphrase what you’ve heard to ensure you’ve understood correctly.",
#     "Adam: Paraphrasing sounds useful. How do you approach disagreements?",
#     "John: Approach them with a mindset of collaboration, not confrontation. Focus on finding common ground and understanding the other person’s perspective. It’s more about solving the problem together than winning the argument.",
#     "Adam: I like that approach. Any final tips for improving communication in everyday situations?",
#     "John: Practice empathy. Try to put yourself in the other person’s shoes. Also, be aware of non-verbal cues, like body language and tone of voice. They can often convey as much as, or even more than, words.",
#     "Adam: Thanks, John. This is really helpful. I’ll start practicing these techniques and see how it goes.",
#     "John: No problem, Adam! Let me know how it works out. Good communication is a skill you can keep developing, so just keep at it!"
# ]

# # Image size and settings
# width, height = 1980, 1080
# background_color = (255, 255, 255)  # White
# text_color = (0, 0, 0)  # Black
# font_size = 60

# # Load a font
# font = ImageFont.truetype("times.ttf", font_size)

# def format_text_with_newlines(text, max_words_per_line=10):
#     words = text.split()
#     lines = []
#     for i in range(0, len(words), max_words_per_line):
#         lines.append(' '.join(words[i:i + max_words_per_line]))
#     return '\n'.join(lines)

# def create_image(text, index):
#     formatted_text = format_text_with_newlines(text)
    
#     # Create a new image with white background
#     img = Image.new('RGB', (width, height), background_color)
#     draw = ImageDraw.Draw(img)
    
#     # Calculate text size and position
#     bbox = draw.textbbox((0, 0), formatted_text, font=font)
#     text_width = bbox[2] - bbox[0]
#     text_height = bbox[3] - bbox[1]
    
#     text_x = (width - text_width) / 2
#     text_y = (height - text_height) / 2
    
#     # Draw text on image
#     draw.text((text_x, text_y), formatted_text, font=font, fill=text_color)
    
#     # Save image
#     img.save(f'conversation_{index}.png')

# # Generate images for each part of the conversation
# for i, conversation in enumerate(conversations):
#     create_image(conversation, i + 1)




'''Converting a video by frames'''
import cv2
import os

# Path to the images and the output video
image_folder = r'C:\python1\conversation'  # Directory where your images are located
video_name = 'output_video.mp4'  # Output video file name

# Define video parameters
fps = 1  # Frames per second (adjust based on your needs)
frame_size = (1980, 1080)  # Size of the frames in the video

# Get all image filenames
images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
images.sort()  # Ensure images are in order

# Initialize video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for MP4
video_writer = cv2.VideoWriter(video_name, fourcc, fps, frame_size)

for image in images:
    image_path = os.path.join(image_folder, image)
    frame = cv2.imread(image_path)
    
    # Resize the image to match frame_size (if needed)
    if (frame.shape[1], frame.shape[0]) != frame_size:
        frame = cv2.resize(frame, frame_size)
    
    video_writer.write(frame)  # Write the frame to the video

video_writer.release()  # Finalize the video file
cv2.destroyAllWindows()  # Clean up
