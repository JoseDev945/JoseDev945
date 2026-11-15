"""Genera los SVG del perfil de JoseDev945 (tema océano / sonar)."""
import math, os, sys

OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)

THEMES = {
    "dark": dict(bg="#07131f", win="#0b1b2b", panel="#0e2236", border="#1d4a66", line="#163650",
                 text="#d3e3f0", muted="#7f97ad", teal="#4fd1c5", amber="#f6b45a", coral="#ff7b72",
                 sea1="#0f3b57", sea2="#0b2c44", sky1="#1a2a4a", sky2="#3b2d4f", sun="#f6b45a"),
    "light": dict(bg="#eef4f9", win="#f8fbfd", panel="#ffffff", border="#a9c7dc", line="#d6e5ef",
                  text="#15283a", muted="#5d7489", teal="#0e8a87", amber="#c06a00", coral="#cf3f4f",
                  sea1="#7cc4d6", sea2="#4a9fb8", sky1="#ffd9a8", sky2="#ffb59a", sun="#ff8c42"),
}
MONO = "ui-monospace, 'SFMono-Regular', 'JetBrains Mono', Menlo, Consolas, monospace"

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

# ---------------------------------------------------------------- banner
TOML = [
    ("h", "[perfil]"),
    ("kv", "nombre", '"José González"'),
    ("kv", "rol", '"Desarrollador de Software"'),
    ("kv", "empresa", '"Botes Galileo"'),
    ("kv", "puerto", '"Panamá"'),
    ("kv", "enfoque", '"Web · 3D · Videojuegos"'),
    ("b",),
    ("h", "[stack]"),
    ("kv", "web", '["Next.js", "React", "TypeScript"]'),
    ("kv", "tres_d", '["Three.js", "Rapier"]'),
    ("kv", "juegos", '["Godot 4", "GDScript"]'),
    ("kv", "backend", '["Node.js", "PostgreSQL"]'),
    ("kv", "deploy", '["Vercel", "pnpm"]'),
    ("b",),
    ("h", "[contacto]"),
    ("kv", "github", '"JoseDev945"'),
    ("kv", "zona", '"UTC-5 · Ciudad de Panamá"'),
]
BLIPS = [("GALILEO", 0.62, 38), ("PORTAFOLIO", 0.58, 140), ("TIENDA", 0.45, 230), ("FRUIT-BRAWL", 0.74, 312)]

