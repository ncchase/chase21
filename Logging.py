from discord_webhook import DiscordWebhook, DiscordEmbed

# Webhook Config
webhook = DiscordWebhook(url=discord_webhook_url, avatar_url="https://i.imgur.com/IpIG5TP.png", username="Instagram Statistics Tracker")

embed = DiscordEmbed(title="Initialised", description="Initialised at " + init_time_with_day, color=0xFEFEFE)
embed.set_footer(text=version)
embed.add_embed_field(name="Tracking ", value=scrape_username, inline=False)
webhook.add_embed(embed) # Add embed object to webhook
response = webhook.execute() # Send Webhook
webhook.remove_embed(0)