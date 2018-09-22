def setup(bot):
    bot.load_extension("cogs.subfoldered_cog.sample_subfolder")

def teardown(bot):
    bot.unload_extension("cogs.subfoldered_cog.sample_subfolder")