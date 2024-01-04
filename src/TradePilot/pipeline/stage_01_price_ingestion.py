from TradePilot.config.configuration import ConfigurationManager
from TradePilot.components.price_ingestion import PriceIngestion
from TradePilot import logger

STAGE_NAME = "Price Ingestion stage"


class PriceIngestionTrainingPipeline:
    def __init__(self):
        """
        Initialize DataIngestionTrainingPipeline instance.
        """
        pass

    def main(self):
        """
        Execute the main steps of the data ingestion training pipeline.

        Returns:
            None
        """
        config = ConfigurationManager()
        price_ingestion_config = config.get_price_ingestion_config()
        price_ingestion = PriceIngestion(config=price_ingestion_config)
        price_ingestion.download_data()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = PriceIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e