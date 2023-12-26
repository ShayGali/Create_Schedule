from dataclasses import dataclass
import pandas as pd


@dataclass
class Lecture:
    """A class to represent a lecture"""
    class_name: str
    lecturer: str
    day: str
    hours: str
    room: str
    semester: str
    credits: int
    start_time: str = None
    end_time: str = None
    start_hour: int = None
    end_hour: int = None

    def __post_init__(self):
        """Calculate the start and end times of the lecture"""
        self.end_time, self.start_time = self.hours.split(" - ")
        self.start_hour = int(self.start_time.split(":")[0])
        self.end_hour = int(self.end_time.split(":")[0])

    def __str__(self):
        """Return a string representation of the lecture"""
        return f"{self.class_name}\n{self.lecturer}\n{self.hours}\n{self.room}\n{self.day}"


def create_lectures_list(df: pd.DataFrame):
    """given a DataFrame, create a list of Lecture objects"""
    lectures_list = []
    for index, row in df.iterrows():
        lectures_list.append(
            Lecture(
                row["שם שעור"],
                row["מורה"],
                row["יום"],
                row["שעות"],
                row["חדר"],
                row["סמס"],
                row['נ"ז'],
            )
        )
    return lectures_list
