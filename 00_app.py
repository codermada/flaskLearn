from flask import Flask, request

from flask_babel import Babel, gettext

# babel is a library that helps with internationalization (i18n) and localization (l10n) in Python applications. It provides tools for handling translations, formatting dates, numbers, and more.
def get_local():
    """This function is used to determine the best match for the user's preferred languages based on the Accept-Language header in the HTTP request. It checks the languages specified in the header against a list of supported languages and returns the best match."""
    return request.accept_languages.best_match(
        ["fr_FR", "en_US", "es_ES", "de_DE"]
    )

app = Flask(__name__)

# The Babel instance is created and associated with the Flask application. The locale_selector parameter is set to the get_local function, which will be called to determine the user's preferred language for each request.
babel = Babel(app, locale_selector=get_local)

# ./translations/fr/LC_MESSAGES/messages.po
###################
# msgid ""
# msgstr ""
# "Language: fr\n"

# msgid "hello"
# msgstr "bonjour"
###################
# pybabel compile -d translations

# The BABEL_TRANSLATION_DIRECTORIES configuration variable is set to "translations", which tells Babel where to find the translation files. These files are typically organized in a directory structure that includes the language code (e.g., fr for French) and the LC_MESSAGES subdirectory, which contains the .po files with the translations.
app.config["BABEL_TRANSLATION_DIRECTORIES"] = "translations"


@app.route('/')
def index():
    return gettext("hello")
    # return {
    #     "accept_languages": str(request.accept_languages),
    #     "selected": get_local()
    # }


if __name__ == '__main__':
    app.run(debug=True)
