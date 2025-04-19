import subprocess
import sys

class PackageInstaller:
    def __init__(self, required_packages=None):
        # Default list of required packages if not provided
        if required_packages is None:
            required_packages = ['yfinance', 'xgboost', 'scikit-learn', 'pandas', 'numpy']
        self.required_packages = required_packages

    def install_package(self, package):
        """Installs the package using pip."""
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

    def check_and_install_packages(self):
        """Checks if required packages are installed. Installs them if not."""
        for package in self.required_packages:
            try:
                # Try importing the package to check if it's installed
                __import__(package)
            except ImportError:
                # If the package is not installed, install it
                print(f"Package {package} not found. Installing...")
                self.install_package(package)
                print(f"Package {package} installed successfully.")
            else:
                print(f"Package {package} is already installed.")
