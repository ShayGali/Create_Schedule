from typing import Tuple


def get_color(class_name: str) -> Tuple[str, str]:
    """
    This function returns the color of the class and the color of the text.
    Now it will work for semester 1 only.
    """
    if "אלגוריתמים" in class_name:
        return "#B2EBF2", "#80DEEA"  # Light Blue Lagoon & Medium Turquoise
    elif class_name.startswith("רשתות"):
        return "#D1C4E9", "#B39DDB"  # Bright Gray & Light Pastel Purple
    elif class_name.startswith("הסתברות"):
        return "#F8BBD0", "#F48FB1"  # Light Thulian Pink & English Lavender
    elif class_name.startswith("תכנות מערכות"):
        return "#C8E6C9", "#A5D6A7"  # Tea Green & Light Moss Green
    elif class_name.startswith("תכנות מונחה"):
        return "#FFECB3", "#FFE082"  # Very Pale Orange & Light Gold
    elif class_name.startswith("מבוא ל"):
        return "#CD5C5C", "#BC8F8F"
    return "#FFFFFF", "#FFFFFF"  # White & White
