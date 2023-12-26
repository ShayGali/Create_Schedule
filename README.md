this small project help me to build my schedule.

my university gives me the lectures schedule in a pdf file, and in rows and columns format, so I need to convert it to a
table format(cvc file), and from there to display it in a calendar format.

so I wrote this small project to help me with that.

## How to use it

I write full directions in Hebrew [here](./הסבר.pdf)

if you want to run it:
make sure that you have python 3.6 or higher installed on your computer.
make sure that you have java installed on your computer, and the system variable JAVA_HOME is set to the java
installation folder.

run the following commands:

```bash
pip install -r requirements.txt
```

now after you have the src.pdf file that contains the lectures schedule, run the following command:

```bash
python extract_data.py
```

now clean the data that created, and put the data in the table.csv file.

now run the following command:

```bash
python clean_data.py
```

now you have clean data with want you need, now you can run the following command:

```bash
python main.py
```

and a window will open with the calendar.