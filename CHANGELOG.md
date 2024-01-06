# CHANGELOG

## 0.3.1 (2024-01-06)
- Added `ares_util.ares.call_ares_sub_register` for getting data from sub registers described at: https://ares.gov.cz/swagger-ui/#/
- Added `ares_util.ares.sub_register_state_transformer`
- Added `ares_util.settings.SUB_REGISTER_MAP`
- Modified `ares_util.ares.call_ares` to also return `sub_registers` dictionary with info about available sub registers

## 0.3.0 (2024-01-04)
- `ares_util.ares.call_ares`
  - no longer raise `AresNoResponseError`
  - `city_town_part` has been removed from response
  - `zip_code` is now `int` type instead of `str`
