#!/usr/bin/env python3
"""Grafer till blogginlagget 'Vad kostar en sjomil under segel?'
Motorbaten ar en Elling E3, 13.80m, 15 ton, CE-A.
Driftpunkter: 6 kn = 0.5 l/NM (agarnas uppmatta), 7.5 kn = 1.0 l/NM (varvet),
16 kn = 3.8 l/NM (varvet)."""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter
from scipy.interpolate import PchipInterpolator

OUT = "/mnt/user-data/outputs"

NM_AR      = 2250
NM_MOTOR   = 750
DIESEL     = 20.0
FREYA_LNM  = 0.469
SEGEL_KR   = 90_000
SEGEL45_KR = 160_000

E3 = [(6.0, 0.50), (7.5, 1.00), (16.0, 3.80)]

BLA     = "#1f4e79"
LJUSBLA = "#5b8db8"
GRA     = "#8c8c8c"
ORANGE  = "#c8722a"
ROD     = "#a33b32"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 11,
    "axes.edgecolor": "#cccccc",
    "axes.linewidth": 0.8,
    "figure.facecolor": "white",
    "axes.facecolor": "white",
})


def kr(x, pos=None):
    return f"{x:,.0f}".replace(",", " ")


def komma(x, d=2):
    return f"{x:.{d}f}".replace(".", ",")


freya_krnm     = (SEGEL_KR/10 + NM_MOTOR*FREYA_LNM*DIESEL) / NM_AR
freya_med_krnm = (SEGEL_KR/8  + NM_MOTOR*FREYA_LNM*DIESEL) / NM_AR
freya_mot_krnm = FREYA_LNM * DIESEL

# ================================================================ GRAF 1
alternativ = [
    ("Elling E3\n16 knop",               3.80 * DIESEL,                                          ROD),
    ("Elling E3\n7,5 knop",              1.00 * DIESEL,                                          "#c15a50"),
    ("45' segelbåt\n(Hydra Net)",        (SEGEL45_KR/10 + NM_MOTOR*FREYA_LNM*DIESEL*1.25)/NM_AR, ORANGE),
    ("Elling E3\n6 knop",                0.50 * DIESEL,                                          "#d99a94"),
    ("Freya\nenbart för motor",          freya_mot_krnm,                                         GRA),
    ("Freya seglad\n(Medelhavet, 8 år)", freya_med_krnm,                                         LJUSBLA),
    ("Freya seglad\n(10 år)",            freya_krnm,                                             BLA),
]

fig, ax = plt.subplots(figsize=(9, 6.4))
namn   = [a[0] for a in alternativ]
varden = [a[1] for a in alternativ]
farger = [a[2] for a in alternativ]

bars = ax.barh(namn, varden, color=farger, height=0.6)
for b, v in zip(bars, varden):
    ax.text(v + 1.0, b.get_y() + b.get_height()/2, f"{komma(v)} kr",
            va="center", ha="left", fontsize=11, fontweight="bold", color="#333333")

ax.set_xlabel("Framdrivningskostnad, kronor per sjömil")
ax.set_xlim(0, max(varden) * 1.18)
ax.set_title("Vad kostar en sjömil?", fontsize=15, fontweight="bold", loc="left", pad=14)
ax.text(0, 1.032,
        "2 250 NM per år · diesel 20 kr/l · segel avskrivna över sin formmässiga livslängd",
        transform=ax.transAxes, fontsize=9.5, color="#666666")
ax.spines[["top", "right", "left"]].set_visible(False)
ax.tick_params(axis="y", length=0)
ax.grid(axis="x", color="#eeeeee", zorder=0)
ax.set_axisbelow(True)
fig.tight_layout()
fig.savefig(f"{OUT}/kostnad_per_sjomil.png", dpi=160, bbox_inches="tight")
plt.close(fig)


# ================================================================ GRAF 2
ar = np.arange(0, 11)
freya_segel = (SEGEL_KR/10 + NM_MOTOR*FREYA_LNM*DIESEL) * ar
freya_med   = (SEGEL_KR/8  + NM_MOTOR*FREYA_LNM*DIESEL) * ar
freya_motor = (NM_AR * FREYA_LNM * DIESEL) * ar
e3_6        = (NM_AR * 0.50 * DIESEL) * ar
e3_75       = (NM_AR * 1.00 * DIESEL) * ar

fig, ax = plt.subplots(figsize=(9, 5.6))
ax.plot(ar, e3_75,       color=ROD,       lw=2.4, label="Elling E3 vid 7,5 knop")
ax.plot(ar, e3_6,        color="#d99a94", lw=2.4, label="Elling E3 vid 6 knop")
ax.plot(ar, freya_motor, color=GRA,       lw=2.0, ls=":",  label="Freya, enbart för motor")
ax.plot(ar, freya_med,   color=LJUSBLA,   lw=2.4, ls="--", label="Freya seglad, segel byts efter 8 år")
ax.plot(ar, freya_segel, color=BLA,       lw=2.8, label="Freya seglad, segel byts efter 10 år")

for y, f in [(e3_75, ROD), (e3_6, "#c48c86"), (freya_motor, GRA),
             (freya_med, LJUSBLA), (freya_segel, BLA)]:
    ax.annotate(f"{kr(y[-1])} kr", xy=(10, y[-1]), xytext=(6, 0),
                textcoords="offset points", va="center", fontsize=10,
                fontweight="bold", color=f)

