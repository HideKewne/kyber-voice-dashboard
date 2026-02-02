#!/usr/bin/env python3
"""Generate 2 White variant mockup with different layout"""
import os
from google import genai
from google.genai import types

# Gemini API key
api_key = "AIzaSyBtjuQoQXf8hq7UGCEcGt4ya1ZRsWzssw4"

client = genai.Client(api_key=api_key)

prompt = """Generate a high-fidelity UI mockup for "Kyber" Voice AI Agent SaaS Agency Dashboard with GLASSMORPHISM design.

EXACT SPECIFICATIONS:

**Style:** Clean white minimal glassmorphism with blue accents
**Format:** Desktop dashboard, 1440px width, high resolution

**VARIANT 2 LAYOUT - Different from standard:**
- TOP NAVIGATION BAR instead of sidebar (horizontal nav)
- Logo "Kyber" with stylized K icon on the left of top nav bar
- Navigation items horizontally: Overview, Clients, Interviews, Knowledge Base, Export Hub, Settings
- User avatar and notifications on the right of top nav bar
- Search bar centered in top nav

**Main content below nav bar:**
- Large hero metric card spanning full width showing "24 Recent Interviews" with a large chart
- Below: 3 equal-width metric cards in a row (Pending Clients: 8, Avg Quality Score: 8.7/10, Completion Rate: 94%)
- Bottom section: Two-column layout with Recent Activity list on left, Quick Actions on right

**Colors:**
- Primary accent: #3B82F6 (Blue) for CTAs, links
- Primary hover: #2563EB (Darker blue)
- Background: #FAFAFA (Off-white)
- Card backgrounds: rgba(255, 255, 255, 0.7) with backdrop-filter blur(20px)
- Card borders: 1px solid rgba(255, 255, 255, 0.5)
- Box shadows: 0 8px 32px rgba(0, 0, 0, 0.08)
- Headlines: #18181B (Near black)
- Body text: #52525B (Gray)

**Typography:**
- Font: Inter, sans-serif
- Headlines: Bold (700)
- Body: Regular (400)

**Glassmorphism effects:**
- Cards: frosted white glass with blur, soft shadows
- Border-radius: 24px on all cards
- Subtle shadows and depth
- Top nav bar also has glass effect

**Must include:**
- "Kyber" logo with stylized K icon (keep same logo style, blue accent)
- Dropdown menu in navigation
- Search bar with "Search & Ask" placeholder
- Clean, minimal, not cluttered
- Sans-serif typography
- Rounded edges everywhere
- Welcome text "Good morning, Jay"
"""

print("Generating 2 White variant mockup...")
response = client.models.generate_content(
    model="gemini-3-pro-image-preview",
    contents=[prompt],
    config=types.GenerateContentConfig(
        response_modalities=['TEXT', 'IMAGE'],
        image_config=types.ImageConfig(
            aspect_ratio="16:9",
            image_size="2K"
        ),
    ),
)

# Save the generated image
for part in response.parts:
    if part.text:
        print(f"Response text: {part.text}")
    elif part.inline_data:
        image = part.as_image()
        output_path = "/home/ubuntu/voice-agent-ui/mockups/2-white-dashboard-mockup.jpg"
        image.save(output_path)
        print(f"Image saved to: {output_path}")

print("Done generating 2 White variant!")
