# 🐶 Dynamic Dog Wallpaper Changer 🐶

Woof-woof! 🐾 Are you a doggo lover who's tired of the same old, boring desktop wallpaper? Say no more! This short and pawsome Python script let's you set an adorable doggo pic as your wallpaper every day! It's like a daily belly rub for your desktop! 🐕‍🦺💕

## Features

- Fetch images of selected breeds!
- Or fetch random doggos every day!
- Set the image as your desktop wallpaper!

## Requirements

- Windows OS
- Python 3.x
- `requests` library
- `PIL` (Pillow) library
- `ctypes`

## Installation

1. Clone this repository or download the script.
2. Install the required Python packages if you haven't already:

    ```bash
    pip install requests Pillow
    ```

## Usage

### Manual Execution

You can run the script manually by executing the following command in your terminal:

```bash
python path/to/main.py
```

### Scheduled Execution

To have a new wallpaper set automatically at regular intervals, you can schedule the script to run using Windows Task Scheduler.

#### Steps:

1. Open Task Scheduler.
2. Create a new task and navigate to the "Actions" tab.
3. Add a new action and select "Start a program".
4. In the "Program/script" box, enter the full path to your Python executable (e.g., `C:\path\to\python.exe`).
5. In the "Add arguments (optional)" box, enter the full path to the script (e.g., `"C:\path\to\script.py"`).

Make sure to set the trigger as per your preference, for instance, to run the script daily.

## Troubleshooting

If the script isn't working as expected when scheduled through Task Scheduler, consider the following:

1. Ensure that the user account running the task has the required permissions.
2. Make sure you've entered the full paths to both the Python executable and the script in Task Scheduler.
3. Check "Run with highest privileges" under the "General" tab in Task Scheduler settings.

