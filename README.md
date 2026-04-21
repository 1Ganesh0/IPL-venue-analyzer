# IPL Venue Intelligence System

## 📌 Objective

Analyze IPL venues using ball-by-ball data to derive scoring patterns and strategic insights.

---

## 📊 Dataset

* IPL ball-by-ball dataset (2008–2025)
* Includes delivery-level data such as runs, overs, teams, and venue

---

## ⚙️ Features

* Venue-based filtering of match data
* Average score computation per venue
* Powerplay (overs 1–6) and death overs (16–20) analysis
* Chasing vs defending win percentage
* Insight generation based on scoring trends
* Visualization of score distributions

---

## 🧠 Methodology

* Processed 200k+ ball-by-ball records
* Aggregated delivery-level data into match-level metrics
* Computed phase-wise scoring patterns
* Evaluated match outcomes using innings-level comparisons
* Generated rule-based insights for venue-specific strategies

---

## 📈 Key Insights

* Scoring patterns vary significantly across venues
* Some venues favor chasing teams while others support defending
* Powerplay and death overs influence outcomes differently depending on venue
* Balanced performance across innings phases is critical

---

## 🖥️ Tech Stack

* Python
* Pandas, NumPy
* Matplotlib, Seaborn

---

## 🚀 How to Run

1. Open the notebook (`ipl_analysis.ipynb`) in Jupyter or Colab
2. Upload the dataset (`IPL.csv`)
3. Run all cells
4. Select a venue (via input prompt or index selection)

---

## 📂 Project Structure

```
IPL-Venue-Analysis/
│
├── ipl_analysis.ipynb
├── IPL.csv (optional)
├── requirements.txt
└── README.md
```

---

## 📌 Conclusion

This project demonstrates how raw ball-by-ball cricket data can be transformed into actionable venue-specific insights, enabling better understanding of scoring behavior and match dynamics.

---

## 🔮 Future Work

* Build interactive dashboard
* Add player-level analysis
* Extend to predictive modeling
