import os
import json

import streamlit as st
import openai

#configuring openai - api key
working_dir = os.path.dirname(os.path.abspath(__file__))
config_data = json.load(open(f"{working_dir}/config.json"))

print(config_data)