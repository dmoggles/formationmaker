import numpy as np


def autoscale_font(fig, ax, shirt_height):
    fig_size_inches = fig.get_size_inches()
    ax_pos = ax.get_position()
    ax_width = ax_pos.width
    ax_height = ax_pos.height
    ax_size_inches = (ax_width * fig_size_inches[0], ax_height * fig_size_inches[1])
    shirt_height_inches = ax_size_inches[1] * shirt_height / (ax.get_ylim()[1] - ax.get_ylim()[0])
    return shirt_height_inches


def draw_football_shirt(number, color1, color2, x, y, shirt_height, ax, fig, z=1):
    shirt_width = shirt_height / 1.4
    # shirt body
    ax.fill(
        [x, x + shirt_width, x + shirt_width, x],
        [y, y, y + shirt_height, y + shirt_height],
        color1,
        zorder=z,
        lw=1,
        ec=color1,
    )

    shadow_width = 0.025 * shirt_width
    # ax.fill(
    #    [
    #        x-shadow_width, x+shirt_width+shadow_width,x+shirt_width+shadow_width, x-shadow_width
    #    ],
    #    [
    #        y-shadow_width, y-shadow_width, y+shirt_height+shadow_width, y+shirt_height+shadow_width
    #    ]
    #    , color2,
    #    zorder=z-0.3
    # )

    sleeve_width = shirt_height / 4
    sleeve_length = shirt_width * 0.75
    # left sleeve
    ax.fill(
        [x, x - sleeve_length * np.sin(45), x - sleeve_length * np.sin(45) + sleeve_width * np.sin(45), x],
        [
            y + shirt_height,
            y + shirt_height - sleeve_length * np.sin(45),
            y + shirt_height - sleeve_length * np.sin(45) - sleeve_width * np.sin(45),
            y + shirt_height - sleeve_length * np.sin(45),
        ],
        color1,
        zorder=z - 0.2,
        lw=1,
        ec=color1,
    )
    # right sleeve
    ax.fill(
        [
            x + shirt_width,
            x + shirt_width + sleeve_length * np.sin(45),
            x + shirt_width + sleeve_length * np.sin(45) - sleeve_width * np.sin(45),
            x + shirt_width,
        ],
        [
            y + shirt_height,
            y + shirt_height - sleeve_length * np.sin(45),
            y + shirt_height - sleeve_length * np.sin(45) - sleeve_width * np.sin(45),
            y + shirt_height - sleeve_length * np.sin(45),
        ],
        color1,
        zorder=z - 0.2,
        lw=1,
        ec=color1,
    )
    scale = autoscale_font(fig, ax, shirt_height)

    font_size = scale / 0.77 * 20
    ax.text(x + shirt_width / 2, y + shirt_height / 2, number, color=color2, va="center", ha="center", size=font_size)
    background_color = ax.get_facecolor()
    ax.fill(
        [
            x + shirt_width / 2 - shirt_height / 7 / np.sqrt(2),
            x + shirt_width / 2 + shirt_height / 7 / np.sqrt(2),
            x + shirt_width / 2,
        ],
        [
            y + shirt_height,
            y + shirt_height,
            y + shirt_height - shirt_height / 7,
        ],
        color=tuple(list(background_color[:3]) + [1]),
        edgecolor=tuple(list(background_color[:3]) + [1]),
        zorder=z + 1,
    )
    ax.plot(
        [
            x + shirt_width / 2 - shirt_height / 7 / np.sqrt(2),
            x + shirt_width / 2,
            x + shirt_width / 2 + shirt_height / 7 / np.sqrt(2),
        ],
        [y + shirt_height, y + shirt_height - shirt_height / 7, y + shirt_height],
        lw=2,
        ls="solid",
        color=color2,
    )
    ax.plot(
        [
            x + shirt_width + sleeve_length * np.sin(45),
            x + shirt_width + sleeve_length * np.sin(45) - sleeve_width * np.sin(45),
        ],
        [
            y + shirt_height - sleeve_length * np.sin(45),
            y + shirt_height - sleeve_length * np.sin(45) - sleeve_width * np.sin(45),
        ],
        color=color2,
        lw=4 * (scale / 1.54),
    )
    ax.plot(
        [
            x - sleeve_length * np.sin(45),
            x - sleeve_length * np.sin(45) + sleeve_width * np.sin(45),
        ],
        [
            y + shirt_height - sleeve_length * np.sin(45),
            y + shirt_height - sleeve_length * np.sin(45) - sleeve_width * np.sin(45),
        ],
        color=color2,
        lw=4 * (scale / 1.54),
    )
