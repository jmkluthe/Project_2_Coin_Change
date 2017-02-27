# Project_2_Coin_Change

Authors:
  <p>Joshua Kluthe</p>
  <ul>
    <li>changeslow.py
    <li>get_times.py
    <li>run_changeslow.py
    <li>\_\_init\_\_.py and \_\_main\_\_.py
  </ul>
  <p>Rohan Gokhale</p>
  <ul>
    <li>changegreedyalg.py
  </ul>
  <p>Alan Seims<p>
  <ul>
    <li>changedp.py
  </ul>

Program uses Python 3.x interpreter and is packaged into a module.

To run outside of the directory, use command "python3 Project_2_Coin_Change 'relative/link/to/file.txt'".

To run inside directory, use command "\_\_main\_\_.py 'relative/link/to/file.txt'" or "python3 \_\_main\_\_.py 'relative/link/to/file.txt'".

Running the module in this way reads the input file and runs each set of coins and change amount
through the greedy and dynamic programming algorithms. Since the changeslow algorithm is much slower
than the other two and requires very different inputs in order to run in a timely fashion, the
changeslow files are found in a subdirectory "Project_2_Coin_Change/changeslow_files".

To run the changeslow algorithm on a file with values that will allow it to run in a timely manner,
simply cd to the changeslow_files directory and call "run_changeslow.py changeslow_coins.txt" or
"python3 run_changeslow.py changeslow_coins.txt".
