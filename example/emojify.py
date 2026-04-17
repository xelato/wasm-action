#!/usr/bin/env python3
"""
Write a Python program that continuously monitors a specific test file for changes (use polling) and when changed adds an emoji character to a matching word.

File Monitor - Continuously monitors a file and adds emojis to matching words
Includes a comprehensive emoji dictionary for automatic matching
"""

import os
import time
import re
import sys
from pathlib import Path


# Large static emoji dictionary mapping words to emojis
EMOJI_DICT = {
    # Programming & Technology
    "python": "🐍",
    "javascript": "⚡",
    "java": "☕",
    "code": "💻",
    "coding": "💻",
    "program": "🖥️",
    "programming": "🖥️",
    "developer": "👨‍💻",
    "software": "💿",
    "hardware": "🔧",
    "computer": "💻",
    "laptop": "💻",
    "data": "📊",
    "database": "🗄️",
    "server": "🖥️",
    "cloud": "☁️",
    "api": "🔌",
    "bug": "🐛",
    "debug": "🔍",
    "git": "🌿",
    "github": "🐙",
    "docker": "🐳",
    "linux": "🐧",
    "windows": "🪟",
    "mac": "🍎",
    "android": "🤖",
    "ios": "📱",
    "app": "📱",
    "website": "🌐",
    "web": "🕸️",
    "internet": "🌐",
    "wifi": "📶",
    "network": "🔗",
    "security": "🔒",
    "password": "🔑",
    "encrypt": "🔐",
    "hack": "🔓",
    "ai": "🤖",
    "robot": "🤖",
    "machine": "⚙️",
    
    # Emotions & Reactions
    "happy": "😊",
    "sad": "😢",
    "love": "❤️",
    "angry": "😠",
    "excited": "🎉",
    "joy": "😄",
    "smile": "😊",
    "laugh": "😂",
    "cry": "😭",
    "cool": "😎",
    "awesome": "🤩",
    "amazing": "✨",
    "great": "👍",
    "good": "👌",
    "bad": "👎",
    "wow": "😮",
    "omg": "😱",
    "fun": "🎊",
    "party": "🎉",
    "celebrate": "🎊",
    
    # Nature & Animals
    "dog": "🐕",
    "cat": "🐱",
    "bird": "🐦",
    "fish": "🐠",
    "snake": "🐍",
    "lion": "🦁",
    "tiger": "🐯",
    "bear": "🐻",
    "panda": "🐼",
    "monkey": "🐵",
    "elephant": "🐘",
    "rabbit": "🐰",
    "fox": "🦊",
    "wolf": "🐺",
    "horse": "🐴",
    "cow": "🐮",
    "pig": "🐷",
    "chicken": "🐔",
    "bee": "🐝",
    "butterfly": "🦋",
    "tree": "🌳",
    "flower": "🌸",
    "rose": "🌹",
    "plant": "🌱",
    "sun": "☀️",
    "moon": "🌙",
    "star": "⭐",
    "rain": "🌧️",
    "snow": "❄️",
    "fire": "🔥",
    "water": "💧",
    "ocean": "🌊",
    "mountain": "⛰️",
    "beach": "🏖️",
    
    # Food & Drink
    "pizza": "🍕",
    "burger": "🍔",
    "fries": "🍟",
    "hotdog": "🌭",
    "taco": "🌮",
    "corn": "🌽",
    "sushi": "🍣",
    "ramen": "🍜",
    "pasta": "🍝",
    "bread": "🍞",
    "cheese": "🧀",
    "cherry": "🍒",
    "egg": "🥚",
    "bacon": "🥓",
    "steak": "🥩",
    "salad": "🥗",
    "carrot": "🥕",
    "potato": "🥔",
    "onion": "🧅",
    "fruit": "🍎",
    "apple": "🍎",
    "banana": "🍌",
    "orange": "🍊",
    "lemon": "🍋",
    "strawberry": "🍓",
    "grape": "🍇",
    "watermelon": "🍉",
    "cake": "🎂",
    "cookie": "🍪",
    "chocolate": "🍫",
    "candy": "🍬",
    "icecream": "🍦",
    "lollipop": "🍭",
    "honey": "🍯",
    "donut": "🍩",
    "coffee": "☕",
    "tea": "🍵",
    "beer": "🍺",
    "wine": "🍷",
    "cocktail": "🍹",
    "milk": "🥛",
    "juice": "🧃",
    
    # Activities & Sports
    "soccer": "⚽",
    "football": "🏈",
    "basketball": "🏀",
    "baseball": "⚾",
    "tennis": "🎾",
    "golf": "⛳",
    "swimming": "🏊",
    "running": "🏃",
    "cycling": "🚴",
    "gym": "💪",
    "fitness": "🏋️",
    "yoga": "🧘",
    "music": "🎵",
    "guitar": "🎸",
    "piano": "🎹",
    "dance": "💃",
    "art": "🎨",
    "paint": "🖌️",
    "draw": "✏️",
    "read": "📖",
    "book": "📚",
    "write": "✍️",
    "movie": "🎬",
    "camera": "📷",
    "photo": "📸",
    "game": "🎮",
    "gaming": "🎮",
    
    # Travel & Places
    "travel": "✈️",
    "plane": "✈️",
    "car": "🚗",
    "bus": "🚌",
    "train": "🚂",
    "bike": "🚲",
    "ship": "🚢",
    "rocket": "🚀",
    "home": "🏠",
    "house": "🏡",
    "building": "🏢",
    "hotel": "🏨",
    "school": "🏫",
    "hospital": "🏥",
    "bank": "🏦",
    "church": "⛪",
    "castle": "🏰",
    "city": "🌃",
    "town": "🏘️",
    "map": "🗺️",
    "compass": "🧭",
    
    # Objects & Symbols
    "phone": "📱",
    "email": "📧",
    "message": "💬",
    "letter": "✉️",
    "gift": "🎁",
    "balloon": "🎈",
    "trophy": "🏆",
    "medal": "🥇",
    "crown": "👑",
    "money": "💰",
    "dollar": "💵",
    "coin": "🪙",
    "gem": "💎",
    "ring": "💍",
    "watch": "⌚",
    "key": "🔑",
    "lock": "🔒",
    "bell": "🔔",
    "light": "💡",
    "bulb": "💡",
    "battery": "🔋",
    "magnet": "🧲",
    "tool": "🔧",
    "hammer": "🔨",
    "wrench": "🔧",
    "scissors": "✂️",
    "umbrella": "☂️",
    "glasses": "👓",
    "hat": "🎩",
    "shirt": "👕",
    "shoe": "👟",
    
    # Time & Weather
    "time": "⏰",
    "clock": "🕐",
    "calendar": "📅",
    "today": "📆",
    "yesterday": "📆",
    "tomorrow": "📆",
    "morning": "🌅",
    "night": "🌃",
    "day": "☀️",
    "evening": "🌆",
    "spring": "🌸",
    "summer": "☀️",
    "autumn": "🍂",
    "fall": "🍁",
    "winter": "❄️",
    
    # Work & Business
    "work": "💼",
    "office": "🏢",
    "business": "💼",
    "meeting": "🤝",
    "presentation": "📊",
    "chart": "📈",
    "growth": "📈",
    "success": "🎯",
    "target": "🎯",
    "goal": "🎯",
    "project": "📋",
    "task": "✅",
    "todo": "📝",
    "done": "✅",
    "complete": "✔️",
    "start": "▶️",
    "stop": "⏹️",
    "pause": "⏸️",
    
    # Health & Medical
    "doctor": "👨‍⚕️",
    "nurse": "👩‍⚕️",
    "medicine": "💊",
    "pill": "💊",
    "vaccine": "💉",
    "health": "🏥",
    "heart": "❤️",
    "brain": "🧠",
    "muscle": "💪",
    "bone": "🦴",
    
    # Education & Science
    "study": "📖",
    "learn": "📚",
    "teach": "👨‍🏫",
    "student": "🎓",
    "graduate": "🎓",
    "test": "📝",
    "exam": "📄",
    "science": "🔬",
    "lab": "🧪",
    "experiment": "🧬",
    "chemistry": "⚗️",
    "biology": "🧬",
    "physics": "⚛️",
    "math": "🔢",
    "calculate": "🧮",
    
    # Misc
    "yes": "✅",
    "no": "❌",
    "check": "✓",
    "cross": "✗",
    "warning": "⚠️",
    "alert": "🚨",
    "danger": "⚡",
    "safe": "✅",
    "new": "🆕",
    "hot": "🔥",
    "trending": "📈",
    "popular": "⭐",
    "best": "🏆",
    "top": "🔝",
    "important": "❗",
    "urgent": "🚨",
    "please": "🙏",
    "thanks": "🙏",
    "thank": "🙏",
    "help": "🆘",
    "question": "❓",
    "answer": "💡",
    "idea": "💡",
    "think": "🤔",
    "remember": "💭",
    "forget": "🤷",
    "know": "🧠",
    "fast": "⚡",
    "slow": "🐌",
    "big": "🔴",
    "small": "🔵",
    "strong": "💪",
    "weak": "😓",
    "win": "🏆",
    "lose": "😔",
    "first": "🥇",
    "second": "🥈",
    "third": "🥉",
}


