import pandas as pd
from src.wine.logging import logger



class DataValidation:
    def __init__(self, config):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            # Read dataset
            data = pd.read_csv(self.config.unzip_data_dir)

            # Actual columns and datatypes from data
            actual_schema = dict(data.dtypes.astype(str))

            # Expected schema from schema.yaml
            expected_schema = self.config.all_schema

            # List to store validation errors
            errors = []

            # Validate columns and datatypes
            for col, dtype in expected_schema.items():

                # Check if column exists
                if col not in actual_schema:
                    errors.append(f"Missing column: {col}")

                # Check datatype
                elif actual_schema[col] != dtype:
                    errors.append(
                        f"{col}: Expected {dtype}, Found {actual_schema[col]}"
                    )

            # Check for extra columns in dataset
            for col in actual_schema.keys():
                if col not in expected_schema:
                    errors.append(f"Unexpected column found: {col}")

            # Validation status
            validation_status = len(errors) == 0  # validation_status is True if no errors and False if any error.

            # Write status and errors to file
            with open(self.config.status_file, "w") as f:
                if validation_status:
                    f.write("Validation status: True")
                else:
                    f.write("Validation status: False\n")
                    for err in errors:
                        f.write(err + "\n")

            logger.info(f"Validation status: {validation_status}")

            if errors:
                logger.info("Validation Errors:")
                for err in errors:
                    logger.info(err)

            return validation_status

        except Exception as e:
            raise e