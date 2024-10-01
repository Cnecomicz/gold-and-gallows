import pygame

import gng.global_constants as gc


class TextBundle:
    def __init__(
        self, text, font=gc.BASIC_FONT, color=gc.TEXT_COLOR, font_size=gc.FONT_SIZE
    ):
        self.text = text
        self.font = font
        self.color = color
        self.font_size = font_size


def bdlr(text, font=gc.BASIC_FONT, color=gc.TEXT_COLOR):
    # Syntactic sugar for creating the TextBundle class. Pronounced
    # "bundler." Does nothing, but is fewer characters, which makes a
    # difference when it comes to dialogue trees especially. In dialogue
    # tree data files, use "from text_handler import *" to save on
    # writing "th" each time too.
    return TextBundle(text=text, font=font, color=color)


def make_text(DISPLAY_SURF, bgcolor, left, top, text_width, *text_bundles):
    # NOTE: The newline character "\n" does work, but it _must_ be
    # separated with spaces on both sides, or at the end of your text
    # string.
    line = 0
    ending_position = left
    for text_bundle in text_bundles:
        words = text_bundle.text.split(" ")
        current_line = ""
        for word in words:
            textSurf = text_bundle.font.render(
                current_line, True, text_bundle.color, bgcolor
            )
            nextSurf = text_bundle.font.render(
                current_line + word + " ", True, text_bundle.color, bgcolor
            )
            if (
                nextSurf.get_width() + (ending_position - left) <= text_width
            ) and word != "\n":
                current_line += word + " "
            else:
                textRect = textSurf.get_rect()
                textRect.topleft = (
                    ending_position,
                    top + line * text_bundle.font.get_height(),
                )
                ending_position = left
                DISPLAY_SURF.blit(textSurf, textRect)
                if word != "\n":
                    current_line = "" + word + " "
                else:
                    current_line = ""
                line += 1
        # Print the final line.
        if current_line != " ":  # Don't print lone spaces after \n.
            textSurf = text_bundle.font.render(
                current_line, True, text_bundle.color, bgcolor
            )
            textRect = textSurf.get_rect()
            textRect.topleft = (
                ending_position,
                top + line * text_bundle.font.get_height(),
            )
            ending_position = textRect.right
            DISPLAY_SURF.blit(textSurf, textRect)


def make_hovered_option(DISPLAY_SURF, bgcolor, left, top, text_width, text_bundle):
    hovered_symbol = "> "
    hoveredSurf = text_bundle.font.render(
        hovered_symbol, True, text_bundle.color, bgcolor
    )
    hovered_width = hoveredSurf.get_width()
    make_text(
        DISPLAY_SURF,
        bgcolor,
        left - hovered_width,
        top,
        hovered_width,
        bdlr(hovered_symbol, text_bundle.font, text_bundle.color),
    )
    make_text(DISPLAY_SURF, bgcolor, left, top, text_width, text_bundle)


def get_number_of_lines(left, text_width, *text_bundles):
    # TODO: lot of overlap with make_text, maybe DRY
    lines = 1
    ending_position = left
    for text_bundle in text_bundles:
        words = text_bundle.text.split(" ")
        current_line = ""
        for word in words:
            textSurf = text_bundle.font.render(
                current_line, True, text_bundle.color  # , bgcolor
            )
            nextSurf = text_bundle.font.render(
                current_line + word + " ", True, text_bundle.color  # , bgcolor
            )
            if (
                nextSurf.get_width() + (ending_position - left) <= text_width
            ) and word != "\n":
                current_line += word + " "
            else:
                ending_position = left
                if word != "\n":
                    current_line = "" + word + " "
                else:
                    current_line = ""
                lines += 1
    return lines


def make_all_options(
    DISPLAY_SURF, bgcolor, left, top, text_width, cursor_index, *text_bundles
):
    line = 0
    for option in text_bundles:
        if option == text_bundles[cursor_index]:
            make_hovered_option(
                DISPLAY_SURF,
                bgcolor,
                left,
                top + line * option.font.get_height(),
                text_width,
                option,
            )
        else:
            make_text(
                DISPLAY_SURF,
                bgcolor,
                left,
                top + line * option.font.get_height(),
                text_width,
                option,
            )
        line += get_number_of_lines(left, text_width, option)
