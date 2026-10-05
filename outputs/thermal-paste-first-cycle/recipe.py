#!/usr/bin/env python3
"""Masses to weigh for one thermal paste batch, and the density it should have with no trapped air.

    python3 recipe.py --filler 40 --fine-share 30            # 40 vol% alumina, 30% of it the fine grade, 25 g batch
    python3 recipe.py --filler 50 --fine-share 0 --batch 30
    python3 recipe.py --table                                 # the control and the four gate extremes

Densities are from the supplier pages and data sheets for the lots listed in README.md.
Change them here if a different lot's data sheet says otherwise.
"""
import argparse

ALUMINA = 3.97  # g/cm3, Atlantic Equipment Engineers data sheet for AL-602
OIL = 0.97      # g/cm3, vendor page for 1000 cSt silicone oil

# name, total filler vol%, share of the alumina that is the fine grade (%)
GATE_SET = [
    ("control", 40, 30),
    ("extreme 1: low loading, coarse only", 30, 0),
    ("extreme 2: high loading, mixed sizes", 55, 30),
    ("extreme 3: fine only", 40, 100),
    ("extreme 4: high loading, coarse only", 50, 0),
]


def batch(filler_pct, fine_share_pct, batch_g):
    phi = filler_pct / 100
    density = phi * ALUMINA + (1 - phi) * OIL  # g/cm3 with no trapped air
    volume = batch_g / density
    alumina = phi * volume * ALUMINA
    fine = alumina * fine_share_pct / 100
    return {
        "oil_g": (1 - phi) * volume * OIL,
        "coarse_g": alumina - fine,
        "fine_g": fine,
        "volume_ml": volume,
        "full_density": density,
    }


def line(name, filler_pct, fine_share_pct, batch_g):
    b = batch(filler_pct, fine_share_pct, batch_g)
    return (f"{name:38s} oil {b['oil_g']:5.2f} g | coarse {b['coarse_g']:5.2f} g | fine {b['fine_g']:5.2f} g"
            f" | {b['volume_ml']:4.1f} mL | density with no air {b['full_density']:.3f} g/cm3")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--filler", type=float, help="total alumina, percent of batch volume")
    p.add_argument("--fine-share", type=float, default=0, help="percent of the alumina that is the fine grade")
    p.add_argument("--batch", type=float, default=25, help="batch mass in grams")
    p.add_argument("--table", action="store_true", help="print the control and the four gate extremes")
    args = p.parse_args()
    if args.table:
        for name, filler, fine in GATE_SET:
            print(line(name, filler, fine, args.batch))
    elif args.filler is not None:
        print(line(f"{args.filler:g} vol%, {args.fine_share:g}% fine", args.filler, args.fine_share, args.batch))
    else:
        p.print_help()


if __name__ == "__main__":
    main()
