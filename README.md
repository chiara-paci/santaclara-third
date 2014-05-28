#Santa Clara Third

Santa Clara Third is a Django app containg all static third parties
files common to all Santa Clara applications.

1. Build package:
   ```
        $ cd santaclara-third/
        $ python setup.py sdist
   ```

2. Install package:
    ```
        $ cd santaclara-third/
        $ pip install --user dist/santaclara_third-<version>.tar.gz
    ```

3. Add "santaclara_css" to your INSTALLED_APPS setting like this:
    ```
        INSTALLED_APPS = (
            ...
            'santaclara_third',
            ...
        )
    ```

