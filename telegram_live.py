from telethon import TelegramClient,events

# api e hash da generare qui:https://core.telegram.org/api/obtaining_api_id

# Inserire l'ID API di 7 caratteri.
api_id = 'xxxxxx'
# Inserire l'hash API di 32 caratteri
api_hash = 'xxxxxxxxxxxxx'
# Inserire il numero di telefono con cui sono stati creati ID e HASH.

client = TelegramClient("nome_della_sessione", api_id, api_hash)

chats = input("inderisci il nome del gruppo (nel formato t.me/xxxxx):")


@client.on(events.NewMessage(chats=chats))
async def my_event_handler(event):
    
    print("ID utente:"+str(event.message.from_id.user_id))
    print("Messaggio:"+event.message.message)

client.start()
client.run_until_disconnected()

