import discord
from discord.ext import commands

import os
BOT_TOKEN = os.getenv("BOT_TOKEN")
PRAYER_CHANNEL_ID = 1483564167930712204

SHEMA_TEXT = """שְׁמַע יִשְׂרָאֵל ה׳ אֱלֹקֵינוּ ה׳ אֶחָד.
בָּרוּךְ שֵׁם כְּבוֹד מַלְכוּתוֹ לְעוֹלָם וָעֶד.

וְאָהַבְתָּ אֵת ה׳ אֱלֹקֶיךָ בְּכָל לְבָבְךָ וּבְכָל נַפְשְׁךָ וּבְכָל מְאֹדֶךָ
וְהָיוּ הַדְּבָרִים הָאֵלֶּה אֲשֶׁר אָנֹכִי מְצַוְּךָ הַיּוֹם עַל לְבָבֶךָ
וְשִׁנַּנְתָּם לְבָנֶיךָ וְדִבַּרְתָּ בָּם בְּשִׁבְתְּךָ בְבֵיתֶךָ וּבְלֶכְתְּךָ בַדֶּרֶךְ וּבְשָׁכְבְּךָ וּבְקוּמֶךָ
וּקְשַׁרְתָּם לְאוֹת עַל יָדֶךָ וְהָיוּ לְטֹטָפֹת בֵּין עֵינֶיךָ
וּכְתַבְתָּם עַל מְזוּזוֹת בֵּיתֶךָ וּבִשְׁעָרֶיךָ

וְהָיָה אִם שָׁמֹעַ תִּשְׁמְעוּ אֶל מִצְו‍ֹתַי אֲשֶׁר אָנֹכִי מְצַוֶּה אֶתְכֶם הַיּוֹם לְאַהֲבָה אֶת ה׳ אֱלֹקֵיכֶם וּלְעָבְדוֹ בְּכָל לְבַבְכֶם וּבְכָל נַפְשְׁכֶם
וְנָתַתִּי מְטַר אַרְצְכֶם בְּעִתּוֹ יוֹרֶה וּמַלְקוֹשׁ וְאָסַפְתָּ דְגָנֶךָ וְתִירֹשְׁךָ וְיִצְהָרֶךָ
וְנָתַתִּי עֵשֶׂב בְּשָׂדְךָ לִבְהֶמְתֶּךָ וְאָכַלְתָּ וְשָׂבָעְתָּ
הִשָּׁמְרוּ לָכֶם פֶּן יִפְתֶּה לְבַבְכֶם וְסַרְתֶּם וַעֲבַדְתֶּם אֱלֹקִים אֲחֵרִים וְהִשְׁתַּחֲוִיתֶם לָהֶם
וְחָרָה אַף ה׳ בָּכֶם וְעָצַר אֶת הַשָּׁמַיִם וְלֹא יִהְיֶה מָטָר וְהָאֲדָמָה לֹא תִתֵּן אֶת יְבוּלָהּ וַאֲבַדְתֶּם מְהֵרָה מֵעַל הָאָרֶץ הַטֹּבָה אֲשֶׁר ה׳ נֹתֵן לָכֶם
וְשַׂמְתֶּם אֶת דְּבָרַי אֵלֶּה עַל לְבַבְכֶם וְעַל נַפְשְׁכֶם וּקְשַׁרְתֶּם אֹתָם לְאוֹת עַל יֶדְכֶם וְהָיוּ לְטוֹטָפֹת בֵּין עֵינֵיכֶם
וְלִמַּדְתֶּם אֹתָם אֶת בְּנֵיכֶם לְדַבֵּר בָּם בְּשִׁבְתְּךָ בְבֵיתֶךָ וּבְלֶכְתְּךָ בַדֶּרֶךְ וּבְשָׁכְבְּךָ וּבְקוּמֶךָ
וּכְתַבְתָּם עַל מְזוּזוֹת בֵּיתֶךָ וּבִשְׁעָרֶיךָ
לְמַעַן יִרְבּוּ יְמֵיכֶם וִימֵי בְנֵיכֶם עַל הָאֲדָמָה אֲשֶׁר נִשְׁבַּע ה׳ לַאֲבֹתֵיכֶם לָתֵת לָהֶם כִּימֵי הַשָּׁמַיִם עַל הָאָרֶץ.

וַיֹּאמֶר ה׳ אֶל מֹשֶׁה לֵּאמֹר.
דַּבֵּר אֶל בְּנֵי יִשְׂרָאֵל וְאָמַרְתָּ אֲלֵהֶם וְעָשׂוּ לָהֶם צִיצִת עַל כַּנְפֵי בִגְדֵיהֶם לְדֹרֹתָם וְנָתְנוּ עַל צִיצִת הַכָּנָף פְּתִיל תְּכֵלֶת.
וְהָיָה לָכֶם לְצִיצִת וּרְאִיתֶם אֹתוֹ וּזְכַרְתֶּם אֶת כָּל מִצְו‍ֹת ה׳ וַעֲשִׂיתֶם אֹתָם וְלֹא תָתוּרוּ אַחֲרֵי לְבַבְכֶם וְאַחֲרֵי עֵינֵיכֶם אֲשֶׁר אַתֶּם זֹנִים אַחֲרֵיהֶם
לְמַעַן תִּזְכְּרוּ וַעֲשִׂיתֶם אֶת כָּל מִצְו‍ֹתָי וִהְיִיתֶם קְדֹשִׁים לֵאלֹקֵיכֶם.
אֲנִי ה׳ אֱלֹקֵיכֶם אֲשֶׁר הוֹצֵאתִי אֶתְכֶם מֵאֶרֶץ מִצְרַיִם לִהְיוֹת לָכֶם לֵאלֹקִים אֲנִי ה׳ אֱלֹקֵיכֶם"""

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)


def split_text(text, max_length=1800):
    parts = []
    current = ""

    for paragraph in text.split("\n\n"):
        if len(current) + len(paragraph) + 2 <= max_length:
            if current:
                current += "\n\n"
            current += paragraph
        else:
            if current:
                parts.append(current)
            current = paragraph

    if current:
        parts.append(current)

    return parts

class PrayerView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(
        label="📖 שמע ישראל",
        style=discord.ButtonStyle.primary,
        custom_id="shema_button"
    )
    async def send_shema(self, interaction: discord.Interaction, button: discord.ui.Button):
    parts = split_text(SHEMA_TEXT)

    await interaction.response.send_message(parts[0], ephemeral=True)

    for part in parts[1:]:
        await interaction.followup.send(part, ephemeral=True)

@bot.event
async def on_ready():
    bot.add_view(PrayerView())
    await bot.tree.sync()
    print(f"Logged in as {bot.user}")


@bot.tree.command(name="setup_prayer", description="יצירת כפתור שמע")
async def setup_prayer(interaction):
    await interaction.response.send_message(
        "לחץ כדי לשלוח שמע ישראל:",
        view=PrayerView()
    )


bot.run(BOT_TOKEN)
