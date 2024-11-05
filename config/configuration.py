import os
import yaml

from typing import Any, Dict


class Configuration:
    """Base URL configuration and general settings retrieval."""

    def __init__(self):
        self.config = self._load_config()

    @staticmethod
    def _load_config() -> Dict[str, Any]:
        """Loads configuration data from config.yaml."""
        config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.yaml")

        try:
            with open(config_path, 'r') as file:
                return yaml.safe_load(file) or {}
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file not found at path: {config_path}")
        except yaml.YAMLError as e:
            raise ValueError(f"Error parsing YAML file at {config_path}: {e}")

    def _get_value(self, keys: str) -> Any:
        """Return a value from the configuration dictionary."""
        keys_list = keys.split('.')
        value = self.config
        for key in keys_list:
            try:
                value = value[key]
            except KeyError:
                raise KeyError(f"Missing key '{key}' in configuration.")
        return value

    def get_e_commerce_base_url(self) -> str:
        """Return the base URL specified in the configuration."""
        return self._get_value('base_url.e_commerce_base_url')

    def get_device_name(self) -> str:
        """Return the chosen device name from the configuration."""
        return self._get_value('mobile_emulation_device.device_name')