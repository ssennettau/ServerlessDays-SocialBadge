import io

from PIL import Image, ImageDraw, ImageFont, ImageOps

def build_badge(in_headshot, in_name, in_title) -> str:
    # Get the base images
    bg = Image.open("template.jpg")
    headshot = Image.open(io.BytesIO(in_headshot))
    headshot = ImageOps.fit(headshot, (500,500))

    # Compose the Working Image
    img = Image.new("RGBA", (bg.size[0], bg.size[1]))
    img.paste(bg)
    img.paste(headshot, (int( bg.size[0] / 2 - headshot.size[0] / 2 ), 100))

    # Add text
    font_regular = ImageFont.truetype(
        "./fonts/OpenSans-Regular.ttf",
        48
    )
    font_bold = ImageFont.truetype(
        "./fonts/OpenSans-Bold.ttf",
        60
    )

    text_layer = Image.new(
        "RGBA", 
        (img.size[0],img.size[1]),
        (255,255,255,0)
    )
    text_draw = ImageDraw.Draw(text_layer)

    text_draw.text(
        (int(img.size[0] / 2), 675), 
        in_name, 
        font=font_bold, 
        fill=(255,255,255,255), 
        align="center",
        anchor="mm",
    )
    text_draw.text(
        (int(img.size[0] / 2), 750),
        in_title,
        font=font_regular, 
        fill=(255,255,255,255),
        align="center",
        anchor="mm",
    )

    img = Image.alpha_composite(img,text_layer)

    # Output the result

    data = io.BytesIO()
    img.save(data, format="PNG")

    return data.getvalue()

if __name__ == "__main__":
    badge = build_badge("head.jpg",
                "Bilbo X. Baggins", 
                "Chief Cloud Architect at Hobbiton")
    print(badge[:64])
