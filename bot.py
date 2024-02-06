import os
from dotenv import load_dotenv
import random
import nextcord
from nextcord.ext import commands

load_dotenv()

# Load truth questions from a file
with open("truth.txt") as file:
    truth_questions = file.read().splitlines()

bot = commands.Bot(command_prefix="!")

@bot.slash_command(description="Display a Truth Question", guild_ids=[your guild id])
async def truth(ctx):
    if not truth_questions:
        await ctx.send("There are no truth questions available.")
        return

    # Generate a random index to select a truth question
    truth_index = random.randint(0, len(truth_questions) - 1)
    truth_question = truth_questions[truth_index]

    # Create an initial response
    initial_response = await ctx.send(f"**Truth Question:**\n{truth_question}")

    # Add reactions if needed
    await initial_response.add_reaction('✅')

# Run the bot
bot.run(os.getenv("TOKEN"))
