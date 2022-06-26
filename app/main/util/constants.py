from enum import Enum


# TODO: change name
class ConstantsEnum(Enum):
  """
  Constants for the service
  """
  DEFAULT_BUFFER_SIZE = 8192


class ApisEnum(Enum):
  """
  APIs for the service 
  """
  ITEMS_API = 'https://api.mercadolibre.com/items/'
  USERS_API = 'https://api.mercadolibre.com/users/'
  CATEGORIES_API = 'https://api.mercadolibre.com/categories/'
  CURRENCIES_API = 'https://api.mercadolibre.com/currencies/'


class CountriesEnum(Enum):
  """
  Countries for the service
  """
  ARGENTINA = ("MLA", "Argentina")
  BRAZIL = ("MLB", "Brazil")
  COLOMBIA = ("MLC", "Colombia")

  def __init__(self, code, country_name):
    self.code = code
    self.country_name = country_name

# countries dict singleton
countries_dict = dict()
for country in CountriesEnum:
  countries_dict[country.code] = country.country_name
