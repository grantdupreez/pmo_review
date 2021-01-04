import os
import streamlit as st


def st_file_selector(st_placeholder, path='.', label='Please, select a file/folder...'):
    # get base path (directory)
    base_path = '.' if path is None or path is '' else path
    base_path = base_path if os.path.isdir(
        base_path) else os.path.dirname(base_path)
    base_path = '.' if base_path is None or base_path is '' else base_path
    # list files in base path directory
    files = os.listdir(base_path)
    if base_path is not '.':
        files.insert(0, '..')
    files.insert(0, '.')
    selected_file = st_placeholder.selectbox(
        label=label, options=files, key=base_path)
    selected_path = os.path.normpath(os.path.join(base_path, selected_file))
    if selected_file is '.':
        return selected_path
    if os.path.isdir(selected_path):
        selected_path = st_file_selector(st_placeholder=st_placeholder,
                                         path=selected_path, label=label)
    return selected_path
