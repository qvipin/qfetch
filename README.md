# qfetch

<img src="https://files.vipin.xyz/api/public/dl/-lYTy1Wl?inline=true" alt="qfetch" align="right" height="290px">

qfetch is a simple, no-fuss CLI tool written in Python that gives you a clean snapshot of your system info on Linux and macOS. It shows details like your OS, architecture, packages, shell version, terminal type, memory usage, uptime, and even throws in some fun ASCII art for good measure. It’s designed to be straightforward and looks good right out of the box.

Designed & Tested for **Ubuntu**, **Debian**, and **MacOS**. More operating systems and distributions will be added in the near future.

## Installation

qfetch was designed specifically for terminals with **NerdFonts** which you can download at [nerdfonts.com](https://www.nerdfonts.com) and add to your terminal using [these](https://webinstall.dev/nerdfont/) instructions. Afterwards install and run using the following commands...

```bash
pip install qfetch-py
qfetch
```

## Usage

```txt
usage: qfetch [-h]
                 [--art <Playboy-Bunny, Tux, Phoenix, Robot, Random-Art>]
                 [--sys-info <sys_info_default, sys_info_no_nerd_font>]

options:
  -h, --help            show this help message and exit
  --art, -a <Playboy-Bunny, Tux, Phoenix, Robot, Random-Art>
                        select the Ascii Art you want qfetch to use.
  --sys-info, -s <sys_info_default, sys_info_no_nerd_font>
                        select how you want qfetch to present your sysinfo
```

**e.g.**

`qfetch -a Tux`

`qfetch -s sys_info_no_nerd_font`

## License

qfetch, a simple, no-fuss System Information CLI tool written in Python
Copyright (C) 2025 qvipin

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
