from mplsoccer import VerticalPitch
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from vizzes.util import draw_football_shirt


def get_ax_size(ax, fig):
    bbox = ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    width, height = bbox.width, bbox.height
    width *= fig.dpi
    height *= fig.dpi
    return width, height


def initialize_pitch(pitch_color="grass"):
    pitch = VerticalPitch(pitch_type="opta", linewidth=1, pitch_color=pitch_color)
    fig = Figure(figsize=(8, 12))
    ax = fig.subplots(1, 1)
    pitch.draw(ax)
    return pitch, fig, ax


def draw_shirts(pitch: VerticalPitch, ax, fig, formation, primary_colour, secondary_colour, numbers_dict, name_dict):
    width, height = get_ax_size(ax, fig)
    size = 10
    formation_axes = pitch.inset_formation_axes(formation=formation, width=size * height / width, length=size, ax=ax)
    for i, (pos, f_ax) in enumerate(formation_axes.items()):
        f_ax: Axes = f_ax
        f_ax.set_ylim(0, 1)
        number = numbers_dict.get(pos, i)
        f_ax.axis("off")
        draw_football_shirt(
            number,
            primary_colour,
            secondary_colour,
            0,
            0.2,
            0.8,
            f_ax,
            fig,
        )
        if pos in name_dict:
            f_ax.text(
                (f_ax.get_xlim()[1] + f_ax.get_xlim()[0]) / 2,
                0.15,
                name_dict[pos],
                ha="center",
                va="top",
                size=9,
                zorder=10,
            )
    return formation_axes


def draw_pitch(primary_shirt_colour, secondary_shirt_colour, formation, number_dict, name_dict):
    print(number_dict)
    pitch, fig, ax = initialize_pitch()
    formation_axes = draw_shirts(
        pitch, ax, fig, formation, primary_shirt_colour, secondary_shirt_colour, number_dict, name_dict
    )
    return fig, list(formation_axes.keys())
