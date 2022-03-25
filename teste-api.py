from telethon import TelegramClient, events
#contadorGreen = 0
#contadorRed = 0
api_id = 11396179
api_hash = 'fe079b1f5105bb1ffee859329873ce0a'


client = TelegramClient('anon', api_id, api_hash)


@client.on(events.NewMessage)
async def handler(event):
    chat_id = event.chat_id
    if chat_id == -1001727231060:
        msg = event.raw_text
        await client.send_message(-640513185,msg)
        if "GREEN" in msg:
            print("GREEN")
        elif "LOSS" in msg:
            print("LOSS")
        #print("RED: {} \n GREEN: {}".format(contadorRed,contadorGreen))
    #print("{} {}".format(chat_id,msg))


#-647711835 - GRUPO TESTE 2 SÓ COM ALINE
#640513185 - GRUPO CRIADO VIP TESTE
#1001727231060 - GRUPO OFICIAL ROLETA
#-1001273131752 - GRUPO DAS CONSULTAS
#5136509506 - GRUPO BOT TESTE
client.start()
client.run_until_disconnected()