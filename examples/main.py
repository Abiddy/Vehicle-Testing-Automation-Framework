from vtaf.config import TestConfig
from vtaf.test_framework import VehicleTestFramework

def main():
    # Configure test parameters
    config = TestConfig(
        vehicle_id="SDV_001",
        test_suite="full_system_test",
        protocols=['CAN', 'Ethernet', 'MQTT'],
        simulation_tools={
            'dSPACE': True,
            'Vector_CANoe': True
        },
        test_levels=['system', 'HIL']
    )
    
    # Initialize and run test framework
    framework = VehicleTestFramework(config)
    results = framework.execute_test_suite()
    
    # Print results
    print("Test Execution Results:")
    print(results)

if __name__ == "__main__":
    main() 