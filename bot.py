## IMPORTS ##
from interactions import slash_command, Client
import interactions
import pyautogui
import token_manager

## VARIABLES ##
bot = interactions.Client()

@slash_command(
    name="screenshot",
    description="Make a screenshot of the screen"
)
async def take_screenshot(ctx):
    try:
        screenshot = pyautogui.screenshot()
        screenshot.save("screenshot.png")
        await ctx.send(embed={
            "title": "Screenshot Taken",
            "description": "Here's the screenshot:",
            "image": {"url": "attachment://screenshot.png"},
            "color": 0x00ff00  # Green color
        }, file="screenshot.png")
    except Exception as e:
        await ctx.send(embed={
            "title": "Error",
            "description": f"An error occurred: {str(e)}",
            "color": 0xff0000  # Red color
        })

@slash_command(
    name="exit",
    description="Exit the macro"
)
async def exit_macro(ctx):
    try:
        pyautogui.press('f3')
        await ctx.send(embed={
            "title": "Macro Exited",
            "description": "The macro has been exited successfully.",
            "color": 0x0000ff  # Blue color
        })
    except Exception as e:
        await ctx.send(embed={
            "title": "Error",
            "description": f"An error occurred: {str(e)}",
            "color": 0xff0000  # Red color
        })

@slash_command(
    name="pause",
    description="Pause the macro"
)
async def pause_macro(ctx):
    try:
        pyautogui.press('f2')
        await ctx.send(embed={
            "title": "Macro Paused",
            "description": "The macro has been paused.",
            "color": 0xffff00  # Yellow color
        })
    except Exception as e:
        await ctx.send(embed={
            "title": "Error",
            "description": f"An error occurred: {str(e)}",
            "color": 0xff0000  # Red color
        })

@slash_command(
    name="start",
    description="Start the macro"
)
async def start_macro(ctx):
    try:
        pyautogui.press('f1')
        await ctx.send(embed={
            "title": "Macro Started",
            "description": "The macro has been started.",
            "color": 0x00ff00  # Green color
        })
    except Exception as e:
        await ctx.send(embed={
            "title": "Error",
            "description": f"An error occurred: {str(e)}",
            "color": 0xff0000  # Red color
        })

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

directory = "bot/token/token.txt"
token = token_manager.read_token(directory)
if not token:
    token_manager.show_token_popup(directory)
    token = token_manager.read_token(directory)
bot.start(token)
