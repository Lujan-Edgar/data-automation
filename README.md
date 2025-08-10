# data-automation

This portfolio contains scripts and notebooks I developed to automate data processing for my team at **HDM Capital Renewable Finance**.  
The focus is on **cleaning Excel notebooks, automating repetitive processes, and delivering organized results**—primarily for business deals across US states.

## Projects

- **sort_ucc/matlab/**  
 This MATLAB Live Script ensured our main Excel notebook was ready for use by:
    - Eliminating duplicates
    - Filling missing data
    - Filtering out non-Texas deals
    - Sorting the final list in ascending order

- **automate_deal_list/**  
 My second major contribution. Python (pandas) notebook for automating the UCC Filing process.  
  This project was originally written as a MATLAB Live Script and allowed my team and I to automate the preparation of our shared Excel notebook for revision.  
  In short, it reads a `.txt` file containing a list of deal names, and uses these names to automatically assign the status of each UCC document from "Sent" to "Done" (meaning it has been uploaded to the CRM).

- **hurricane_harvey_matlab/**  
  MATLAB Live Script analyzing Hurricane Harvey data, focusing on data wrangling and visualization.

## Technologies Used
- Python (pandas)
- MATLAB
- Excel automation

## How to Use

1. Clone the repo or download the scripts.
2. For Python notebooks: open in JupyterLab or Jupyter Notebook.
3. For MATLAB scripts: open `.mlx` files in MATLAB R2020a or newer.
4. Check the "data" section to obtain the docs neede for running each script.
5. Some names of the files might be required since you will not be working with the original files.

---

**I built these projects to save time and ensure data quality in a real work environment.  
Feel free to explore, use, or suggest improvements!**