def banner(t):
    W, H = 960, 500
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" xml:space="preserve" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="{MONO}">']
    o.append(f'''<defs>
<radialGradient id="sg" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="{t['teal']}" stop-opacity=".18"/><stop offset="100%" stop-color="{t['teal']}" stop-opacity="0"/></radialGradient>
<linearGradient id="sweep" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="{t['teal']}" stop-opacity="0"/><stop offset="100%" stop-color="{t['teal']}" stop-opacity=".55"/></linearGradient>
</defs>''')
    o.append(f'<rect width="{W}" height="{H}" rx="18" fill="{t["bg"]}"/>')
    o.append(f'<rect x="10" y="10" width="{W-20}" height="{H-20}" rx="14" fill="{t["win"]}" stroke="{t["border"]}"/>')
    # title bar
    for i, c in enumerate([t["coral"], t["amber"], t["teal"]]):
        o.append(f'<circle cx="{34+i*20}" cy="34" r="6" fill="{c}"/>')
    o.append(f'<text x="{W/2}" y="39" text-anchor="middle" font-size="13" fill="{t["muted"]}">jose@galileo: ~/perfil — nano perfil.toml</text>')
    o.append(f'<line x1="10" y1="58" x2="{W-10}" y2="58" stroke="{t["line"]}"/>')

    # ---- left panel: sonar
    lx, ly, lw, lh = 28, 76, 330, 396
    o.append(f'<rect x="{lx}" y="{ly}" width="{lw}" height="{lh}" rx="10" fill="{t["panel"]}" stroke="{t["border"]}"/>')
    o.append(f'<text x="{lx+16}" y="{ly+26}" font-size="13" font-weight="700" fill="{t["text"]}" letter-spacing="1.5">SONAR.PROYECTOS</text>')
    o.append(f'<text x="{lx+lw-16}" y="{ly+26}" text-anchor="end" font-size="11" fill="{t["muted"]}">rango 4 · activo</text>')
    o.append(f'<line x1="{lx}" y1="{ly+40}" x2="{lx+lw}" y2="{ly+40}" stroke="{t["line"]}"/>')
    cx, cy, R = lx + lw/2, ly + 214, 138
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="url(#sg)"/>')
    for k in range(1, 5):
        o.append(f'<circle cx="{cx}" cy="{cy}" r="{R*k/4:.1f}" fill="none" stroke="{t["teal"]}" stroke-opacity="{.15+.08*k:.2f}" stroke-dasharray="{"" if k==4 else "3 5"}"/>')
    for a in range(0, 360, 30):
        r = math.radians(a)
        o.append(f'<line x1="{cx}" y1="{cy}" x2="{cx+R*math.cos(r):.1f}" y2="{cy+R*math.sin(r):.1f}" stroke="{t["teal"]}" stroke-opacity=".12"/>')
    # sweep wedge
    wedge = []
    for a in range(-40, 1, 2):
        r = math.radians(a)
        wedge.append(f'{cx+R*math.cos(r):.1f},{cy+R*math.sin(r):.1f}')
    o.append(f'<g><polygon points="{cx},{cy} {" ".join(wedge)}" fill="url(#sweep)" opacity=".7"/>'
             f'<line x1="{cx}" y1="{cy}" x2="{cx+R}" y2="{cy}" stroke="{t["teal"]}" stroke-width="2"/>'
             f'<animateTransform attributeName="transform" type="rotate" from="0 {cx} {cy}" to="360 {cx} {cy}" dur="6s" repeatCount="indefinite"/></g>')
    for i, (name, d, ang) in enumerate(BLIPS):
        r = math.radians(ang)
        bx, by = cx + R*d*math.cos(r), cy + R*d*math.sin(r)
        delay = ang / 360 * 6
        o.append(f'<circle cx="{bx:.1f}" cy="{by:.1f}" r="4" fill="{t["amber"]}"><animate attributeName="opacity" values="1;.25;1" dur="6s" begin="{delay:.2f}s" repeatCount="indefinite"/></circle>')
        o.append(f'<circle cx="{bx:.1f}" cy="{by:.1f}" r="4" fill="none" stroke="{t["amber"]}"><animate attributeName="r" values="4;14" dur="2s" begin="{delay:.2f}s" repeatCount="indefinite"/><animate attributeName="opacity" values=".8;0" dur="2s" begin="{delay:.2f}s" repeatCount="indefinite"/></circle>')
        anchor = "start" if math.cos(r) >= 0 else "end"
        dx = 10 if anchor == "start" else -10
        o.append(f'<text x="{bx+dx:.1f}" y="{by+4:.1f}" text-anchor="{anchor}" font-size="10.5" font-weight="700" fill="{t["text"]}">{name}</text>')
    # boat at center
    o.append(f'<path d="M{cx-11},{cy+3} L{cx+11},{cy+3} L{cx+7},{cy+9} L{cx-7},{cy+9} Z" fill="{t["coral"]}"/>'
             f'<path d="M{cx},{cy+2} L{cx},{cy-13} L{cx+9},{cy+1} Z" fill="{t["text"]}"/>')
    o.append(f'<text x="{lx+16}" y="{ly+lh-16}" font-size="10.5" fill="{t["muted"]}">4 contactos · rumbo: producción</text>')

    # ---- right panel: editor
    rx, ry, rw, rh = 376, 76, 556, 396
    o.append(f'<rect x="{rx}" y="{ry}" width="{rw}" height="{rh}" rx="10" fill="{t["panel"]}" stroke="{t["border"]}"/>')
    o.append(f'<text x="{rx+16}" y="{ry+26}" font-size="13" font-weight="700" fill="{t["text"]}">perfil.toml</text>')
    o.append(f'<rect x="{rx+rw-128}" y="{ry+11}" width="112" height="22" rx="11" fill="{t["teal"]}" fill-opacity=".15" stroke="{t["teal"]}" stroke-opacity=".5"/>')
    o.append(f'<text x="{rx+rw-72}" y="{ry+26}" text-anchor="middle" font-size="11.5" font-weight="700" fill="{t["teal"]}">@JoseDev945</text>')
    o.append(f'<line x1="{rx}" y1="{ry+40}" x2="{rx+rw}" y2="{ry+40}" stroke="{t["line"]}"/>')
    y = ry + 62
    for n, row in enumerate(TOML, 1):
        o.append(f'<text x="{rx+30}" y="{y}" text-anchor="end" font-size="11" fill="{t["muted"]}" fill-opacity=".7">{n}</text>')
        if row[0] == "h":
            o.append(f'<text x="{rx+44}" y="{y}" font-size="12.5" font-weight="700" fill="{t["amber"]}">{esc(row[1])}</text>')
        elif row[0] == "kv":
            o.append(f'<text x="{rx+44}" y="{y}" font-size="12.5"><tspan fill="{t["teal"]}">{esc(row[1])}</tspan><tspan fill="{t["muted"]}"> = </tspan><tspan fill="{t["text"]}">{esc(row[2])}</tspan></text>')
        y += 17.5
    # cursor
    o.append(f'<rect x="{rx+44}" y="{y-12}" width="8" height="15" fill="{t["teal"]}"><animate attributeName="opacity" values="1;0;1" dur="1.1s" repeatCount="indefinite"/></rect>')
    # nano footer
    fy = ry + rh - 30
    o.append(f'<line x1="{rx}" y1="{fy-10}" x2="{rx+rw}" y2="{fy-10}" stroke="{t["line"]}"/>')
    x = rx + 16
    for key, lbl in [("^O", "Guardar"), ("^W", "Buscar"), ("^K", "Cortar"), ("^X", "Zarpar")]:
        o.append(f'<rect x="{x}" y="{fy+1}" width="24" height="17" rx="3" fill="{t["text"]}"/>')
        o.append(f'<text x="{x+12}" y="{fy+14}" text-anchor="middle" font-size="11" font-weight="700" fill="{t["panel"]}">{key}</text>')
        o.append(f'<text x="{x+30}" y="{fy+14}" font-size="11.5" fill="{t["text"]}">{lbl}</text>')
        x += 106
    o.append(f'<text x="{rx+rw-16}" y="{fy+14}" text-anchor="end" font-size="11" fill="{t["muted"]}">{len(TOML)} líneas</text>')
    o.append('</svg>')
    return "\n".join(o)

