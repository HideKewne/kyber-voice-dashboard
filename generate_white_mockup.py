#!/usr/bin/env python3
"""Generate White Dashboard mockup using Gemini API"""

import os
from google import genai
from google.genai import types

API_KEY = "AIzaSyBtjuQoQXf8hq7UGCEcGt4ya1ZRsWzssw4"

client = genai.Client(api_key=API_KEY)

prompt = """Generate a high-fidelity UI mockup for a Voice AI Agent SaaS Agency Dashboard with CLEAN WHITE GLASSMORPHISM design.

EXACT SPECIFICATIONS:

**Style:** Clean white glassmorphism - modern, minimal, airy, light
**Format:** Desktop dashboard screenshot, 1440px width, high resolution

**Colors (EXACT HEX VALUES):**
- Primary accent: #3B82F6 (Blue) for CTAs, links, active states
- Primary hover: #2563EB (Darker blue)
- Light accent: #60A5FA (Light blue for subtle highlights)
- Page background: #FAFAFA (Off-white)
- Card backgrounds: rgba(255, 255, 255, 0.7) with frosted glass blur effect
- Card borders: 1px solid rgba(255, 255, 255, 0.5)
- Card shadows: Soft shadow 0 8px 32px rgba(0, 0, 0, 0.08)
- Headlines: #18181B (Near black)
- Body text: #52525B (Gray)
- Borders/dividers: #E4E4E7 (Light gray)

**Typography:**
- Font style: Clean sans-serif (like Inter)
- Headlines: Bold weight, dark gray #18181B
- Body: Regular weight, medium gray #52525B
- All text crisp and legible

**Layout - Dashboard with sidebar:**
LEFT SIDEBAR (vertical, white frosted glass):
- App logo at top "Kyber" with blue accent
- Navigation items with icons:
  - Overview (dashboard icon) - ACTIVE with blue highlight
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
- Row of 4 metric cards (white frosted glass, blue accents):
  - "Recent Interviews" showing "24" with up arrow
  - "Pending Clients" showing "8"
  - "Avg Quality Score" showing "8.7/10" with blue stars
  - "Completion Rate" showing "94%" with circular progress
- Below: "Recent Activity" section with list items
- "Quick Actions" panel with blue-outlined buttons

**Glassmorphism effects:**
- All cards: white frosted glass effect with subtle blur
- Soft shadows for depth
- Border-radius: Very rounded corners (24px) on all cards
- Light, airy feel
- Semi-transparent white overlays

**Overall feel:**
- Clean, minimal, modern
- Bright and airy white aesthetic
- Blue accents for interactivity
- Professional SaaS dashboard
- NOT cluttered - spacious and breathable"""

print("Generating White Dashboard mockup (Kyber) with gemini-3-pro-image-preview...")

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
            output_path = "/home/ubuntu/voice-agent-ui/mockups/white-dashboard-mockup.jpg"
            image.save(output_path)
            print(f"✅ White Dashboard mockup saved to: {output_path}")

except Exception as e:
    print(f"Error: {e}")
