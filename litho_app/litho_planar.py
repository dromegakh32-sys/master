import numpy as np
import trimesh
from PIL import Image, ImageOps, ImageFilter


def enhance_image(img):
    img = ImageOps.autocontrast(img)
    img = img.filter(ImageFilter.UnsharpMask(radius=2, percent=180, threshold=3))
    return img


def non_linear_mapping(pixels):
    # ضغط قوي للظلال
    gamma_dark = 0.6
    gamma_light = 1.4

    dark_boost = np.power(pixels, gamma_dark)
    light_compress = np.power(dark_boost, gamma_light)

    return np.clip(light_compress, 0, 1)


def generate_planar_lithophane(
    image_path,
    width_mm,
    height_mm,
    min_thickness,
    max_thickness,
    base_thickness,
    resolution_mm
):
    img = Image.open(image_path).convert("L")
    img = enhance_image(img)

    target_w = int(width_mm / resolution_mm)
    target_h = int(height_mm / resolution_mm)

    img = img.resize((target_w, target_h), Image.LANCZOS)

    pixels = np.asarray(img, dtype=np.float32) / 255.0

    pixels = non_linear_mapping(pixels)

    pixels = 1.0 - pixels  # نافــر

    heights = min_thickness + pixels * (max_thickness - min_thickness)

    h, w = heights.shape

    sx = width_mm / (w - 1)
    sy = height_mm / (h - 1)

    vertices = []
    faces = []

    def v(x, y, z):
        vertices.append([x, y, z])
        return len(vertices) - 1

    top = np.zeros((h, w), dtype=int)
    base = np.zeros((h, w), dtype=int)

    for y in range(h):
        for x in range(w):
            top[y, x] = v(
                x * sx,
                (h - y) * sy,
                base_thickness + heights[y, x]
            )

    for y in range(h):
        for x in range(w):
            base[y, x] = v(
                x * sx,
                (h - y) * sy,
                0
            )

    for y in range(h - 1):
        for x in range(w - 1):
            faces += [
                [top[y, x], top[y, x + 1], top[y + 1, x]],
                [top[y + 1, x], top[y, x + 1], top[y + 1, x + 1]],
                [base[y + 1, x], base[y, x + 1], base[y, x]],
                [base[y + 1, x + 1], base[y, x + 1], base[y + 1, x]],
            ]

    for y in range(h - 1):
        faces += [
            [base[y, 0], top[y, 0], top[y + 1, 0]],
            [base[y, 0], top[y + 1, 0], base[y + 1, 0]],
            [top[y, w - 1], base[y, w - 1], base[y + 1, w - 1]],
            [top[y, w - 1], base[y + 1, w - 1], top[y + 1, w - 1]],
        ]

    for x in range(w - 1):
        faces += [
            [top[0, x], base[0, x], base[0, x + 1]],
            [top[0, x], base[0, x + 1], top[0, x + 1]],
            [base[h - 1, x], top[h - 1, x], top[h - 1, x + 1]],
            [base[h - 1, x], top[h - 1, x + 1], base[h - 1, x + 1]],
        ]

    return trimesh.Trimesh(vertices=vertices, faces=faces, process=True)
