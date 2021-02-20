"""Provides a random greeting every day."""
import logging
import random
from datetime import date

GREETINGS = [
    'Never settle.',
    'Walk the talk, and talk the walk!',

    'Never, never, never give up. - Winston Churchill',
    'To consume without investing is to ruin. - Norbert Blüm',
    'If one does not know to which port one is sailing, no wind is favorable. '
        '- Lucius Annaeus Seneca',
    'If you think you can do a thing or think you can\'t do a thing, you\'re right. - Henry Ford',
    'You can\'t build a reputation on what you are going to do. - Henry Ford',
    'Whether you think you can, or you think you can\'t - you\'re right. - Henry Ford',
    'Anyone who stops learning is old, whether at twenty or eighty. Anyone who keeps learning '
        'stays young. - Henry Ford',
    'Failure is simply the opportunity to begin again, this time more intelligently. - Henry Ford',
    'It has been my observation that most people get ahead during the time that others waste. '
        '- Henry Ford',
    'Someone\'s sitting in the shade today because someone planted a tree a long time ago. '
        '- Warren Buffett',
    'If you don\'t feel comfortable owning something for 10 years, then don\'t own it for 10 '
        'minutes. - Warren Buffett',
    'Be fearful when others are greedy. Be greedy when others are fearful. - Warren Buffett',
    'People should pursue what they\'re passionate about. That will make them happier than pretty '
        'much anything else. - Elon Musk',
    'Persistence is very important. You should not give up unless you are forced to give up. '
        '- Elon Musk',
    'The human brain is an incredible pattern-matching machine. - Jeff Bezos',
    'Work Hard, have fun, make history. - Jeff Bezos',
    'Patience is a key element of success. - Bill Gates',
    'People always fear change. People feared electricity when it was invented, didn\'t they? '
        '- Bill Gates',
    'Innovation distinguishes between a leader and a follower. - Steve Jobs',
    'My favorite things in life don\'t cost any money. It\'s really clear that the most precious '
        'resource we all have is time. - Steve Jobs',
]

CURRENT = GREETINGS[0]
LAST_UPDATED = 0


def get_greeting():
    """Returns the current greeting."""
    global CURRENT
    global LAST_UPDATED

    if not date.today() == LAST_UPDATED:
        CURRENT = random.choice(GREETINGS)
        LAST_UPDATED = date.today()

    return CURRENT


try:
    import custom_greetings
    GREETINGS.extend(custom_greetings.GREETINGS)
except ModuleNotFoundError:
    logging.info('Using default greetings module.')
