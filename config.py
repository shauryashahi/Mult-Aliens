from plugins.text_formatter import text_formatter
from plugins.pdf_formatter import pdf_formatter


available_plugins = {
    "text": text_formatter,
    "pdf": pdf_formatter
}
