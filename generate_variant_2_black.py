#!/usr/bin/env python3
"""Generate 2 Black variant mockup with different layout"""
import os
from google import genai
from google.genai import types

# Gemini API key
api_key = "AIzaSyBtjuQoQXf8hq7UGCEcGt4ya1ZRsWzssw4"

client = genai.Client(api_key=api_key)

prompt = """Generate a high-fidelity UI mockup for "Kyber" Voice AI Agent SaaS Agency Dashboard with GLASSMORPHISM design.

EXACT SPECIFICATIONS:

**Style:** Black/White/Gold chic boutique glassmorphism
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
- Primary accent: #D4AF37 (Gold) for CTAs, accents, focus states
- Primary hover: #B8952D (Dark gold)
- Background: #0D0D0D (Near black)
- Card backgrounds: rgba(26, 26, 26, 0.7) with backdrop-filter blur(20px)
- Card borders: 1px solid rgba(212, 175, 55, 0.2) (subtle gold tint)
- Headlines: #FFFFFF (White)
- Body text: #F5F5F5 (Light gray)

**Typography:**
- Font: Inter, sans-serif
- Headlines: Bold (700)
- Body: Regular (400)

**Glassmorphism effects:**
- Cards: frosted glass with blur, subtle gold border glow
- Border-radius: 24px on all cards
- Subtle shadows and depth
- Top nav bar also has glass effect

**Must include:**
- "Kyber" logo with stylized K icon (keep same logo style)
- Dropdown menu in navigation
- Search bar with "Search & Ask" placeholder
- Clean, minimal, not cluttered
- Sans-serif typography
- Rounded edges everywhere
- Welcome text "Good morning, Jay"
"""

print("Generating 2 Black variant mockup...")
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
        output_path = "/home/ubuntu/voice-agent-ui/mockups/2-black-dashboard-mockup.jpg"
        image.save(output_path)
        print(f"Image saved to: {output_path}")

print("Done generating 2 Black variant!")
