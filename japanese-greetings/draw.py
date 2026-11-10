# -*- coding: utf-8 -*-
import io
import math
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'img')
os.makedirs(OUT, exist_ok=True)

NAVY = '#1C2A4A'
INK = '#23262D'
WHITE = '#FFFFFF'
LINE = '#C9CED8'
GREEN = '#00A84D'
YELLOW = '#F5B700'
RED = '#D7372B'
ORANGE = '#EF7C1C'
BLUE = '#0052A4'
SKY = '#00A5DE'

def svg(name, body, vb='0 0 160 100'):
    s = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}">{body}</svg>\n'
    io.open(os.path.join(OUT, name), 'w', encoding='utf-8', newline='\n').write(s)

# c01: Alarm clock for morning (7:00 am)
svg('c01-alarm.svg',
    f'<path d="M52 26 L62 36 M108 26 L98 36" stroke="{LINE}" stroke-width="4" stroke-linecap="round"/>'
    f'<path d="M48 22 A12 12 0 0 1 66 32 L54 36 Z" fill="{ORANGE}"/>'
    f'<path d="M112 22 A12 12 0 0 0 94 32 L106 36 Z" fill="{ORANGE}"/>'
    f'<circle cx="80" cy="56" r="32" fill="{WHITE}" stroke="{LINE}" stroke-width="3"/>'
    f'<circle cx="80" cy="56" r="28" fill="#F8FAFC"/>'
    f'<circle cx="80" cy="56" r="2.5" fill="{INK}"/>'
    f'<line x1="80" y1="56" x2="80" y2="38" stroke="{INK}" stroke-width="2.5" stroke-linecap="round"/>'
    f'<line x1="80" y1="56" x2="68" y2="68" stroke="{ORANGE}" stroke-width="2" stroke-linecap="round"/>'
    f'<path d="M60 84 L54 94 M100 84 L106 94" stroke="{LINE}" stroke-width="3.5" stroke-linecap="round"/>')

# c02: Front door of house
svg('c02-door.svg',
    f'<rect x="45" y="10" width="70" height="84" rx="2" fill="#E2E8F0" stroke="{LINE}" stroke-width="2.5"/>'
    f'<rect x="52" y="14" width="56" height="80" fill="{BLUE}"/>'
    f'<rect x="58" y="20" width="20" height="32" rx="2" fill="{WHITE}" opacity="0.85"/>'
    f'<rect x="82" y="20" width="20" height="32" rx="2" fill="{WHITE}" opacity="0.85"/>'
    f'<rect x="58" y="58" width="20" height="30" rx="2" fill="#1E3A8A"/>'
    f'<rect x="82" y="58" width="20" height="30" rx="2" fill="#1E3A8A"/>'
    f'<circle cx="98" cy="56" r="3" fill="{YELLOW}"/>'
    f'<rect x="40" y="94" width="80" height="4" rx="2" fill="{LINE}"/>')

# c03: Waving hand
svg('c03-handwave.svg',
    f'<path d="M72 88 L72 64 L66 52 A5 5 0 0 1 74 46 L78 54 L78 36 A5 5 0 0 1 88 36 L88 52 L90 38 A5 5 0 0 1 100 40 L98 55 L100 45 A4 4 0 0 1 108 47 L102 70 L96 88 Z" fill="{WHITE}" stroke="{LINE}" stroke-width="2.5" stroke-linejoin="round"/>'
    f'<path d="M116 35 Q126 50 116 65" fill="none" stroke="{YELLOW}" stroke-width="2.5" stroke-linecap="round"/>'
    f'<path d="M124 30 Q138 50 124 70" fill="none" stroke="{ORANGE}" stroke-width="2" stroke-linecap="round"/>')

# c04: Bright sun
svg('c04-sun.svg',
    f'<circle cx="80" cy="50" r="22" fill="{YELLOW}" stroke="{ORANGE}" stroke-width="2.5"/>'
    f'<g stroke="{ORANGE}" stroke-width="3" stroke-linecap="round">'
    f'<line x1="80" y1="16" x2="80" y2="22"/>'
    f'<line x1="80" y1="78" x2="80" y2="84"/>'
    f'<line x1="46" y1="50" x2="52" y2="50"/>'
    f'<line x1="108" y1="50" x2="114" y2="50"/>'
    f'<line x1="56" y1="26" x2="60" y2="30"/>'
    f'<line x1="100" y1="70" x2="104" y2="74"/>'
    f'<line x1="56" y1="74" x2="60" y2="70"/>'
    f'<line x1="100" y1="30" x2="104" y2="26"/>'
    f'</g>')

# c05: Crescent moon and evening stars
svg('c05-moon.svg',
    f'<path d="M84 18 A34 34 0 1 0 102 78 A28 28 0 1 1 84 18 Z" fill="{YELLOW}" stroke="{LINE}" stroke-width="2"/>'
    f'<g fill="{SKY}">'
    f'<path d="M42 30 L44 36 L50 38 L44 40 L42 46 L40 40 L34 38 L40 36 Z"/>'
    f'<path d="M116 28 L117 32 L121 33 L117 34 L116 38 L115 34 L111 33 L115 32 Z"/>'
    f'<path d="M124 58 L125 61 L128 62 L125 63 L124 66 L123 63 L120 62 L123 61 Z"/>'
    f'</g>')

