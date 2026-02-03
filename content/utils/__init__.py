import numpy as np

def hsv_to_rgb_np(hsv):
    h, s, v = hsv.T
    h = h * 6.0
    i = np.floor(h).astype(int)
    f = h - i

    p = v * (1.0 - s)
    q = v * (1.0 - s * f)
    t = v * (1.0 - s * (1.0 - f))

    i = i % 6

    rgb = np.empty((len(h), 3))
    masks = [
        (v, t, p),
        (q, v, p),
        (p, v, t),
        (p, q, v),
        (t, p, v),
        (v, p, q),
    ]

    for k in range(6):
        idx = i == k
        rgb[idx] = np.stack(masks[k], axis=1)[idx]

    return rgb


def visually_distinct_colors(n, seed=None):
    rng = np.random.default_rng(seed)

    hues = np.linspace(0, 1, n, endpoint=False)
    rng.shuffle(hues)

    sats = rng.uniform(0.6, 0.9, n)
    vals = rng.uniform(0.7, 0.9, n)

    hsv = np.stack([hues, sats, vals], axis=1)
    return hsv_to_rgb_np(hsv)
