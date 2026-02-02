#!/usr/bin/env python3
"""Generate 3 Black variant mockup with compact sidebar layout"""
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

**VARIANT 3 LAYOUT - Compact icon sidebar:**
- THIN ICON-ONLY SIDEBAR on left (60px wide) with icons for: Overview, Clients, Interviews, Knowledge Base, Export Hub, Settings
- Small "K" logo icon at top of sidebar
- Sidebar icons are gold colored, active icon highlighted

**Header area (top of main content):**
- Full search bar spanning most of header width with "Search & Ask" placeholder
- Notifications bell icon
- User avatar with dropdown
- "Kyber" text logo next to search

**Main content - Bento Grid Layout:**
- Large "Recent Interviews: 24" card taking 2 columns with mini chart
- "Pending Clients: 8" card with progress bar
- "Avg Quality Score: 8.7/10" card with star rating
- "Completion Rate: 94%" card with circular progress ring
- "Recent Activity" card spanning 2 columns showing latest 4 items
- "Quick Actions" card with 4 action buttons in a 2x2 grid

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
- Icon sidebar also has glass effect

**Must include:**
- "K" logo icon in sidebar (keep same logo style)
- "Kyber" text in header
- Search bar with "Search & Ask" placeholder
- Bento-style grid layout
- Clean, minimal, not cluttered
- Sans-serif typography
- Rounded edges everywhere
- Welcome text "Good morning, Jay"
"""

print("Generating 3 Black variant mockup...")
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
        output_path = "/home/ubuntu/voice-agent-ui/mockups/3-black-dashboard-mockup.jpg"
        image.save(output_path)
        print(f"Image saved to: {output_path}")

print("Done generating 3 Black variant!")
