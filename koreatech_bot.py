import discord
from discord.ext import commands
import asyncio
import sys
from discord.ext.commands import Bot
import datetime
from discord.utils import get
import os
#디스코드 토큰  icon_url= 'https://newsimg.hankookilbo.com/cms/articlerelease/2016/12/06/201612061853373206_1.jpg'

if __name__ == '__main__':
  py_ver = int(f"{sys.version_info.major}{sys.version_info.minor}")
  if py_ver > 37 and sys.platform.startswith('win'):
     asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


app = commands.Bot(command_prefix='!한기대 ')
now_datetime = datetime.datetime.now()
user_list = []
user_list_ready = []
#디스코드 봇 실행 코드
@app.event
async def on_ready():
    print('다음으로 로그인 합니다.')
    print(app.user.name)
    print('connection was succesful')
    await app.change_presence(status=discord.Status.online, activity=None)

#임베드 코드
    @app.command()
    async def 도움(ctx):
        embed=discord.Embed(title = "안녕하세요! 한기대 게임 디스코드입니다!", description = "과별로 역할을 나눠서 운영하고있습니다!"
        "\n 역할배정 방에 들어가셔서 원하시는 역할을 말씀해 주시면 달아드리겠습니다"
        "\n 역할의 종류는 아래 설명을 읽어주세용", 
        color = discord.Color.blue())
        
        embed.set_author(name= "한기대봇")
        embed.add_field (name = "기본역할", value = "기본적인 역할입니다! ", inline = True)
        embed.add_field (name = "과별로 선택하시면됩니다", value = "ex)메카, 컴공, 에신화 ... ", inline = True)
        embed.add_field (name = "추가역할", value = "추가적인 역할입니다. 다셔도되고 안다셔도 상관없습니다!", inline = False)
        embed.add_field (name = "주의", value = "추가적인 역할을 다실 경우, 전체 멘션을 통해 언제든지 알람이 울릴 수 있단점을 유의해주세요! ", inline = False)
        embed.add_field (name = "역할종류", value = "솔랭, 자유랭, 내전, -메- 등등 원하는 역할이 있으시다면 말씀해주세요.", inline = False)
        embed.add_field (name = "기타 명령어들", value = "앞으로 추가할 예정입니다", inline = False)
        embed.set_footer (text = "bot version : 1.3.6")
        await ctx.send (embed=embed)

    #내전 임베드 생성

    @app.command()
    async def 내전모집(ctx):
        embed=discord.Embed(title = "내전 모집 포스팅을 시작하셨습니다!", description = "아래 🟢와 🔴를 통해 참여 여부를 표시하시면됩니다", color = discord.Color.red())
        embed.set_author(name= ctx.author.display_name, icon_url= ctx.author.avatar_url)
        embed.add_field (name = "인원 제한", value = "10명", inline = True)
        embed.add_field (name = "명령어", value = "!한기대 내전모집, 내전참가확인, 내전리스트초기화", inline = True)
        embed.set_footer (text = str(now_datetime)+ "에 생성됨")
        msg = await ctx.send (embed=embed)
        await msg.add_reaction("🟢")
        await msg.add_reaction("🔴")

    #내전 임베드 조작
    @app.event
    async def on_reaction_add(reation, user):
        if user.bot ==1:
            return None
        if str(reation.emoji) == "🟢":
            if len(user_list) >= 10:
                user_list.remove(user.name)
                user_list_ready.insert(10, user.name)
                await reation.message.channel.send(user.name+"님은 대기 인원입니다.")
            else:
                for create_list in user_list:
                    if str(user.name) in create_list:
                        user_list.remove(user.name)
                        await reation.message.channel.send(user.name +" 이미 참가하셨습니다 \n 나가시려면 🔴를 눌러주세요")
                        break
            user_list.append(user.name)
            await reation.message.channel.send("현재인원("+str(len(user_list[:10]))+"/10)")
        if str(reation.emoji) == "🔴":
            for create_list in user_list:
                if str(user.name) in create_list:
                    user_list.remove(user.name)
                    await reation.message.channel.send(user.name+"님이 신청에서 나가셨습니다. 현재인원"+"("+str(len(user_list[:10]))+"/10)")
                    break

    #내전 참가 신청확인
    @app.command()
    async def 내전참가확인(ctx):
        embed=discord.Embed(title = "내전 참가 인원입니다", description = str(now_datetime)+"기준", color = discord.Color.blue())
        embed.add_field (name = "참가", value = '%s' %user_list[:10], inline = True)
        embed.add_field (name = "현재인원", value= len(user_list[:10]), inline=False)
        embed.add_field (name = "대기", value = '%s' %user_list[10:], inline= True)
        embed.add_field (name = "대기인원", value= len(user_list[10:]), inline= False)
        await ctx.send (embed=embed)

    #내전 리스트 초기화
    @app.command()
    async def 내전리스트초기화(ctx):
        embed=discord.Embed(title = "초기화되었습니다!", description = "초기화 시간"+str(now_datetime), color = discord.Color.blurple())
        embed.add_field (name = "다시만드려면...", value = '!한기대 내전모집 을 쳐주세요', inline = True)
        user_list.clear()
        await ctx.send(embed=embed)

