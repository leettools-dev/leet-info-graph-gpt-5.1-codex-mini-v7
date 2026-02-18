from io import BytesIO
from typing import Union

from PIL import Image, ImageDraw, ImageFont

from .spec import InfographicSpec


def render_spec_to_png(spec: Union[dict, InfographicSpec]) -> bytes:
    if isinstance(spec, InfographicSpec):
        spec_dict = spec.dict()
    else:
        spec_dict = spec

    width = 1200
    height = 675
    bg_color = (20, 24, 82)
    accent = (85, 208, 255)

    image = Image.new("RGB", (width, height), bg_color)
    draw = ImageDraw.Draw(image)

    title_font = ImageFont.load_default()
    body_font = ImageFont.load_default()

    draw.text((40, 40), spec_dict["title"], font=title_font, fill=accent)
    draw.text((40, 80), f"Type: {spec_dict['infographic_type']}", font=body_font, fill=(255, 255, 255))

    y = 140
    for block in spec_dict["layout_blocks"]:
        draw.text((40, y), f"• {block['content']}", font=body_font, fill=(240, 240, 240))
        y += 30
        if y > height - 120:
            y = 140

    citation_y = height - 40
    citation_text = " | ".join([f"[{c['id']}] {c['title']}" for c in spec_dict["citations"]])
    draw.text((40, citation_y), citation_text, font=body_font, fill=(200, 200, 200))

    buffer = BytesIO()
    image.save(buffer, format="PNG")
    return buffer.getvalue()
