"""Compatibility wrapper for TongueTie language data.

The app imports the uniquely named ``tonguetie_language_data`` module to avoid
module-name collisions on Streamlit Cloud. This wrapper keeps the old module
name working for any external code that imports it.
"""
from tonguetie_language_data import LANGUAGES, language_options, POPULAR, PROFICIENCY_LEVELS

__all__ = ["LANGUAGES", "language_options", "POPULAR", "PROFICIENCY_LEVELS"]