# c06: Bed for good night
svg('c06-bed.svg',
    f'<rect x="28" y="32" width="10" height="54" rx="3" fill="{NAVY}"/>'
    f'<rect x="122" y="52" width="10" height="34" rx="3" fill="{NAVY}"/>'
    f'<rect x="36" y="60" width="88" height="14" rx="2" fill="{LINE}"/>'
    f'<rect x="42" y="46" width="24" height="16" rx="4" fill="{WHITE}" stroke="{LINE}" stroke-width="2"/>'
    f'<path d="M60 54 H122 V74 H60 Z" fill="{BLUE}"/>'
    f'<path d="M60 54 Q72 50 84 54 L84 62 L60 62 Z" fill="{SKY}"/>')

# c07: Polite bow
svg('c07-bow.svg',
    f'<ellipse cx="64" cy="28" rx="10" ry="12" fill="{INK}"/>'
    f'<path d="M64 40 C75 42 88 50 96 66 L86 78 C78 68 70 60 60 56 Z" fill="{NAVY}"/>'
    f'<path d="M60 56 L64 88 L52 88 L46 62 Z" fill="{INK}"/>'
    f'<line x1="88" y1="56" x2="80" y2="76" stroke="{WHITE}" stroke-width="3" stroke-linecap="round"/>'
    f'<path d="M26 90 H134" stroke="{LINE}" stroke-width="2.5" stroke-linecap="round"/>')

# c08: ID card badge
svg('c08-idcard.svg',
    f'<path d="M80 8 L80 24 M76 24 H84" stroke="{BLUE}" stroke-width="3" stroke-linecap="round"/>'
    f'<rect x="52" y="24" width="56" height="68" rx="4" fill="{WHITE}" stroke="{LINE}" stroke-width="2"/>'
    f'<rect x="52" y="24" width="56" height="12" rx="3" fill="{BLUE}"/>'
    f'<circle cx="80" cy="30" r="2.5" fill="{WHITE}"/>'
    f'<rect x="68" y="42" width="24" height="24" rx="3" fill="#E2E8F0" stroke="{LINE}" stroke-width="1.5"/>'
    f'<circle cx="80" cy="51" r="5" fill="{NAVY}"/>'
    f'<path d="M72 64 C72 58 88 58 88 64 Z" fill="{NAVY}"/>'
    f'<rect x="62" y="72" width="36" height="4" rx="2" fill="{INK}"/>'
    f'<rect x="68" y="80" width="24" height="3" rx="1.5" fill="{LINE}"/>')

# c09: Friendly greeting hands
svg('c09-hands.svg',
    f'<path d="M30 62 L54 50 L64 56 L52 72 L36 74 Z" fill="{NAVY}"/>'
    f'<path d="M130 62 L106 50 L96 56 L108 72 L124 74 Z" fill="{BLUE}"/>'
    f'<path d="M54 50 L72 38 C76 35 84 35 88 38 L106 50" fill="none" stroke="{LINE}" stroke-width="3"/>'
    f'<ellipse cx="80" cy="56" rx="18" ry="12" fill="{WHITE}" stroke="{LINE}" stroke-width="2.5"/>'
    f'<path d="M72 50 L88 50 M70 56 L90 56 M74 62 L86 62" stroke="{YELLOW}" stroke-width="2.5" stroke-linecap="round"/>')

# Explain tiles:
svg('x-sun.svg',
    f'<circle cx="80" cy="50" r="24" fill="{YELLOW}" stroke="{ORANGE}" stroke-width="2"/>'
    f'<g stroke="{ORANGE}" stroke-width="3" stroke-linecap="round">'
    f'<line x1="80" y1="14" x2="80" y2="20"/><line x1="80" y1="80" x2="80" y2="86"/>'
    f'<line x1="44" y1="50" x2="50" y2="50"/><line x1="110" y1="50" x2="116" y2="50"/>'
    f'</g>')

svg('x-bow.svg',
    f'<ellipse cx="66" cy="30" rx="9" ry="11" fill="{INK}"/>'
    f'<path d="M66 41 C76 43 88 51 94 65 L84 75 C77 66 70 59 62 55 Z" fill="{BLUE}"/>'
    f'<path d="M62 55 L64 85 L54 85 L48 60 Z" fill="{INK}"/>'
    f'<line x1="30" y1="88" x2="130" y2="88" stroke="{LINE}" stroke-width="2"/>')

svg('x-card.svg',
    f'<rect x="54" y="16" width="52" height="68" rx="4" fill="{WHITE}" stroke="{LINE}" stroke-width="2"/>'
    f'<rect x="54" y="16" width="52" height="12" rx="3" fill="{GREEN}"/>'
    f'<circle cx="80" cy="42" r="8" fill="{NAVY}"/>'
    f'<rect x="64" y="58" width="32" height="4" rx="2" fill="{INK}"/>'
    f'<rect x="68" y="66" width="24" height="3" rx="1.5" fill="{LINE}"/>')

svg('x-hands.svg',
    f'<ellipse cx="80" cy="50" rx="28" ry="18" fill="{WHITE}" stroke="{LINE}" stroke-width="2.5"/>'
    f'<path d="M66 44 L94 44 M62 50 L98 50 M66 56 L94 56" stroke="{ORANGE}" stroke-width="3" stroke-linecap="round"/>')

print("SVGs successfully generated in", OUT)
