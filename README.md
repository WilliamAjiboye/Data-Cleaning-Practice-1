# 🎥 Netflix Data Cleaning Project

Welcome to the **Netflix Data Cleaning Project**, where we enhance a real-world dataset by enriching missing `cast` and `director` information using **The Movie Database (TMDb) API**. This project showcases the power of Python for practical data engineering and cleaning tasks.

---

## 📊 Project Overview

This project aims to clean the [Netflix Titles Dataset](https://www.kaggle.com/datasets/shivamb/netflix-shows) by:

* Identifying rows with missing `cast` or `director` fields.
* Querying TMDb API to retrieve missing data.
* Efficiently updating and saving the cleaned dataset.

---

## 🛠️ Tools & Technologies

| Tool       | Purpose                          |
| ---------- | -------------------------------- |
| `Python`   | Core language for scripting      |
| `Pandas`   | Data manipulation & analysis     |
| `Requests` | HTTP requests to access TMDb API |
| `tqdm`     | Progress bar for user feedback   |
| `dotenv`   | Secure API key management        |
| `TMDb API` | Source of movie/series metadata  |

---

## 📝 Features

* Modular codebase (splits logic into reusable functions)
* TMDb caching for performance optimization
* Exception handling for robust API interaction
* Final dataset saved as `netflix_titles_updated.csv`

---

## 📂 Project Structure

```bash
.
├── main.py                # Driver script
├── tmdb_api.py            # All API utility functions
├── secrets.env            # Stores your TMDb API key securely
├── netflix_titles.csv     # Original dataset
├── netflix_titles_updated.csv  # Cleaned output
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

---

## 🚀 Getting Started

1. **Clone the repo**

```bash
git clone https://github.com/your-username/netflix-data-cleaning.git
cd netflix-data-cleaning
```

2. **Set up your environment**

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. **Create your **\`\`** file**

```env
API_KEY=your_tmdb_api_key_here
```

4. **Run the script**

```bash
python main.py
```

---

## 👍 Outcome

A cleaned Netflix dataset with enriched metadata:

* Filled `cast` and `director` fields
* Preserved original indices for easy traceability
* Optimized performance through caching and error handling

---

## 🌟 What You Learn

* Real-world data cleaning strategies
* Working with third-party APIs
* Writing modular, production-friendly Python code
* Managing secrets and project dependencies securely

---

## 📁 Sample Output

```csv
title,type,director,cast,...
The Crown,TV Show,Peter Morgan,Claire Foy, Matt Smith,...
Bird Box,Movie,Susanne Bier,Sandra Bullock, Trevante Rhodes,...
```

---

## 👁️ Future Improvements

* Add unit tests for API modules
* Extend to fill in missing genres, countries, and descriptions
* Build a web dashboard to visualize the enrichment process

---

## 🚀 Contributing

Pull requests are welcome! Feel free to fork the repository and enhance its functionality.

---

## 🚀 License

MIT License. See `LICENSE` for more details.

---

> ✨ *Built with passion for clean data and cleaner code.*
