import discord
from discord.ext import commands

# Enable intents
intents = discord.Intents.default()
intents.message_content = True  # This is required to read message content

# Create the bot with the specified intents
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is ready. Logged in as {bot.user}")

@bot.command()
async def setup(ctx):
    guild = ctx.guild

    # Category and channels mapping with emojis
    categories = {
        "🏫 Welcome": ["👋│welcome", "📜│rules", "📢│announcements", "🔍│faq", "🆘│helpdesk"],
        "📚 Spring Semester": [
            "✍️│ENG-101", "➗│MAT-101", "🌌│PHY-101", 
            "🖥️│CSE-112", "💡│CSE-113", "🧪│CSE-114", 
            "🧬│CSE-115", "📖│lecture-notes", "📝│assignments", 
            "📊│resources", "💻│coding-help", "🎓│exam-prep"
        ],
        "📰 Campus News": ["🎙️│seminars", "📆│events", "🏆│achievements", "🌱│opportunities", "📢│notices"],
        "🎤 Voice Chats": ["🗣️│general-talk", "📖│study-group", "🎮│gaming-room", "🛠️│project-discussions"],
        "🤖 ECA": [
            "🧩│competitive-programming", "🤖│robotics", "💻│hackathons", 
            "🎨│design-club", "📸│photography", "🏃│sports", 
            "🎭│arts-club", "🎤│debates"
        ],
        "💬 General Talk": ["🌍│chitchat", "📸│media-sharing", "📬│suggestions", "🌟│introductions"],
        "🎭 Entertainment": [
            "🎶│music", "🎥│movies", "🖤│dark-memes", 
            "🎮│game-night", "📺│anime", "😂│fun-memes"
        ],
        "💡 Research & Innovation": [
            "🔬│research-papers", "🤔│brainstorming", "🛠️│projects", 
            "📡│AI-ML", "📱│hardware-lab", "💼│startup-zone"
        ],
        "🌟 Community": ["🤝│mentorship", "🌏│alumni", "🏗️│collaborations", "📚│career-tips"]
    }

    # Create categories and channels
    for category_name, channels in categories.items():
        category = await guild.create_category(category_name)
        for channel_name in channels:
            if "voice" in category_name.lower():
                await guild.create_voice_channel(channel_name, category=category)
            else:
                await guild.create_text_channel(channel_name, category=category)
    
    await ctx.send("Server setup is complete with emojis!")

# Run the bot with your token
bot.run("YOUR_BOT_TOKEN")
