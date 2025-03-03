from typing import Dict
import pandas as pd
import matplotlib.pyplot as plt

class MetricsCollector:
    def __init__(self):
        self.kpi_metrics = {
            'defect_density': 0,
            'test_coverage': 0,
            'performance_score': 0
        }
    
    def collect_metrics(self, test_results: Dict) -> Dict:
        """
        Collect and analyze test metrics
        """
        # Calculate defect density
        self.calculate_defect_density(test_results)
        
        # Calculate test coverage
        self.calculate_test_coverage(test_results)
        
        # Generate performance metrics
        self.calculate_performance_metrics(test_results)
        
        return self.kpi_metrics
    
    def calculate_defect_density(self, test_results: Dict):
        """
        Calculate defect density based on test results
        """
        total_tests = len(test_results)
        failed_tests = sum(1 for result in test_results.values() 
                         if result.get('status') == 'error')
        
        self.kpi_metrics['defect_density'] = (failed_tests / total_tests) if total_tests > 0 else 0

    def calculate_test_coverage(self, test_results: Dict):
        """
        Calculate test coverage percentage
        """
        total_protocols = len(test_results)
        successful_tests = sum(1 for result in test_results.values() 
                             if result.get('status') == 'success')
        
        self.kpi_metrics['test_coverage'] = (successful_tests / total_protocols * 100) if total_protocols > 0 else 0

    def calculate_performance_metrics(self, test_results: Dict):
        """
        Calculate overall performance score
        """
        if not test_results:
            self.kpi_metrics['performance_score'] = 0
            return

        success_rate = sum(1 for result in test_results.values() 
                          if result.get('status') == 'success') / len(test_results)
        self.kpi_metrics['performance_score'] = success_rate * 100
    
    def generate_report(self, metrics: Dict):
        """
        Generate test report with visualizations
        """
        df = pd.DataFrame(metrics)
        plt.figure(figsize=(10, 6))
        df.plot(kind='bar')
        plt.title('Test Metrics Overview')
        plt.savefig('test_metrics.png') 