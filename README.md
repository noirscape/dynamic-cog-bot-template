# Dynamic cog bot template

This is a bot template for the discord.py framework.

It provides you with the ability to load and unload cogs dynamically, as well as providing you the ability to autoload specified cogs.

## Usage

1. Fork this bot.
1. Copy secure.yml.example to secure.yml and fill in your token.
1. Run the bot once to create the `cogs` folder.
1. Put any cogs you want to run inside the `cogs` folder. Cogs that need multiple files should supply a wrapper extension. See `sample_wrapper.py` for an example on how to make a wrapper extension.
1. Supply the cogs that should be ran automatically, as well as the prefix in `config.yml`.

## License

GPLv2, not licensable under later versions.

```py
# Bot cog template - Dynamic cog loading template.
# Copyright (C) 2018 - Valentijn "noirscape" V.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License, version 2 as published by
# the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program. If not, see <http://www.gnu.org/licenses/>.
```