import discord
from discord.ext import commands

from .Nata.Formation import Formation


class DevCommands(commands.Cog, name='Developer Commands'):
	'''These are the developer commands'''

	def __init__(self, bot):
		self.bot = bot

	async def cog_check(self, ctx):
		return ctx.author.id in self.bot.owner_ids


	@commands.command(name="listcogs", aliases=['lc'])
	async def listcogs(self, ctx):
		'''
		Returns a list of all enabled commands.
		'''
		embed = discord.Embed(title="Cogs List", description="A list of all cogs", color=0xE91E63)
		message = "***-***\n".join([str(cog) for cog in self.bot.extensions])
		embed.add_field(name="test", value=message)
		await ctx.send(embed=embed)

	@commands.command(name="args", aliases=['ar'])
	async def multi_quote(self, ctx, *args):
			one_word_per_line = '\n'.join(args)
			quote_text = 'You said:\n>>> {}'.format(one_word_per_line)
			await ctx.send(quote_text)


	@commands.command(name="formation", aliases=['fm'])
	async def formation(self, ctx, time):
		frm = Formation( self.bot, ctx, time, ctx.author.id)
		await frm.confirmation()


	@commands.command(name="assign_roles")
	async def assign_roles(self, ctx, *, role_names):
		'''
		Assigns roles to a user/users. ( )
		'''
		roles = role_names.split(',')
		for role in roles:
			role = role.strip()
			role = discord.utils.get(ctx.guild.roles, name=role)
			await ctx.author.add_roles(role)


	@commands.command(name="rolesInit", aliases=['ri'])
	async def roles__init__(self, ctx):
			channel = discord.utils.get(ctx.guild.channels, name="roles")
			# if len (await channel.history(limit=10).flatten() ) != 0:
			# 	return
			embed = discord.Embed(title="Product Select", description="React to the emojis corresponding with what you need", color=0xE91E63)
			embed.add_field(name="test", value="""
:white_check_mark: :    big data
***-***
:heart: :    immmmm
***-***
:x: :    cmmmmm
""")
			message = await channel.send(embed=embed)
			await message.add_reaction("✅")
			await message.add_reaction("❤️")
			await message.add_reaction("❌")


def setup(bot):
	bot.add_cog(DevCommands(bot))