#자유 모집 포스팅

    #자유 모집 포스팅 만들기
    
#역할 자동 배정 안내 임베드
    @app.command()
    async def 역할안내(ctx):
        embed=discord.Embed(title = "자동 역할배정 안내입니다", description = "!을 붙인 뒤에 원하는 역할을 띄어쓰기 없이 쓰면됩니다", color = discord.Color.purple())
        embed.set_author(name= ctx.author.display_name, icon_url= ctx.author.avatar_url)
        embed.add_field (name = "현재 있는 역할", value = "13일의 금요일, 레식, 내전, 스터디, 영화, 솔랭, 자랭, 디스코드게임", inline = True)
        embed.set_footer (text = str(now_datetime)+ "에 생성됨")
        await ctx.send (embed=embed)
#역할 자동 배정 시작 
    #13일의 금요일 배정
    @app.command(name="13일의금요일", pass_context=True)
    async def _HumanRole(ctx, member: discord.Member=None):
        member = member or ctx.message.author
        await member.add_roles(get(ctx.guild.roles, name="13일의 금요일"))
        await ctx.channel.send(str(member)+"에게 13일의 금요일 역할이 적용되었습니다.")
    
    #내전 역할 배정
    @app.command(name="내전", pass_context=True)
    async def _HumanRole(ctx, member: discord.Member=None):
        member = member or ctx.message.author
        await member.add_roles(get(ctx.guild.roles, name="내전"))
        await ctx.channel.send(str(member)+"에게 내전 역할이 적용되었습니다.")

    #스터디 역할 배정
    @app.command(name="스터디", pass_context=True)
    async def _HumanRole(ctx, member: discord.Member=None):
        member = member or ctx.message.author
        await member.add_roles(get(ctx.guild.roles, name="스터디"))
        await ctx.channel.send(str(member)+"에게 스터디 역할이 적용되었습니다.")

    #영화 역할 배정
    @app.command(name="영화", pass_context=True)
    async def _HumanRole(ctx, member: discord.Member=None):
        member = member or ctx.message.author
        await member.add_roles(get(ctx.guild.roles, name="영화"))
        await ctx.channel.send(str(member)+"에게 영화 역할이 적용되었습니다.")

    #레식 역할 배정
    @app.command(name="레식", pass_context=True)
    async def _HumanRole(ctx, member: discord.Member=None):
        member = member or ctx.message.author
        await member.add_roles(get(ctx.guild.roles, name="레식"))
        await ctx.channel.send(str(member)+"에게 레식 역할이 적용되었습니다.")

    #솔랭 역할 배정
    @app.command(name="솔랭", pass_context=True)
    async def _HumanRole(ctx, member: discord.Member=None):
        member = member or ctx.message.author
        await member.add_roles(get(ctx.guild.roles, name="솔랭"))
        await ctx.channel.send(str(member)+"에게 솔랭 역할이 적용되었습니다.")
    
    #자랭 역할 배정
    @app.command(name="자랭", pass_context=True)
    async def _HumanRole(ctx, member: discord.Member=None):
        member = member or ctx.message.author
        await member.add_roles(get(ctx.guild.roles, name="자랭"))
        await ctx.channel.send(str(member)+"에게 자랭 역할이 적용되었습니다.")

    #디스코드게임 역할 배정
    @app.command(name="디스코드게임", pass_context=True)
    async def _HumanRole(ctx, member: discord.Member=None):
        member = member or ctx.message.author
        await member.add_roles(get(ctx.guild.roles, name="디스코드게임"))
        await ctx.channel.send(str(member)+"에게 디스코드게임 역할이 적용되었습니다.")
    
#크롤링 이벤트
    
#크롤링 이벤트


app.run(os.environ['token'] )