# ---------------------------------------------------------------- whoami card
def whoami(t):
    W, H = 960, 360
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" xml:space="preserve" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="{MONO}">']
    o.append(f'''<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="{t['sky1']}"/><stop offset="100%" stop-color="{t['sky2']}"/></linearGradient>
<linearGradient id="sea" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="{t['sea1']}"/><stop offset="100%" stop-color="{t['sea2']}"/></linearGradient>
<clipPath id="art"><rect x="652" y="70" width="280" height="262" rx="10"/></clipPath>
</defs>''')
    o.append(f'<rect width="{W}" height="{H}" rx="18" fill="{t["bg"]}"/>')
    o.append(f'<rect x="10" y="10" width="{W-20}" height="{H-20}" rx="14" fill="{t["win"]}" stroke="{t["border"]}"/>')
    for i, c in enumerate([t["coral"], t["amber"], t["teal"]]):
        o.append(f'<circle cx="{34+i*20}" cy="36" r="6" fill="{c}"/>')
    o.append(f'<text x="104" y="41" font-size="13" fill="{t["muted"]}">jose@galileo · zsh · conectado</text>')
    # left box
    o.append(f'<rect x="28" y="70" width="606" height="262" rx="10" fill="{t["panel"]}" stroke="{t["border"]}"/>')
    def prompt(y, cmd):
        return (f'<text x="48" y="{y}" font-size="16" font-weight="700"><tspan fill="{t["coral"]}">❯</tspan>'
                f'<tspan fill="{t["teal"]}"> {esc(cmd)}</tspan></text>')
    o.append(prompt(102, "whoami"))
    o.append(f'<text x="48" y="130" font-size="15"><tspan fill="{t["text"]}">josé_gonzález</tspan><tspan fill="{t["muted"]}">  —  </tspan><tspan fill="{t["amber"]}">Desarrollador de Software</tspan></text>')
    o.append(f'<line x1="48" y1="146" x2="614" y2="146" stroke="{t["line"]}"/>')
    rows = [("puerto:", "Panamá · Botes Galileo"), ("misión:", "webs rápidas y mundos 3D que se juegan")]
    y = 172
    for k, v in rows:
        o.append(f'<text x="48" y="{y}" font-size="13.5" fill="{t["muted"]}">{k}</text><text x="150" y="{y}" font-size="13.5" fill="{t["text"]}">{esc(v)}</text>')
        y += 24
    o.append(prompt(238, "ls ./bitacora/"))
    rows = [("web/", "Next.js · React · TypeScript · Tailwind"), ("3d_y_juegos/", "Three.js · Rapier · Godot 4"),
            ("backend/", "Node.js · PostgreSQL · Vercel")]
    y = 264
    for k, v in rows:
        o.append(f'<text x="48" y="{y}" font-size="13.5" fill="{t["amber"]}">{k}</text><text x="190" y="{y}" font-size="13.5" fill="{t["text"]}">{esc(v)}</text>')
        y += 22
    # right art: sunset at sea with a boat
    o.append(f'<g clip-path="url(#art)">')
    o.append(f'<rect x="652" y="70" width="280" height="262" fill="url(#sky)"/>')
    o.append(f'<circle cx="792" cy="214" r="54" fill="{t["sun"]}" fill-opacity=".95"/>')
    o.append(f'<rect x="652" y="214" width="280" height="120" fill="url(#sea)"/>')
    for i in range(5):
        yy = 226 + i*14
        o.append(f'<rect x="{752-i*6}" y="{yy}" width="{80+i*12}" height="2.5" rx="1.2" fill="{t["sun"]}" fill-opacity="{.6-i*.1:.2f}"/>')
    # boat bobbing
    o.append(f'''<g><path d="M732,212 L788,212 L780,224 L740,224 Z" fill="{t['coral']}"/>
<path d="M758,210 L758,170 L784,208 Z" fill="{t['win']}"/><path d="M754,210 L754,180 L736,208 Z" fill="{t['win']}" fill-opacity=".8"/>
<animateTransform attributeName="transform" type="translate" values="0,0; 0,-3; 0,0" dur="3s" repeatCount="indefinite"/></g>''')
    o.append(f'''<path d="M652,236 q20,-8 40,0 t40,0 t40,0 t40,0 t40,0 t40,0 t40,0 t40,0" fill="none" stroke="{t['teal']}" stroke-width="2.5" stroke-opacity=".8">
<animateTransform attributeName="transform" type="translate" values="0,0; -40,0" dur="4s" repeatCount="indefinite"/></path>''')
    o.append('</g>')
    o.append(f'<rect x="652" y="70" width="280" height="262" rx="10" fill="none" stroke="{t["border"]}"/>')
    o.append(f'<rect x="664" y="82" width="140" height="24" rx="6" fill="#0b1b2b" fill-opacity=".6"/>')
    o.append(f'<text x="674" y="99" font-size="12.5" font-weight="700" fill="#ffffff">pacífico.runtime</text>')
    o.append(f'<rect x="664" y="300" width="186" height="22" rx="6" fill="#0b1b2b" fill-opacity=".6"/>')
    o.append(f'<text x="674" y="316" font-size="11.5" fill="#ffffff">estado: siempre navegando</text>')
    o.append('</svg>')
    return "\n".join(o)

