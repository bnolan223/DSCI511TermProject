# Project Title: **Bad Bunny Song Data Analysis Using Last.fm API**

## **Project Overview**
This project aims to collect, process, and analyze data on Bad Bunny’s songs using the Last.fm API. The primary goal is to extract as much information as possible on all of Bad Bunny's tracks, including track details and relevant statistics (such as play counts, listeners, etc.). This data will be used to perform exploratory analysis and share insights.

---

## **Data Source**
**Source:** Last.fm API

**Data Available:**
- Track names
- Play count
- Listeners count
- Album name
- Track duration
- Other metadata (when available)

The Last.fm API provides publicly accessible information about tracks, artists, and albums. It allows developers to query and retrieve comprehensive information for artists like Bad Bunny.

**Access Rights:**
The Last.fm API requires the creation of an API key to access data. Usage of this data is subject to Last.fm’s [API Terms of Use](https://www.last.fm/api/tos).

**Limitations:**
- Data may be limited by Last.fm’s terms of service.
- Some fields may be incomplete or missing for certain tracks.
- Rate limits may apply for API requests, requiring efficient use of API calls.

---

## **Project Files**
**1. `main.py`:**
   - Script to extract and process song data from Last.fm API.
   - Collects data on all of Bad Bunny's available tracks.
   - Processes raw data into a structured format (CSV) for analysis.

**2. `data/`:**
   - Contains the output CSV file with all tracks and metadata.

**3. `README.md`:**
   - Documentation file (this file) with an overview of the project, instructions, and notes on access rights.

---

## **Setup Instructions**

### **Step 1: Prerequisites**
1. **Install Python**: Ensure Python 3.x is installed on your system. You can check with:
   ```bash
   python --version
   ```
2. **Install Required Libraries**:
   ```bash
   pip install requests pandas
   ```

---

### **Step 2: API Setup**
1. **Get API Key**
   - Go to the [Last.fm API](https://www.last.fm/api/account/create) and log in.
   - Create a new API key and copy it for use in the script.

2. **Add API Key to the Script**
   - Open `main.py`.
   - Replace `YOUR_API_KEY_HERE` with your actual API key in the appropriate part of the script.

---

### **Step 3: Run the Script**
1. Execute the following command to run the script and extract the data:
   ```bash
   python main.py
   ```
2. Once the script runs successfully, the data will be saved in the `data/` directory as a CSV file containing all the track data for Bad Bunny.

---

## **Approach to Data Acquisition**
1. **API Request**:
   - The Last.fm API’s "artist.getTopTracks" method is used to request the top tracks for Bad Bunny.
   - API responses are paginated, so multiple calls are made to get all track data.

2. **Data Parsing**:
   - The API response is parsed to extract essential data like track name, listeners, play count, and album.

3. **Data Preprocessing**:
   - Missing or incomplete data is flagged.
   - Data is cleaned and structured into a tabular CSV format for further analysis.

---

## **Approach to Data Preprocessing**
1. **Remove Duplicates**:
   - Check for duplicate tracks and remove them to ensure unique entries.

2. **Data Cleaning**:
   - Handle missing or null values appropriately.
   - Convert numeric fields (like listeners and play count) to integers for analysis.

3. **Data Structuring**:
   - Store track information (name, album, play count, etc.) into a CSV file for easy sharing and analysis.

---

## **Issues and Limitations**
1. **Spotify API Changes**:
   - Spotify’s recent API changes (effective November 27, 2024) restrict access to certain catalog information for new app developers. These changes affected the ability to retrieve track metadata and analysis data from Spotify’s API.
   - Due to these limitations, the team pivoted to use the Last.fm API instead.

2. **Data Availability**:
   - Data availability may vary depending on what Last.fm has in its catalog. Some track metadata may be incomplete.

3. **Rate Limits**:
   - The Last.fm API enforces rate limits on the number of API requests.
   - Excessive calls may result in temporary blocking. To avoid this, requests are spaced out and limited to essential calls only.

4. **Data Completeness**:
   - Not all tracks may have complete metadata, as availability depends on Last.fm’s database.

---

## **Potential Enhancements**
1. **Error Handling**:
   - Improve handling for rate-limit errors and retries in the API call process.

2. **Data Visualization**:
   - Create visualizations (like play count vs. listeners) for deeper analysis.

3. **Automation**:
   - Automate the process to update track data periodically (e.g., using GitHub Actions or a cron job).

4. **Multiple Artists**:
   - Expand the project to analyze data for multiple artists in addition to Bad Bunny.

---

## **Contact Information**
For any questions or support, please reach out to:
- **Contributor**: Bennett Nolan
- **Email**: bsn29@drexel.edu

---

## **Conclusion**
This project provides an end-to-end solution for collecting, cleaning, and analyzing data on Bad Bunny’s music catalog using the Last.fm API. The README outlines all steps required to set up, run, and maintain the project. By publishing the project’s code and dataset to GitHub, others can replicate or expand on the analysis.

---

