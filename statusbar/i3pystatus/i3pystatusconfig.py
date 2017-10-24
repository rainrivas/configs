from i3pystatus import Status

status = Status()

# Shows pulseaudio default sink volume
#
# Note: requires libpulseaudio from PyPI
status.register("pulseaudio",
    format="♪{volume}",)

# Shows your CPU temperature, if you have an Intel CPU
status.register("temp",
    format="{temp:.0f}°C",)

# Displays clock like this:
# Tue 30 Jul 11:59:46 PM KW31
#                          ^-- calendar week
status.register("clock",
    format="%a %b %-d | %X | Week %V",)

# This would look like this:
# Discharging 6h:51m
status.register("battery",
    format="{status} {remaining:%E%hh:%Mm}",
    alert=True,
    alert_percentage=5,
    status={
        "DIS":  "Halp in",
        "CHR":  "NomNom for",
        "FULL": "FULL",
    },)

status.register("now_playing",
    status={
        "pause": "▷",
        "play": "▶",
        "stop": "◾",
    },
    format="{status} {artist} - {title} ",
    on_upscroll=[],
    on_downscroll=[],
    on_middleclick=[],
    on_rightclick=["player_command", "Stop"],)

status.run()
