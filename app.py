from Lina import Lina

bot = Lina()
bot.load_directory("./brain")
bot.sort_replies()

while True:
    msg = input('You> ')
    if msg == '/quit':
        break

    reply = bot.reply("localuser", msg)
    print('Bot>', reply)
