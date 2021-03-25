from discord_webhook import DiscordWebhook, DiscordEmbed
from datetime import datetime
from credentials import *

# Webhook Config
webhook = DiscordWebhook(url=discord_webhook_url, avatar_url="https://i.imgur.com/70bpq7H.png", username="Chase21 Logging")

def initialised(script_name):
    now = datetime.now()
    time = now.strftime("%d-%m-%Y %H:%M:%S")
    embed = DiscordEmbed(title="Initialised " + script_name, description="Initialised at " + time, color=0xFEFEFE)
    # embed.set_footer(text=version)
    embed.set_timestamp()
    # embed.add_embed_field(name="TBC", value="TBC", inline=False)
    webhook.add_embed(embed) # Add embed object to Webhook
    response = webhook.execute() # Send Webhook
    webhook.remove_embed(0) # Remove embed object

def complete(script_name, year, data):
    embed = DiscordEmbed(title="Completed script " + script_name, description="", color=0x008000)
    embed.add_embed_field(name="Year " + str(year), value=data, inline=False)
    webhook.add_embed(embed) # Add embed object to Webhook
    webhook.execute() # Send Webhook
    webhook.remove_embed(0) # Remove embed object

def report():
    embed = DiscordEmbed(title="TITLE", description="description", color=0xFFFFFF)
    embed.set_timestamp()
    embed.add_embed_field()
    webhook.add_embed(embed) # Add embed object to Webhook
    response = webhook.execute() # Send Webhook
    webhook.remove_embed(0) # Remove embed object

def invalidFormResponse(year, data):
    embed = DiscordEmbed(title="Invalid Form Responses", color=0xFFA500)
    embed.set_timestamp()
    embed.add_embed_field(name="Year " + str(year), value=data, inline=False)
    webhook.add_embed(embed) # Add embed object to Webhook
    webhook.execute() # Send Webhook
    webhook.remove_embed(0) # Remove embed object

if __name__ == "__main__":
    complete("Example Script", "9", "testdata\nline2")
