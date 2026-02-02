#!/usr/bin/env python3
"""Generate Brand Dashboard mockup using Gemini API (Nano Banana Pro)"""

import os
from google import genai
from google.genai import types

API_KEY = "AIzaSyBtjuQoQXf8hq7UGCEcGt4ya1ZRsWzssw4"

client = genai.Client(api_key=API_KEY)

prompt = """Generate a high-fidelity UI mockup for a Voice AI Agent SaaS Agency Dashboard with GLASSMORPHISM design.

EXACT SPECIFICATIONS:

**Style:** Black/White/Gold chic boutique glassmorphism - elegant, premium, sophisticated
**Format:** Desktop dashboard screenshot, 1440px width, high resolution

**Colors (EXACT HEX VALUES):**
- Primary accent: #D4AF37 (Gold) for CTAs, accents, focus states, active nav items
- Background: #0D0D0D (Near black) as the base
- Card backgrounds: Semi-transparent dark gray with frosted glass blur effect
- Card borders: Subtle gold tint glow
- Headlines: #FFFFFF (Pure white)
- Body text: #F5F5F5 (Light gray)
- Icons: Gold or white

**Typography:**
- Font style: Clean sans-serif (like Inter)
- Headlines: Bold weight
- Body: Regular weight
- All text crisp and legible

**Layout - Dashboard with sidebar:**
LEFT SIDEBAR (vertical, dark frosted glass):
- App logo at top "Kyber" with gold accent
- Navigation items with icons:
  - Overview (dashboard icon) - ACTIVE with gold highlight
  - Clients (users icon)
  - Interviews (microphone icon)
  - Knowledge Base (book icon)
  - Export Hub (download icon)
  - Settings (gear icon)
- User profile section at bottom

TOP HEADER:
- Breadcrumb: "Dashboard > Overview"
- Search bar with placeholder "Search & Ask..."
- Dropdown menu button visible
- Notification bell icon
- User avatar

MAIN CONTENT AREA (showing Overview):
- Welcome message: "Good morning, Jay"
- Row of 4 metric cards (frosted glass, gold accents):
  - "Recent Interviews" showing "24" with up arrow
  - "Pending Clients" showing "8"
  - "Avg Quality Score" showing "8.7/10" with gold stars
  - "Completion Rate" showing "94%" with progress ring
- Below: "Recent Activity" section with list items
- "Quick Actions" panel with gold-outlined buttons

**Glassmorphism effects:**
- All cards: frosted glass effect with blur
- Subtle gold border glow on cards
- Border-radius: Very rounded corners (24px) on all cards
- Depth with subtle shadows
- Semi-transparent overlays

**Overall feel:**
- Premium, luxurious, boutique aesthetic
- Clean and minimal, NOT cluttered
- Sophisticated black and gold color scheme
- Modern SaaS dashboard design
- Professional but elegant"""

print("Generating Brand Dashboard mockup (Kyber) with gemini-3-pro-image-preview...")

try:
    response = client.models.generate_content(
        model="gemini-3-pro-image-preview",
        contents=[prompt],
        config=types.GenerateContentConfig(
            response_modalities=['TEXT', 'IMAGE'],
            image_config=types.ImageConfig(
                aspect_ratio="16:9",
                image_size="2K"
            ),
        )
    )

    for part in response.parts:
        if part.text:
            print(f"Response text: {part.text}")
        elif part.inline_data:
            image = part.as_image()
            output_path = "/home/ubuntu/voice-agent-ui/mockups/brand-dashboard-mockup.jpg"
            image.save(output_path)
            print(f"✅ Brand Dashboard mockup saved to: {output_path}")

except Exception as e:
    print(f"Error with gemini-3-pro-image-preview: {e}")
