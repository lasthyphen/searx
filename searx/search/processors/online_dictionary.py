# SPDX-License-Identifier: AGPL-3.0-or-later

import re

from searx.utils import is_valid_lang
from .online import OnlineProcessor


parser_re = re.compile('.*?([a-z]+)-([a-z]+) ([^ ]+)$', re.I)


class OnlineDictionaryProcessor(OnlineProcessor):

    engine_type = 'online_dictionnary'

    def get_params(self, search_query, engine_category):
        params = super().get_params(search_query, engine_category)
        if params is None:
            return None

        m = parser_re.match(search_query.query)
        if not m:
            return None

        from_lang, to_lang, query = m.groups()

        from_lang = is_valid_lang(from_lang)
        to_lang = is_valid_lang(to_lang)

        if not from_lang or not to_lang:
            return None

        params['from_lang'] = from_lang
        params['to_lang'] = to_lang
        params['query'] = query

        return params