import discord
from discord.ext import commands
import asyncio
import sys
from discord.ext.commands import Bot
import datetime
import os
from discord.utils import get
import random
#디스코드 토큰  icon_url= 'https://newsimg.hankookilbo.com/cms/articlerelease/2016/12/06/201612061853373206_1.jpg'

if __name__ == '__main__':
  py_ver = int(f"{sys.version_info.major}{sys.version_info.minor}")
  if py_ver > 37 and sys.platform.startswith('win'):
     asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

#변수
app = commands.Bot(command_prefix='!한기대 ')
now_datetime = datetime.datetime.now()
user_list = []
team_list = ["1팀","2팀","3팀","4팀"]
user_list_alter = []
i =1

#디스코드 봇 실행 코드
@app.event
async def on_ready():
    print('다음으로 로그인 합니다.')
    print(app.user.name)
    print('connection was succesful')
    await app.change_presence(status=discord.Game(name="!한기대 도움"), activity=None)

#롤 내전 모집
    @app.command()
    async def 롤내전모집시작(ctx,*,time_set):
        mention_code = discord.utils.get(ctx.guild.roles, id = 808760114999722014)
        embed=discord.Embed(title = "롤 내전 모집 포스팅을 시작하셨습니다!", description = f"시작시간 {time_set}", color = discord.Color.random())
        embed.set_author(name= ctx.author.display_name, icon_url= ctx.author.avatar_url)
        embed.add_field (name = "현재 인원", value = user_list, inline = False)
        embed.add_field (name = "미확정 인원", value = user_list_alter, inline = False)
        embed.add_field (name = "모집이 끝난후...", value = "반드시 ❌를 눌러 모집을 종료해주세요", inline = False)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/840823850651877387/840823990360211477/league-of-legends.png")
        embed.set_footer (text = str(now_datetime)+ "에 생성됨")
        msg = await ctx.send (embed=embed)
        await msg.add_reaction("🟩")
        await msg.add_reaction("🟥")
        await msg.add_reaction("🟨")
        await msg.add_reaction("❌")
        await ctx.send(mention_code.mention)
        
        def check_emoji_1(reaction_2, user_2):
            return reaction_2.emoji == "🟩" or reaction_2.emoji == "🟥" or reaction_2.emoji == "🟨" or reaction_2.emoji == "❌" and user_2.bot == False
        while i == 1:
            try:
                reaction_2, user_2 = await app.wait_for(event='reaction_add', check=check_emoji_1)
                await msg.delete()
                embed=discord.Embed(title = "내전 모집 포스팅을 시작하셨습니다!", description = f"시작시간 {time_set}", color = discord.Color.random())
                embed.set_author(name= ctx.author.display_name, icon_url= ctx.author.avatar_url)
                embed.add_field (name = "현재 인원", value = user_list, inline = False)
                embed.add_field (name = "미확정 인원", value = user_list_alter, inline = False)
                embed.add_field (name = "모집이 끝난후...", value = "반드시 ❌를 눌러 종료해주세요.", inline = False)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/840823850651877387/840823990360211477/league-of-legends.png")
                embed.set_footer (text = str(now_datetime)+ "에 생성됨")
                msg = await ctx.send (embed=embed)
                await msg.add_reaction("🟩")
                await msg.add_reaction("🟥")
                await msg.add_reaction("🟨")
                await msg.add_reaction("❌")
                if str(reaction_2) == "❌":
                    await msg.delete()
                    user_list.clear()
                    user_list_alter.clear()
            except asyncio.TimeoutError:
                await ctx.send("시간이 초과되었습니다.")
                return
