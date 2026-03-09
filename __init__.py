from .tone_extractor_node import ArchToneExtractor

NODE_CLASS_MAPPINGS = {
    "ArchToneExtractor": ArchToneExtractor
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ArchToneExtractor": "Architecture Tone & Atmosphere Extractor"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
