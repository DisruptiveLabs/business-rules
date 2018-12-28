from __future__ import absolute_import
import datetime

from business_rules.variables import (
    BaseVariables,
    boolean_rule_variable,
    datetime_rule_variable,
    numeric_rule_variable,
    select_rule_variable,
    string_rule_variable,
)


class ExampleVariables(BaseVariables):
    def __init__(self, basket):
        self.basket = basket

    @select_rule_variable(public=False)
    def items(self):
        return self.basket.product_codes

    @string_rule_variable()
    def current_month(self):
        return datetime.datetime.now().strftime("%B")

    @numeric_rule_variable()
    def item_count(self):
        return len(self.basket.product_codes)

    @boolean_rule_variable()
    def rule_variable(self, **kwargs):
        assert 'rule' in kwargs
        return True

    @datetime_rule_variable()
    def today(self):
        return datetime.date.today()