#발로란트 내전 모집
    @app.command()
    async def 발로란트내전모집시작(ctx,*,time_set):
        mention_code = discord.utils.get(ctx.guild.roles, id = 808760114999722014)
        embed=discord.Embed(title = "발로란트 내전 모집 포스팅을 시작하셨습니다!", description = f"시작시간 {time_set}", color = discord.Color.random())
        embed.set_author(name= ctx.author.display_name, icon_url= ctx.author.avatar_url)
        embed.add_field (name = "현재 인원", value = user_list, inline = False)
        embed.add_field (name = "미확정 인원", value = user_list_alter, inline = False)
        embed.add_field (name = "모집이 끝난후...", value = "반드시 ❌를 눌러 모집을 종료해주세요", inline = False)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/840823850651877387/840824839911637012/valorant.png")
        embed.set_footer (text = str(now_datetime)+ "에 생성됨")
        msg = await ctx.send (embed=embed)
        await msg.add_reaction("🟩")
        await msg.add_reaction("🟥")
        await msg.add_reaction("🟨")
        await msg.add_reaction("❌")
        await ctx.send(mention_code.mention)
        
        def check_emoji_1(reaction_2, user_2):
            return reaction_2.emoji == "🟩" or reaction_2.emoji == "🟥" or reaction_2.emoji == "🟨" or reaction_2.emoji == "❌" and user_2.bot == False
        while i == 1:
            try:
                reaction_2, user_2 = await app.wait_for(event='reaction_add', check=check_emoji_1)
                await msg.delete()
                embed=discord.Embed(title = "내전 모집 포스팅을 시작하셨습니다!", description = f"시작시간 {time_set}", color = discord.Color.random())
                embed.set_author(name= ctx.author.display_name, icon_url= ctx.author.avatar_url)
                embed.add_field (name = "현재 인원", value = user_list, inline = False)
                embed.add_field (name = "미확정 인원", value = user_list_alter, inline = False)
                embed.add_field (name = "모집이 끝난후...", value = "반드시 ❌를 눌러 종료해주세요.", inline = False)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/840823850651877387/840824839911637012/valorant.png")
                embed.set_footer (text = str(now_datetime)+ "에 생성됨")
                msg = await ctx.send (embed=embed)
                await msg.add_reaction("🟩")
                await msg.add_reaction("🟥")
                await msg.add_reaction("🟨")
                await msg.add_reaction("❌")
                if str(reaction_2) == "❌":
                    await msg.delete()
                    user_list.clear()
                    user_list_alter.clear()
            except asyncio.TimeoutError:
                await ctx.send("시간이 초과되었습니다.")
                return
    @app.event
    async def on_reaction_add(reation, user):
        if user.bot ==1:
            return None
        if str(reation.emoji) == "🟩":
            if len(user_list) >= 10:
                user_list.remove(user.name)
                user_list_alter.append(user.name)
                await reation.message.channel.send(f"인원이 가득 차 참여하실 수 없습니다. {user.name}님은 대기인원입니다.")
            elif str(user.name) in user_list_alter:
                user_list_alter.remove(user.name)
                user_list.append(user.name)
                await reation.message.channel.send(f"{user.name}님이 미확정에서 참가로 변경하셨습니다.")
            else:
                if str(user.name) not in user_list:
                    user_list.append(user.name)
                else:
                    await reation.message.channel.send(f"{user.name}님은 이미 참가하셨습니다.")
                    pass
        if str(reation.emoji) == "🟥":
            if str(user.name) in user_list:
                user_list.remove(user.name)
            if str(user.name) in user_list_alter:
                user_list_alter.remove(user.name)
        if str(reation.emoji) == "🟨":
            if str(user.name) in user_list:
                user_list.remove(user.name)
                user_list_alter.append(user.name)
                await reation.message.channel.send(f"{user.name}님이 참가에서 미확정으로 변경하였습니다.")
            elif str(user.name) not in user_list_alter:
                user_list_alter.append(user.name)
            else:
                pass

#자유 모집 포스팅

    #자유 모집 포스팅 만들기
    
#역할 자동 배정 안내 임베드
    @app.command()
    async def 역할안내(ctx):
        embed=discord.Embed(title = "자동 역할배정 안내입니다", description = "!을 붙인 뒤에 원하는 역할을 띄어쓰기 없이 쓰면됩니다", color = discord.Color.purple())
        embed.set_author(name= ctx.author.display_name, icon_url= ctx.author.avatar_url)
        embed.add_field (name = "현재 있는 역할", value = "13일의 금요일, 레식, 내전, 스터디, 영화, 솔랭, 자랭, 디스코드게임, 격전", inline = True)
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

    #격전 역할 배정
    @app.command(name="격전", pass_context=True)
    async def _HumanRole(ctx, member: discord.Member=None):
        member = member or ctx.message.author
        await member.add_roles(get(ctx.guild.roles, name="격전"))
        await ctx.channel.send(str(member)+"에게 격전 역할이 적용되었습니다.")
    #발로란트 역할 배정
    @app.command(name="발로란트", pass_context=True)
    async def _HumanRole(ctx, member: discord.Member=None):
        member = member or ctx.message.author
        await member.add_roles(get(ctx.guild.roles, name="발로란트"))
        await ctx.channel.send(str(member)+"에게 발로란트 역할이 적용되었습니다.")
    
#공지사항 이벤트 출력
    @app.command()
    async def 공지사항(ctx):
        embed=discord.Embed(title = "한국기술교육대학교", description = "공지사항", color = discord.Color.light_gray())
        embed.add_field (name = "링크를 클릭하세요", value = "[일반공지](<https://portal.koreatech.ac.kr/p/STHOME/>)", inline = True)
        await ctx.send(embed=embed)

app.run(os.environ['token'] )