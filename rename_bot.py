from pyrogram import Client, filters

# ------------------- CONFIG -------------------
api_id = 27484185
api_hash = "7a52fad60fd16e779bb2324778e5d8da"
bot_token = "8428438458:AAEJbPiZTybx4f5xBgY_fUjJj9yVe1Nz4SM"

# ------------------- BOT INIT -------------------
app = Client("rename_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# ------------------- HANDLER -------------------
@app.on_message(filters.channel & filters.caption & filters.regex(r"TvShowHub\.mp4"))
async def rename_tvshow(client, message):
    try:
        old_caption = message.caption
        new_caption = old_caption.replace("TvShowHub", "MRxVoltz")
        await client.edit_message_caption(
            chat_id=message.chat.id,
            message_id=message.id,
            caption=new_caption
        )
        print(f"✅ Caption updated: {new_caption}")
    except Exception as e:
        print(f"❌ Failed to edit caption: {e}")

# ------------------- RUN BOT -------------------
print("🤖 Bot is running...")
app.run()
