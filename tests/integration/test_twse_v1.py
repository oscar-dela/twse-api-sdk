from twse_api_sdk.twse import TwseV1
import logging

logger = logging.getLogger(__name__)
api = TwseV1()


def test_list_monthly_operating_income() -> None:
    logger.info(api.list_monthly_operating_income())


def test_list_top_20_volume_stocks() -> None:
    logger.info(api.list_top_20_volume_stocks())


def test_list_day_trade_short_suspend_announcement() -> None:
    logger.info(api.list_day_trade_short_suspend_announcement())


def test_list_day_trade_short_suspend_history() -> None:
    logger.info(api.list_day_trade_short_suspend_history())


def test_get_per_5_sec_trading_volume() -> None:
    logger.info(api.get_per_5_sec_trading_volume())


def test_list_top_20_oversea_holding_stocks() -> None:
    logger.info(api.list_top_20_oversea_holding_stocks())


def test_list_oversea_holding_stock_industry_percentage_catagory() -> None:
    logger.info(api.list_oversea_holding_stock_industry_percentage_catagory())


def test_list_stock_pe_and_pb_and_dividend_yield() -> None:
    logger.info(api.list_stock_pe_and_pb_and_dividend_yield())


def test_list_no_restriction_of_quota_change_stock() -> None:
    logger.info(api.list_no_restriction_of_quota_change_stock())


def test_list_stop_trading_stocks() -> None:
    logger.info(api.list_stop_trading_stocks())


def test_list_stop_margin_stocks() -> None:
    logger.info(api.list_stop_margin_stocks())


def test_get_margin_volume() -> None:
    logger.info(api.get_margin_volume())


def test_get_abnormal_recommandated_stocks() -> None:
    logger.info(api.get_abnormal_recommandated_stocks())
