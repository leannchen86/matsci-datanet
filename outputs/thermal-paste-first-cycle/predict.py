#!/usr/bin/env python3
"""Fixed formulas for the experiments in EXPERIMENTS.md. Standard library only.

  predict.py loading --powder 12.00 --oil 2.41
  predict.py blend --lc 0.55 --lf 0.40
  predict.py squeeze --plate 80 --volume 0.5

Inputs are measured on this bench; the output is logged before the run it predicts.
"""
import argparse
from math import pi

ALUMINA = 3.97   # g/cm3, assumed particle density
OIL = 0.97       # g/cm3
VISCOSITY = 0.97     # Pa.s, label value for 1000 cSt oil
SURFACE_TENSION = 0.0213  # N/m, silicone oil


def loading(powder, oil):
    """Share of the paste volume that is powder."""
    vp, vo = powder / ALUMINA, oil / OIL
    return vp / (vp + vo)


def oil_for(powder, load):
    """Grams of oil that bring this much powder to this loading."""
    return powder / ALUMINA * (1 - load) / load * OIL


def no_gain(x, lc, lf):
    """Each powder keeps its own oil demand; the demands add."""
    return 1 / ((1 - x) / lc + x / lf)


def gap_filling(x, lc, lf, r):
    """Fines sit in the gaps between coarse grains, less two crowding effects.

    Linear packing model with the coefficients of arXiv 1006.4215; r is the
    coarse-to-fine size ratio. No number is fitted to the outcome.
    """
    a = (1 - (1 - 1 / r) ** 1.13) ** 0.57
    b = (1 - (1 - 1 / r) ** 1.79) ** 0.82
    coarse_led = lc / (1 - x * (1 - a * lc / lf))
    fine_led = lf / (1 - (1 - x) * (1 - lf + b * (lf - lf / lc)))
    return min(coarse_led, fine_led)


def squeeze(force, volume, seconds, capillary):
    """Diameter (mm) of a drop of oil squeezed between flat plates.

    Stefan's law for a fixed volume; with capillary=True the pull of the oil
    film (2 x surface tension x volume / gap^2) is added to the load.
    """
    if not capillary:
        r8 = 8 * force * volume ** 2 * seconds / (3 * pi ** 3 * VISCOSITY)
        return 2000 * r8 ** 0.125
    gap, t = 2e-3, 0.0
    while t < seconds:
        pull = force + 2 * SURFACE_TENSION * volume / gap ** 2
        rate = 2 * pi * gap ** 5 * pull / (3 * VISCOSITY * volume ** 2)
        dt = min(0.002 * gap / rate, seconds - t)
        gap -= rate * dt
        t += dt
    return 2000 * (volume / (pi * gap)) ** 0.5


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("loading", help="loading from weighed powder and oil")
    s.add_argument("--powder", type=float, required=True, help="grams of powder in the cup")
    s.add_argument("--oil", type=float, required=True, help="grams of oil in the cup")

    s = sub.add_parser("blend", help="predicted mixing limit of coarse-fine blends")
    s.add_argument("--lc", type=float, required=True, help="measured limit of coarse alone")
    s.add_argument("--lf", type=float, required=True, help="measured limit of fine alone")
    s.add_argument("--ratio", type=float, default=8.2, help="coarse-to-fine size ratio (label: 45/5.5)")
    s.add_argument("--powder", type=float, default=12.0, help="grams of powder per cup")

    s = sub.add_parser("squeeze", help="oil spread between plates, for the rig check")
    s.add_argument("--plate", type=float, required=True, help="grams pressing on the oil (plate, plus weight if used)")
    s.add_argument("--volume", type=float, default=0.5, help="mL of oil")
    s.add_argument("--times", type=float, nargs="+", default=[30, 60, 300], help="seconds")

    args = p.parse_args()
    if args.cmd == "loading":
        print(f"loading {loading(args.powder, args.oil):.4f}")
    elif args.cmd == "blend":
        print(f"inputs: coarse {args.lc}, fine {args.lf}, size ratio {args.ratio}")
        print("fines share   no-gain   gap-filling   oil at each on "
              f"{args.powder:g} g powder")
        for x in (0.15, 0.30, 0.50, 0.70):
            n, g = no_gain(x, args.lc, args.lf), gap_filling(x, args.lc, args.lf, args.ratio)
            print(f"   {x:.2f}        {n:.3f}      {g:.3f}       "
                  f"{oil_for(args.powder, n):.2f} g / {oil_for(args.powder, g):.2f} g")
        n, g = no_gain(0.30, args.lc, args.lf), gap_filling(0.30, args.lc, args.lf, args.ratio)
        print(f"G = (measured limit at 0.30 - {n:.3f}) / {g - n:.3f}")
    else:
        force, volume = args.plate / 1000 * 9.81, args.volume * 1e-6
        print("seconds   plain viscous   with capillary pull   (diameter, mm)")
        for t in args.times:
            print(f"  {t:5g}      {squeeze(force, volume, t, False):5.1f}            "
                  f"{squeeze(force, volume, t, True):5.1f}")


if __name__ == "__main__":
    main()
