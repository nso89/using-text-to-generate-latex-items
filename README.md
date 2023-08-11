# using-text-to-generate-latex-items
Using a Text File to Generate Latex Items.

* [Prerequisites](#prerequisites)
* [Setup](#setup)
* [Running the Script](#running-the-script)

#### <a name="prerequisites"></a>Prerequisites
* A complete install of `Python 3.x`.
* The `.txt` file with properly formatted lines.

Formatted Lines:
```
Responding to enquiries within the defined scope of the role and redirecting as appropriate
Booking rooms and arranging appropriate accommodations.
Liaising with contacts to ensure consistent administration procedures are followed
```

You'll notice that **periods are optional** and each line contains **no line breaks**.


#### <a name="setup"></a>Setup
1. Under your `USERPROFILE`, extract `using-text-to-generate-latex-items-main.zip`.

**Example**:
```batch
C:\Users\nso89\using-text-to-generate-latex-items-main
```
#### <a name="running-the-script"></a>Running the Script
1. Open `cmd.exe` and change the directory to the `using-text-to-generate-latex-items-main` folder.

**Example**:
```batch
C:\Users\nso89>cd using-text-to-generate-latex-items-main
```
2. Start the `main.py` script.

**Example**:
```batch
C:\Users\nso89\using-text-to-generate-latex-items-main>python main.py
```

3. Suppose the path to your `.txt` file is `C:\Users\username\Projects\using-text-to-generate-latex-items-main\input.txt`, just provide the path without the `USERPROFILE`.

**Example**:

```batch
File Path: Projects\using-text-to-generate-latex-items-main\input.txt
```

4. The `main.py` script generates the `output.txt` file (the `.txt` file will be generated in the same folder as the `input.txt` file).
```
\item Responding to enquiries within the defined scope of the role and redirecting as appropriate.
\item Booking rooms and arranging appropriate accommodations.
\item Liaising with contacts to ensure consistent administration procedures are followed.
```
You'll notice that the **lines containing no periods**, now end with periods.