# ---------------------------------------------------------------- radar
def radar(t, title, axes, color_key):
    W, H = 480, 420
    cx, cy, R = W/2, 228, 112
    n = len(axes)
    col = t[color_key]
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" xml:space="preserve" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="{MONO}">']
    o.append(f'<rect width="{W}" height="{H}" rx="16" fill="{t["win"]}" stroke="{t["border"]}"/>')
    o.append(f'<text x="22" y="34" font-size="13" font-weight="700" fill="{t["text"]}">{esc(title)}</text>')
    o.append(f'<text x="{W-22}" y="34" text-anchor="end" font-size="11" fill="{t["muted"]}">escala 0–100</text>')
    o.append(f'<line x1="12" y1="50" x2="{W-12}" y2="50" stroke="{t["line"]}"/>')
    for k in range(1, 6):
        o.append(f'<circle cx="{cx}" cy="{cy}" r="{R*k/5:.1f}" fill="none" stroke="{t["muted"]}" stroke-opacity="{.15 + .05*k:.2f}" stroke-dasharray="{"" if k==5 else "2 4"}"/>')
    pts = []
    for i, (name, v) in enumerate(axes):
        a = -math.pi/2 + 2*math.pi*i/n
        ex, ey = cx + R*math.cos(a), cy + R*math.sin(a)
        o.append(f'<line x1="{cx}" y1="{cy}" x2="{ex:.1f}" y2="{ey:.1f}" stroke="{t["muted"]}" stroke-opacity=".25"/>')
        pts.append((cx + R*v/100*math.cos(a), cy + R*v/100*math.sin(a)))
        lx, ly = cx + (R+22)*math.cos(a), cy + (R+22)*math.sin(a)
        anchor = "middle" if abs(math.cos(a)) < .3 else ("start" if math.cos(a) > 0 else "end")
        ly += 4 + (6 if math.sin(a) > .5 else (-4 if math.sin(a) < -.5 else 0))
        o.append(f'<text x="{lx:.1f}" y="{ly:.1f}" text-anchor="{anchor}" font-size="12" font-weight="700" fill="{t["text"]}">{esc(name)}</text>')
        o.append(f'<text x="{lx:.1f}" y="{ly+14:.1f}" text-anchor="{anchor}" font-size="10.5" fill="{t["muted"]}">{v}</text>')
    poly = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    o.append(f'<polygon points="{poly}" fill="{col}" fill-opacity=".22" stroke="{col}" stroke-width="2.5" stroke-linejoin="round"/>')
    for x, y in pts:
        o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.5" fill="{t["win"]}" stroke="{col}" stroke-width="2.5"/>')
    o.append('</svg>')
    return "\n".join(o)

SKILLS = [("Frontend", 90), ("3D / WebGL", 80), ("Game Dev", 70), ("Deploy", 75), ("SQL / BD", 60), ("Backend", 70)]
LANGS = [("JavaScript", 92), ("TypeScript", 82), ("CSS", 80), ("GDScript", 65), ("SQL", 60), ("Shaders", 40)]

for name, t in THEMES.items():
    files = {
        f"banner-{name}.svg": banner(t),
        f"whoami-{name}.svg": whoami(t),
        f"sonar-skills-{name}.svg": radar(t, "sonar --habilidades", SKILLS, "teal"),
        f"sonar-langs-{name}.svg": radar(t, "sonar --lenguajes", LANGS, "amber"),
    }
    for fn, s in files.items():
        with open(os.path.join(OUT, fn), "w", encoding="utf-8") as f:
            f.write(s)
print("ok")
