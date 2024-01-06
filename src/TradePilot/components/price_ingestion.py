import yfinance as yf
import os
from TradePilot import logger
from TradePilot.utils.common import create_directories, save_json
from TradePilot.entity.config_entity import PriceDataIngestionConfig


class PriceDataIngestion:
    def __init__(self, config: PriceDataIngestionConfig) -> None:
        self.config = config

    def download_data(self):
        data_dir = os.path.join(self.config.root_dir, self.config.data_dir)
        create_directories([data_dir])

        companies = self.config.companies
        start_date = self.config.date_start
        end_date = self.config.date_end
        period = self.config.period
        df_rows = {}

        for company, ticker in companies.items():
            data = yf.download(tickers=ticker, start=start_date, end=end_date, period=period)
            df_rows[company] = data.shape[0]
            
            if df_rows[company]:
                logger.info(f"downloaded the data of the company {company} with {df_rows[company]} data points")
            else:
                logger.info(f"failed to fetch the data of the company {company}")

            file_name = os.path.join(data_dir, f"{company}.csv")
            data.to_csv(file_name)
            
            logger.info(f"saved the file {file_name}")

        json_file_path = os.path.join(self.config.root_dir, "data_info.json")
        save_json(path=json_file_path, data=df_rows)