ax.set_xlabel("År")
ax.set_ylabel("Ackumulerad framdrivningskostnad, kronor")
ax.set_title("Tio år, 22 500 sjömil", fontsize=15, fontweight="bold", loc="left", pad=14)
ax.text(0, 1.032, "Endast framdrivning: segelgarderob och diesel. Inget annat.",
        transform=ax.transAxes, fontsize=9.5, color="#666666")
ax.set_xlim(0, 11.9)
ax.set_ylim(0, 490_000)
ax.yaxis.set_major_formatter(FuncFormatter(kr))
ax.spines[["top", "right"]].set_visible(False)
ax.grid(color="#eeeeee")
ax.set_axisbelow(True)
ax.legend(frameon=False, loc="upper left", fontsize=10)
fig.tight_layout()
fig.savefig(f"{OUT}/kostnad_tio_ar.png", dpi=160, bbox_inches="tight")
plt.close(fig)


# ================================================================ GRAF 3
kn  = np.array([p[0] for p in E3])
lnm = np.array([p[1] for p in E3])
f   = PchipInterpolator(kn, lnm)
x   = np.linspace(6.0, 16.0, 400)
y   = f(x) * DIESEL

fig, ax = plt.subplots(figsize=(9, 5.8))
ax.plot(x, y, color=ROD, lw=2.8, label="Elling E3, kr/NM")
ax.axhline(freya_krnm, color=BLA, lw=2.2,
           label=f"Freya seglad: {komma(freya_krnm)} kr/NM")
ax.axhline(freya_med_krnm, color=LJUSBLA, lw=1.6, ls="--",
           label=f"Freya seglad, medelhavsslitage: {komma(freya_med_krnm)} kr/NM")
ax.plot([7.1], [freya_mot_krnm], "D", color=GRA, ms=8, zorder=6,
        label=f"Freya för motor, 7,1 kn: {komma(freya_mot_krnm)} kr/NM")
ax.annotate("Freya för motor\n7,1 knop · 0,469 l/NM", xy=(7.1, freya_mot_krnm),
            xytext=(16, -34), textcoords="offset points", fontsize=9.5,
            color="#5a5a5a", linespacing=1.35,
            arrowprops=dict(arrowstyle="-", color="#9a9a9a", lw=1))

etiketter = [
    (6.0,  0.50, "6 knop · 0,5 l/NM\n10 kr/NM",   (6, 26)),
    (7.5,  1.00, "7,5 knop · 1,0 l/NM\n20 kr/NM", (12, 16)),
    (16.0, 3.80, "16 knop · 3,8 l/NM\n76 kr/NM",  (-122, -30)),
]
for kx, kl, txt, off in etiketter:
    ax.plot([kx], [kl*DIESEL], "o", color=ROD, ms=8, zorder=5)
    ax.annotate(txt, xy=(kx, kl*DIESEL), xytext=off, textcoords="offset points",
                fontsize=9.5, color="#8a2f28", linespacing=1.35)

ax.set_xlabel("Elling E3, fart genom vattnet (knop)")
ax.set_ylabel("Kronor per sjömil")
ax.set_title("Samma båt, sju gånger priset", fontsize=15, fontweight="bold",
             loc="left", pad=14)
ax.text(0, 1.032,
        "Freyas linjer är vågräta: seglen kostar lika mycket oavsett hur fort det går.",
        transform=ax.transAxes, fontsize=9.5, color="#666666")
ax.set_xlim(5.6, 16.9)
ax.set_ylim(-3, 88)
ax.spines[["top", "right"]].set_visible(False)
ax.grid(color="#eeeeee")
ax.set_axisbelow(True)
ax.legend(frameon=False, loc="lower right", fontsize=10)
fig.tight_layout()
fig.savefig(f"{OUT}/elling_fart.png", dpi=160, bbox_inches="tight")
plt.close(fig)

if os.path.exists(f"{OUT}/motorbat_kanslighet.png"):
    os.remove(f"{OUT}/motorbat_kanslighet.png")

print(f"Freya seglad (10 ar segel)  : {freya_krnm:5.2f} kr/NM  {freya_krnm*NM_AR:9,.0f} kr/ar")
print(f"Freya seglad (8 ar, Medel.) : {freya_med_krnm:5.2f} kr/NM  {freya_med_krnm*NM_AR:9,.0f} kr/ar")
print(f"Freya enbart motor          : {freya_mot_krnm:5.2f} kr/NM  {freya_mot_krnm*NM_AR:9,.0f} kr/ar")
print()
for k, l in E3:
    print(f"Elling E3 @ {k:4.1f} kn ({l:.2f} l/NM): {l*DIESEL:5.2f} kr/NM  {l*DIESEL*NM_AR:9,.0f} kr/ar")
print()
d = 10.0 - freya_krnm
print(f"Diff Freya seglad vs E3 @6kn: {d:.2f} kr/NM = {d*NM_AR:,.0f} kr/ar = {d*NM_AR*10:,.0f} kr pa 10 ar")
print(f"Effektivitet per ton: Freya {FREYA_LNM/10:.4f} l/ton-NM, E3 {0.50/15:.4f} l/ton-NM")
print(f"E3 forbrukning per timme @6kn: {0.50*6:.1f} l/h. Freya @7.1kn: {FREYA_LNM*7.1:.2f} l/h")
