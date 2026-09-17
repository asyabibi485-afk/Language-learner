# Streamlit ImportError fix

The app now imports language data from `tonguetie_language_data.py` instead of
using the generic module name `language_data`. A compatibility `language_data.py`
wrapper is also included.

Upload the **entire repository contents** to the GitHub repository root and
make sure Streamlit Cloud's Main file is `app.py`. Then reboot/redeploy the app.
