from typing import List, Dict
import logging
from .config import TestConfig, VTAFConfig
from .protocols import ProtocolHandler
from .metrics import MetricsCollector

class VehicleTestFramework:
    def __init__(self, config: TestConfig):
        self.config = config
        self.logger = logging.getLogger(__name__)
        self.protocol_handler = ProtocolHandler()
        self.metrics_collector = MetricsCollector()
        self.vtaf_config = VTAFConfig()
        
    def execute_test_suite(self) -> Dict:
        """
        Execute test suite and collect metrics
        """
        self.logger.info(f"Executing test suite: {self.config.test_suite}")
        results = {}
        
        # Execute tests for each protocol
        for protocol in self.config.protocols:
            if protocol in self.vtaf_config.supported_protocols:
                protocol_results = self.protocol_handler.test_protocol(protocol)
                results[protocol] = protocol_results
                
        # Collect and analyze metrics
        metrics = self.metrics_collector.collect_metrics(results)
        return metrics 