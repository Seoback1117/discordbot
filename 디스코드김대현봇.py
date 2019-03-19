import discord
import asyncio
import random
import datetime
import os


client = discord.Client()



@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("------------------")
    await client.change_presence(game=discord.Game(name= '임타 옷 벗기기 게임', type=1))


@client.event
async def on_message(message):
        if message.content.startswith('!대현아 안녕'):
            await client.send_message(message.channel,"안뇽")

        if message.content.startswith('!대현아주사위'):
            roll = message.content.split(" ")
            rolld = roll[1].split("d")
            dice = 0
            for i in range(1, int(rolld[0])+1):
                dice = dice + random.randint(1, int(rolld[1]))
            await client.send_message(message.channel, str(dice))

        if message.content.startswith('!대현아 골라'):
            choice = message.content.split(" ")
            choicenumber = random.randint(1, len(choice)-1)
            choiceresult = choice[choicenumber]
            await client.send_message(message.channel, choiceresult)

        if message.content.startswith('!대현아 뭐 먹을까'):
            food = "짜장면 짬뽕 라면 고기 똥 햄버거 임타 오승록 햄버거 보쌈 치킨 피자 오줌 너 나 닥쳐"
            foodchoice = food.split(" ")
            foodnumber = random.randint(1, len(foodchoice))
            foodresult = foodchoice[foodnumber-1]
            await client.send_message(message.channel, foodresult)

        if message.content.startswith('!대현아 사다리타기'):
            team = message.content[11:]
            peopleteam = team.split("/")
            people = peopleteam[0]
            team = peopleteam[1]
            person = people.split(" ")
            teamname = team.split(" ")
            random.shuffle(teamname)
            for i in range(0, len(person)):
                await client.send_message(message.channel, person[i] + '=' + teamname[i])

        if message.content.startswith('!대현아 너도 강화해봐'):
            await client.send_message(message.channel, "!강화 김대현")

        if message.content.startswith('!대현아 뭐해'):
            answer = "똥싸 밥먹어 DDR 춤추고있다 숙제중 롤 배그 피파 카트 임타먹는중 달리는중 학원임 채팅중"
            answerchoice = answer.split(" ")
            answernumber = random.randint(1, len(answerchoice))
            answerresult = answerchoice[answernumber-1]
            await client.send_message(message.channel, answerresult)

        if message.content.startswith('!대현아 시발'):
            await client.send_message(message.channel, "뭐 이 시발노무색기야")

        if message.content.startswith('!대현아 일베'):
            await client.send_message(message.channel, "이기 참 딱딱하니 딱 좋노")

        if message.content.startswith('!대현아 야동'):
            await client.send_message(message.channel, "하하 야동은 이 채널이지 https://discord.gg/TY4YpN")

        if message.content.startswith("!대현아 서버"):
            list = []
            for server in client.servers:
                list.append(server.name)
            await client.send_message(message.channel, "\n".join(list))

        if message.content.startswith("!대현아 시간"):
            a = datetime.datetime.today().year
            b = datetime.datetime.today().month
            c = datetime.datetime.today().day
            d = datetime.datetime.today().hour
            e = datetime.datetime.today().minute
            f = datetime.datetime.today().second
            await client.send_message(message.channel,"```" + str(a) + "년 " + str(b) + "월 " + str(c) + "일 " + str(d) + "시 " + str(e) + "분 " + str(f) + "초이걸랑요~~```")

        if message.content.startswith('!대현아 섹스'):
            await client.send_message(message.channel, "ㄱㄱ?")

        if message.content.startswith('!대현아 서백'):
            await client.send_message(message.channel,"구독 ㄱㄱ https://youtu.be/GprGgC_S0us")

        if message.content.startswith('!대현아 김동우'):
            await client.send_message(message.channel, "저는 멍청한 동우가 아닙니다.")

        if message.content.startswith('!대현아 유튜브'):
            await client.send_message(message.channel, "https://www.youtube.com/")

        if message.content.startswith('!대현아 네이버'):
            await client.send_message(message.channel, "https://www.naver.com/")

access_token = os.environ["BOT TOKEN"]
client.run(access_token)
