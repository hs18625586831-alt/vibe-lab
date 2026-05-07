#!/usr/bin/env python3
"""
Idea Collector Script
Usage: python3 scripts/collect_idea.py "Idea Title" "URL" "Summary" "#tags"
"""
import sys
import os
from datetime import datetime

IDEAS_DIR = os.path.join(os.path.dirname(__file__), "..", "ideas")

def main():
    if len(sys.argv) < 4:
        print("Usage: collect_idea.py <title> <url> <summary> [--tags tag1,tag2]")
        sys.exit(1)

    title = sys.argv[1]
    url = sys.argv[2]
    summary = sys.argv[3]
    tags = sys.argv[4] if len(sys.argv) > 4 else "#inspiration"
    
    today = datetime.now().strftime("%Y-%m-%d")
    file_path = os.path.join(IDEAS_DIR, f"{today}.md")

    # Ensure directory exists
    os.makedirs(IDEAS_DIR, exist_ok=True)

    # Append content
    with open(file_path, "a", encoding="utf-8") as f:
        # Add horizontal rule if file is not empty
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            f.write("\n---\n\n")
        
        f.write(f"## {title}\n")
        f.write(f"- **Source**: [Link]({url})\n")
        f.write(f"- **Summary**: {summary}\n")
        f.write(f"- **Tags**: {tags}\n")
        f.write(f"- **Collected At**: {datetime.now().strftime('%H:%M')}\n")

    print(f"✅ Idea collected: {title}")
    print(f"📁 Saved to: {file_path}")

if __name__ == "__main__":
    main()
