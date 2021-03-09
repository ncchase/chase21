from discord_webhook import DiscordWebhook, DiscordEmbed
import datetime

# Webhook Config
webhook = DiscordWebhook(url=discord_webhook_url, avatar_url="https://i.imgur.com/TBC.png", username="NC Chase Logging")

def initialised(script):
    now = datetime.now()
    time = now.strftime("%d-%m-%Y %H:%M:%S")
    embed = DiscordEmbed(title="Initialised " + script, description="Initialised at " + time, color=0xFEFEFE)
    # embed.set_footer(text=version)
    # embed.set_timestamp()
    embed.add_embed_field(name="Tracking ", value="TBC", inline=False)
    webhook.add_embed(embed) # Add embed object to webhook
    response = webhook.execute() # Send Webhook
    webhook.remove_embed(0)

def report():
    embed = DiscordEmbed(title="TITLE", description="description", color="", )
    embed.set_timestamp



