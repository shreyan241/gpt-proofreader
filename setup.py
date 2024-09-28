import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "packages": [
        "os", "tkinter", "asyncio"
    ],
    "includes": [
        "src.api_client",
        "src.cache_manager",
        "src.config",
        "src.document_types",
        "src.gui",
        "src.file_handlers",
        "src.output_manager",
        "src.prompts",
        "src.text_processing",
        "src.utils"
    ],
    "include_files": [
        # Add any additional files your application needs
        # ("path/to/file", "destination/in/executable")
    ],
    "excludes": [],
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"  # Use this for a Windows GUI application

setup(
    name="GrammarCorrector",
    version="1.0",
    description="Grammar Correction Tool",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base, target_name="GrammarCorrector.exe")],
    install_requires=[
        "aiohappyeyeballs==2.4.0",
        "aiohttp==3.10.6",
        "aiolimiter==1.1.0",
        "aiosignal==1.3.1",
        "asyncio==3.4.3",
        "attrs==24.2.0",
        "certifi==2024.8.30",
        "cffi==1.17.1",
        "charset-normalizer==3.3.2",
        "colorama==0.4.6",
        "cryptography==43.0.1",
        "docx==0.2.4",
        "et-xmlfile==1.1.0",
        "fpdf==1.7.2",
        "frozenlist==1.4.1",
        "idna==3.10",
        "loguru==0.7.2",
        "lxml==5.3.0",
        "multidict==6.1.0",
        "numpy==2.1.1",
        "openai==0.28.0",
        "openpyxl==3.1.5",
        "pandas==2.2.3",
        "pdfminer.six==20231228",
        "pdfplumber==0.11.4",
        "pillow==10.4.0",
        "pycparser==2.22",
        "pypdfium2==4.30.0",
        "python-dateutil==2.9.0.post0",
        "python-docx==1.1.2",
        "pytz==2024.2",
        "regex==2024.9.11",
        "requests==2.32.3",
        "setuptools==75.1.0",
        "six==1.16.0",
        "tiktoken==0.7.0",
        "tqdm==4.66.5",
        "typing_extensions==4.12.2",
        "tzdata==2024.2",
        "urllib3==2.2.3",
        "wheel==0.44.0",
        "win32-setctime==1.1.0",
        "yarl==1.12.1",
    ],
)