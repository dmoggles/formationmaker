import streamlit as st
from mplsoccer.dimensions import FormationHelper
from vizzes.pitch import draw_pitch
from data import get_all_players
from functools import partial
import numpy as np
from mplsoccer.dimensions import FormationHelper


def name_formatter(payload):
    if not payload:
        return ""
    return f"{payload['player'].title()} - {payload['squad'].replace('_',' ').title()}"


def update_name_text_field(position):
    value = st.session_state.get(f"{position}_name_selection")
    if value:
        st.session_state[f"{position}_num"] = value["squad_number"]
        st.session_state[f"{position}_name"] = value["player"].title()
    else:
        st.session_state[f"{position}_num"] = 1
        st.session_state[f"{position}_name"] = ""


st.set_page_config(layout="wide")

player_df = get_all_players()
selection_df = player_df.drop_duplicates(subset=["player_id", "player", "squad"])


col1, col2 = st.columns(2)
formation = st.session_state.get("formation", "4231")
positions = FormationHelper.get_formation(formation)
pitch, formation_axes = draw_pitch(
    primary_shirt_colour=st.session_state.get("primary_colour", "#0000FF"),
    secondary_shirt_colour=st.session_state.get("secondary_colour", "#FFFFFF"),
    formation=st.session_state.get("formation", "4231"),
    number_dict={pos[0]: st.session_state.get(f"{pos[0]}_num", 1) for pos in positions},
    name_dict={pos[0]: st.session_state.get(f"{pos[0]}_name", "") for pos in positions},
)


with col1:
    col3, col4, col5 = st.columns(3)
    with col3:
        formation = st.selectbox("Formation", options=FormationHelper.formations, key="formation")
    with col4:
        primary_colour = st.color_picker("Primary Colour", "#0000FF", key="primary_colour")
    with col5:
        secondary_colour = st.color_picker("Secondary Colour", "#FFFFFF", key="secondary_colour")
    for i, pos in enumerate(formation_axes):
        with st.container():
            col2a, col2b, col2c, col2d = st.columns([1, 1, 3, 3])

            with col2a:
                st.write(pos)
            with col2b:
                st.number_input("Num", min_value=1, max_value=99, step=1, key=f"{pos}_num")
            with col2c:
                st.selectbox(
                    "Name",
                    options=[None] + sorted(selection_df.to_records(index=False), key=lambda x: x["player"]),
                    key=f"{pos}_name_selection",
                    format_func=name_formatter,
                    on_change=partial(update_name_text_field, position=pos),
                )
            with col2d:
                st.text_input("Or Type Name Here", key=f"{pos}_name")


with col2:
    st.pyplot(pitch)
