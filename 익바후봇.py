import asyncio
import discord

client = discord.Client()

# 1-6에서 생성된 토큰을 이곳에 입력해주세요.
token = "530321664827719680"

# 봇이 구동되었을 때 동작되는 코드입니다.
@client.event
async def on_ready():
    print("Logged in as ") #화면에 봇의 아이디, 닉네임이 출력됩니다.
    print(client.user.name)
    print(client.user.id)
    print("===========")
    # 디스코드에는 현재 본인이 어떤 게임을 플레이하는지 보여주는 기능이 있습니다.
    # 이 기능을 사용하여 봇의 상태를 간단하게 출력해줄 수 있습니다.
    await client.change_presence(game=discord.Game(name="익후는 괴롭혀야 제맛!", type=1))

# 봇이 새로운 메시지를 수신했을때 동작되는 코드입니다.
@client.event
async def on_message(message):
    if message.author.bot: #만약 메시지를 보낸사람이 봇일 경우에는
        return None #동작하지 않고 무시합니다.

    id = message.author.id #id라는 변수에는 메시지를 보낸사람의 ID를 담습니다.
    channel = message.channel #channel이라는 변수에는 메시지를 받은 채널의 ID를 담습니다.

    if message.content.startswith('!익바후보'): #만약 해당 메시지가 '!커맨드' 로 시작하는 경우에는
        await client.send_message(channel, '맞습니다. 익바후보! 우후~') #봇은 해당 채널에 '커맨드' 라고 말합니다.

    if message.content.startswith('!익멍후청'): #만약 해당 메시지가 '!커맨드' 로 시작하는 경우에는
        await client.send_message(channel, '맞습니다. 익멍후청! 오예~') #봇은 해당 채널에 '커맨드' 라고 말합니다.

    if message.content.startswith('!나이'): #만약 해당 메시지가 '!커맨드' 로 시작하는 경우에는
        await client.send_message(channel, '아무튼 늙었습니다. 와 늙쿠!') #봇은 해당 채널에 '커맨드' 라고 말합니다.

    if message.content.startswith('!키'): #만약 해당 메시지가 '!커맨드' 로 시작하는 경우에는
        await client.send_message(channel, '머리 어깨 무릎 발까지 154!') #봇은 해당 채널에 '커맨드' 라고 말합니다.



client.run(token)