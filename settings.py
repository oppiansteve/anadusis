# -*- coding: utf-8 -*-
# Django settings for social pinax project.

import os
import os.path
import posixpath
import pinax
import socket

PINAX_ROOT = os.path.abspath(os.path.dirname(pinax.__file__))
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

# tells Pinax to use the default theme
PINAX_THEME = 'default'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# tells Pinax to serve media through django.views.static.serve.
SERVE_MEDIA = DEBUG

ADMINS = (
)

# Default admin account and pass
# admin:dewnwerd7

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'    # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3', 'oracle' or 'ado_mssql'.
DATABASE_NAME = os.path.join(PROJECT_ROOT, '.sqlite.db')             # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://www.postgresql.org/docs/8.1/static/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
# although not all variations may be possible on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/London'

# Language code for this installation. All choices can be found here:
# http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
# http://blogs.law.harvard.edu/tech/stories/storyReader$15
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-GB'

SITE_ID = 1
SITE_NAME = "CoLab"

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'site_media', 'media/')

# URL that handles the media served from MEDIA_ROOT.
# Example: "http://media.lawrence.com"
MEDIA_URL = '/site_media/media/'

# Absolute path to the directory that holds static files like app media.
# Example: "/home/media/media.lawrence.com/apps/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'site_media', 'static')

# URL that handles the static files like app media.
# Example: "http://media.lawrence.com"
STATIC_URL = '/site_media/static/'

# Additional directories which hold static files
STATICFILES_DIRS = (
    ('', os.path.join(PROJECT_ROOT, 'media')),
    ('social_project', os.path.join(PROJECT_ROOT, 'media')),
    ('pinax', os.path.join(PINAX_ROOT, 'media', PINAX_THEME, 'pinax')),
    ('bookmarks', os.path.join(PINAX_ROOT, 'media', PINAX_THEME, 'bookmarks'))
)

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = posixpath.join(STATIC_URL, "admin/")

# Make this unique, and don't share it with anybody.
SECRET_KEY = 's)xqnakv4*98b2g58#$p4&1@q6#kck_ho28zu9gz7sawj-d+(v'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django_openid.consumer.SessionConsumer',
    'account.middleware.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'pagination.middleware.PaginationMiddleware',
    'django_sorting.middleware.SortingMiddleware',
    'djangodblog.middleware.DBLogMiddleware',
    'pinax.middleware.security.HideSensistiveFieldsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
)

ROOT_URLCONF = 'urls' # anadusis.urls

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, "templates"),
    os.path.join(PINAX_ROOT, "templates", PINAX_THEME),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    
    "pinax.core.context_processors.pinax_settings",
    
    "notification.context_processors.notification",
    "announcements.context_processors.site_wide_announcements",
    "account.context_processors.account",
    "messages.context_processors.inbox",
    "friends_app.context_processors.invitations",
    "context_processors.combined_inbox_count", #"anadusis.context_processors.combined_inbox_count",
)

COMBINED_INBOX_COUNT_SOURCES = (
    "messages.context_processors.inbox",
    "friends_app.context_processors.invitations",
    "notification.context_processors.notification",
)

INSTALLED_APPS = (
    # included
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.humanize',
    'django.contrib.markup',
    'pinax.templatetags',
    
    # external
    'notification', # must be first
    'django_openid',
    'emailconfirmation',
    'django_extensions',
    'robots',
    'friends',
    'mailer',
    'messages',
    'announcements',
    'oembed',
    'djangodblog',
    'pagination',
#    'gravatar',
    'threadedcomments',
    'threadedcomments_extras',
    'wiki',
    'timezones',
    'voting',
    'voting_extras',
    'tagging',
    'bookmarks',
    'blog',
    'ajax_validation',
    'photologue',
    'avatar',
    'flag',
    'microblogging',
    'locations',
    'uni_form',
    'django_sorting',
    'django_markup',
    'staticfiles',
    'debug_toolbar',
    
    # internal (for now)
    'analytics',
    'profiles',
    'account',
    'signup_codes',
    'tribes',
    'tasks',
    'projects',
    'photos',
    'tag_app',
    'tagging_utils',
    'topics',
    'groups',
    'basic_groups',

    'chronograph', # see lib/django-chronograph (originally git://github.com/t11e/django-chronograph.git)
    
    'tinymce', # http://django-tinymce.googlecode.com/svn/trunk/docs/.build/html/index.html
    
    'videostream', # http://cloud27.com/projects/project/djangovideo/

	'django_extensions', # http://code.google.com/p/django-command-extensions/
	
    # build tools
    'build',
    'south', # http://south.aeracode.org
)