class FileMonitor:
    def __init__(self, filepath, emoji_dict=None, poll_interval=1.0):
        """
        Initialize the file monitor.
        
        Args:
            filepath: Path to the file to monitor
            emoji_dict: Dictionary mapping words to emojis (uses EMOJI_DICT if None)
            poll_interval: How often to check for changes (seconds)
        """
        self.filepath = Path(filepath)
        self.emoji_dict = emoji_dict if emoji_dict is not None else EMOJI_DICT
        self.poll_interval = poll_interval
        self.last_modified = None
        
    def get_file_mtime(self):
        """Get the last modification time of the file."""
        try:
            return os.path.getmtime(self.filepath)
        except FileNotFoundError:
            return None
    
    def add_emojis_to_content(self, content):
        """Add emojis to all matching words in the content."""
        modified_content = content
        changes_made = []
        
        # Process each word in the emoji dictionary
        for word, emoji in self.emoji_dict.items():
            # Only add emoji if word exists
            if word in modified_content.lower():
                # Case-insensitive word boundary search
                pattern = re.compile(r'\b' + re.escape(word) + r'\b', re.IGNORECASE)
                matches = pattern.findall(modified_content)
                
                if matches:
                    # Replace each match with itself + emoji
                    def replacer(match):
                        matched_text = match.group(0)
                        # Check if emoji already follows
                        end_pos = match.end()
                        if end_pos < len(modified_content) and modified_content[end_pos:end_pos+len(emoji)] == emoji:
                            return matched_text
                        return matched_text + emoji
                    
                    new_content = pattern.sub(replacer, modified_content)
                    
                    if new_content != modified_content:
                        changes_made.append(f"{word} → {word}{emoji} ({len(matches)} occurrences)")
                        modified_content = new_content
        
        return modified_content, changes_made
    
    def process_file(self):
        """Read file, add emojis to matching words, and write back."""
        try:
            # Read the file
            with open(self.filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Add emojis to content
            modified_content, changes = self.add_emojis_to_content(content)
            
            # Only write if something changed
            if modified_content != content:
                with open(self.filepath, 'w', encoding='utf-8') as f:
                    f.write(modified_content)
                
                print(f"✓ Modified {self.filepath}")
                for change in changes:
                    print(f"  • {change}")
                return True
            
            return False
            
        except Exception as e:
            print(f"Error processing file: {e}")
            return False
    
    def start_monitoring(self):
        """Start monitoring the file for changes."""
        print(f"🔍 File Monitor with Emoji Dictionary")
        print(f"=" * 60)
        print(f"  File: {self.filepath}")
        print(f"  Emoji dictionary: {len(self.emoji_dict)} words")
        print(f"  Poll interval: {self.poll_interval}s")
        print(f"=" * 60)
        print(f"\n👀 Watching for changes... (Press Ctrl+C to stop)\n")
        
        # Initialize last modified time
        self.last_modified = self.get_file_mtime()
        
        if self.last_modified is None:
            print(f"⚠️  File '{self.filepath}' not found. Waiting for it to be created...")
        
        try:
            while True:
                current_mtime = self.get_file_mtime()
                
                # Check if file was created or modified
                if current_mtime is not None and current_mtime != self.last_modified:
                    timestamp = time.strftime('%H:%M:%S')
                    print(f"\n[{timestamp}] 🔔 Change detected!")
                    
                    # Small delay to ensure write is complete
                    time.sleep(0.1)
                    
                    # Process the file
                    self.process_file()
                    
                    # Update last modified time after our changes
                    self.last_modified = self.get_file_mtime()
                    print()
                
                time.sleep(self.poll_interval)
                
        except KeyboardInterrupt:
            print("\n\n⏹️  Monitoring stopped by user.")


def main():
    """Main function."""
    # Configuration
    if len(sys.argv) < 2:
        print("no file specified for monitoring")
    FILE_TO_MONITOR = sys.argv[1]
    POLL_INTERVAL = 1.0  # Check every second
    
    print(f"\n📚 Loaded {len(EMOJI_DICT)} emoji mappings")
    print(f"Sample mappings: python→{EMOJI_DICT['python']}, "
          f"happy→{EMOJI_DICT['happy']}, "
          f"fire→{EMOJI_DICT['fire']}\n")
    
    # Create monitor instance
    monitor = FileMonitor(
        filepath=FILE_TO_MONITOR,
        emoji_dict=EMOJI_DICT,
        poll_interval=POLL_INTERVAL
    )
    
    # Start monitoring
    monitor.start_monitoring()


if __name__ == "__main__":
    main()
