#!/usr/bin/env python3
"""Two small calculations for the thermal measurements.

    python3 thermal.py fit 0.01:0.787 0.02:1.200 0.03:1.523
        Thickness (cm) and thermal impedance (C-cm2/W) pairs, as LongWin reports them.
        Prints bulk conductivity from the slope and contact impedance from the intercept.
        The numbers above are LongWin's published grease example and must give 2.72 W/mK and 0.434 C-cm2/W.

    python3 thermal.py mount --hot 52.0 49.6 --cold 37.4 35.1
        One mount on the home rig. Each bar has two thermocouples, 5 mm and 25 mm from its test face.
        --hot is the upper bar (far from the face first, then near the face); --cold is the lower bar (near the face first, then far).
        Prints the heat flow in each bar and the thermal impedance across the gap.

The bar conductivity below is a handbook figure for 6061 aluminium, not a measured value for this bar,
so absolute numbers from the home rig are only trusted after comparison with LongWin on the same samples.
"""
import argparse

BAR_K = 167.0        # W/m-K, handbook value for 6061-T6 aluminium
BAR_SIDE_MM = 25.4   # 1 inch square bar
NEAR_MM = 5.0        # thermocouple nearest the test face
FAR_MM = 25.0        # thermocouple farthest from the test face


def fit(pairs):
    xs = [p[0] for p in pairs]
    ys = [p[1] for p in pairs]
    n = len(pairs)
    mean_x, mean_y = sum(xs) / n, sum(ys) / n
    slope = sum((x - mean_x) * (y - mean_y) for x, y in pairs) / sum((x - mean_x) ** 2 for x in xs)
    intercept = mean_y - slope * mean_x
    conductivity = 100.0 / slope  # slope is C-cm/W; 1/slope is W/cm-C; times 100 gives W/m-K
    return conductivity, intercept


def mount(hot_far, hot_near, cold_near, cold_far):
    area_m2 = (BAR_SIDE_MM / 1000) ** 2
    spacing_m = (FAR_MM - NEAR_MM) / 1000
    grad_hot = (hot_far - hot_near) / spacing_m    # K/m, positive when heat flows toward the gap
    grad_cold = (cold_near - cold_far) / spacing_m
    q_hot = BAR_K * area_m2 * grad_hot             # W
    q_cold = BAR_K * area_m2 * grad_cold
    q = (q_hot + q_cold) / 2
    # Extrapolate each bar's temperature to its test face.
    face_hot = hot_near - grad_hot * NEAR_MM / 1000
    face_cold = cold_near + grad_cold * NEAR_MM / 1000
    area_cm2 = area_m2 * 1e4
    impedance = (face_hot - face_cold) * area_cm2 / q  # C-cm2/W
    return q_hot, q_cold, face_hot, face_cold, impedance


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    f = sub.add_parser("fit", help="conductivity and contact impedance from impedance against thickness")
    f.add_argument("pairs", nargs="+", help="thickness_cm:impedance, at least two")
    m = sub.add_parser("mount", help="heat flow and impedance for one mount on the home rig")
    m.add_argument("--hot", nargs=2, type=float, required=True, metavar=("FAR", "NEAR"))
    m.add_argument("--cold", nargs=2, type=float, required=True, metavar=("NEAR", "FAR"))
    args = p.parse_args()

    if args.cmd == "fit":
        pairs = [tuple(float(v) for v in item.split(":")) for item in args.pairs]
        if len(pairs) < 2:
            p.error("give at least two thickness:impedance pairs")
        conductivity, intercept = fit(pairs)
        print(f"bulk conductivity {conductivity:.2f} W/mK, contact impedance {intercept:.3f} C-cm2/W")
    else:
        q_hot, q_cold, face_hot, face_cold, impedance = mount(*args.hot, *args.cold)
        mismatch = abs(q_hot - q_cold) / ((q_hot + q_cold) / 2) * 100
        print(f"heat flow: upper bar {q_hot:.2f} W, lower bar {q_cold:.2f} W (differ by {mismatch:.0f}%)")
        print(f"face temperatures: hot {face_hot:.2f} C, cold {face_cold:.2f} C")
        print(f"thermal impedance {impedance:.3f} C-cm2/W")


if __name__ == "__main__":
    main()