# fixture
FIXTURE_DIRS = (
    os.path.join(PROJECT_ROOT, "fixtures"),
)

ABSOLUTE_URL_OVERRIDES = {
    "auth.user": lambda o: "/profiles/profile/%s/" % o.username,
}

MARKUP_FILTER_FALLBACK = 'none'
MARKUP_CHOICES = (
    ('restructuredtext', u'reStructuredText'),
    ('textile', u'Textile'),
    ('markdown', u'Markdown'),
    ('creole', u'Creole'),
)
WIKI_MARKUP_CHOICES = MARKUP_CHOICES

AUTH_PROFILE_MODULE = 'profiles.Profile'
NOTIFICATION_LANGUAGE_MODULE = 'account.Account'

# AWS
AWS_ACCESS_KEY_ID = 'AKIAI5KRE2OCDICYSLFA'
AWS_SECRET_ACCESS_KEY = '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'

ACCOUNT_OPEN_SIGNUP = False
ACCOUNT_REQUIRED_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = True

# build
BUILD_VERSION = ('0', '2')
BUILD_APPNAME = 'anadusis'
AWS_BUILD_BUCKET_NAME = '%s-django' % BUILD_APPNAME

EMAIL_CONFIRMATION_DAYS = 3
EMAIL_DEBUG = DEBUG
CONTACT_EMAIL = "info@oppian.com"
LOGIN_URL = "/account/login/"
LOGIN_REDIRECT_URLNAME = "what_next"

INTERNAL_IPS = (
    '127.0.0.1',
)

BUILD_IGNORE = (
    os.path.normpath(os.path.join(MEDIA_ROOT, 'upload')),
    os.path.normpath(os.path.join(PROJECT_ROOT, 'pinax-env')),
    os.path.normpath(os.path.join(PROJECT_ROOT, 'support files')),
    os.path.normpath(os.path.join(PROJECT_ROOT, 'rightscripts')),
    os.path.normpath(os.path.join(MEDIA_ROOT, 'avatars')),
    os.path.normpath(os.path.join(MEDIA_ROOT, 'videos')),
    os.path.normpath(os.path.join(MEDIA_ROOT, 'photologue')),
)

ugettext = lambda s: s
LANGUAGES = (
    ('en', u'English'),
)

# Email
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'anadusis@oppian.com'
EMAIL_HOST_PASSWORD = 'neetecel66'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
# default from address for errors
SERVER_EMAIL = '"%s" <anadusis@oppian.com>' % socket.gethostname()
# default from address for normal email
DEFAULT_FROM_EMAIL = 'anadusis@oppian.com'

# google analytics
URCHIN_ID = "UA-11393857-2"

YAHOO_MAPS_API_KEY = "..."

class NullStream(object):
    def write(*args, **kwargs):
        pass
    writeline = write
    writelines = write

RESTRUCTUREDTEXT_FILTER_SETTINGS = {
    'cloak_email_addresses': True,
    'file_insertion_enabled': False,
    'raw_enabled': False,
    'warning_stream': NullStream(),
    'strip_comments': True,
}

# if Django is running behind a proxy, we need to do things like use
# HTTP_X_FORWARDED_FOR instead of REMOTE_ADDR. This setting is used
# to inform apps of this fact
BEHIND_PROXY = False

FORCE_LOWERCASE_TAGS = True

WIKI_REQUIRES_LOGIN = True

# Uncomment this line after signing up for a Yahoo Maps API key at the
# following URL: https://developer.yahoo.com/wsregapp/
# YAHOO_MAPS_API_KEY = ''

# TINYMCE
TINYMCE_JS_URL =  '%stinymce/tiny_mce.js' % STATIC_URL
TINYMCE_JS_ROOT = '%s/apps/tinymce/media/tinymce' % PROJECT_ROOT
TINYMCE_DEFAULT_CONFIG = {
#    'plugins': "table,spellchecker,paste,searchreplace",
    'theme': "advanced",
#    'cleanup_on_startup': True,
#    'custom_undo_redo_levels': 10,
}
TINYMCE_SPELLCHECKER = False
TINYMCE_COMPRESSOR = True

# local_settings.py can be used to override environment-specific settings
# like database and email that differ between development and production.
try:
    from settings_local import *
except ImportError:
    pass
