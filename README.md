# music-league-statistics
**GOAL:** Extracting end-of-season statistics from the Music League app.

**NOTE:** This repository assumes that you have access to a league's four main data files:
- `competitors.csv` --> Competitor IDs mapped to Names
- `rounds.csv` --> Round themes mapped to ID, Description, and Playlist Link
- `submissions.csv` --> Songs (and their metadata) for each Round
- `votes.csv` --> Votes per Competitor (and their metadata) for each Song in each Round

Sample data files can be found in the `data` directory.

## REQUIREMENTS
Requirements are minimal and can be installed using your preferred package manager.
- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`

## REPOSITORY ORGANIZATION
- `organize.py` extracts information from the four main data files (see above) and builds:
  - `output_master.csv` --> The Massive Spreadsheet
  - `output_submissions.csv` --> A re-organized version of `submissions.csv` for easier data analysis
  - `output_votes.csv` --> A re-organized version of `votes.csv` for easier data analysis
- `statistics.py` extracts many statistics (listed at the top of script) from `master.csv`, `output_submissions.csv`, and `output_votes.csv`.

**DIRECTORIES**
- `data` holds the raw exported files from Music League. See [here](https://www.reddit.com/r/musicleague/comments/1e2idmt/now_available_to_music_league_subscribers_league/) for a brief summary of how to get these files.

## USE
After installing the package requirements and exporting your league's data into the `data` directory, you run the following to build the three output files:

```
python organize.py
```

Then, to calculate statistics, run:

```
python statistics.py 
```
## TO-DO:
- Build `organize.py`
  - Map Rounds and Participants to their corresponding IDs.
  - Explode each submission to include rounds for ease of `.groupby()`.

- Build `statistics.py`
  - Confer with Alyssa about statistics.
