from dataclasses import dataclass
from typing import List, Dict

@dataclass
class TestConfig:
    """Configuration for test execution"""
    vehicle_id: str
    test_suite: str
    protocols: List[str]
    simulation_tools: Dict[str, bool]
    test_levels: List[str]
    
class VTAFConfig:
    def __init__(self):
        self.supported_protocols = ['CAN', 'LIN', 'FlexRay', 'Ethernet', 'MQTT', 'V2X']
        self.simulation_tools = {
            'dSPACE': True,
            'Vector_CANoe': True,
            'LabVIEW': True,
            'CarSim': True,
            'MATLAB': True
        }
        self.test_levels = ['unit', 'integration', 'system', 'HIL', 'SIL', 'MIL'] 