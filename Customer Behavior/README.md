# Customer Shopping Behavior Analysis

## Overview

This project analyzes customer shopping behavior using Python, SQL, and Power BI. The goal is to discover customer purchasing patterns, identify trends, and build an interactive dashboard for business insights.

The project includes:

* Data cleaning and preprocessing using Python
* Exploratory Data Analysis (EDA)
* SQL database integration
* Interactive dashboard creation in Power BI

---

## Project Files

| File Name                        | Description                                        |
| -------------------------------- | -------------------------------------------------- |
| `customer_shopping_behavior.csv` | Dataset containing customer shopping behavior data |
| `Project1.ipynb`                 | Jupyter Notebook for data cleaning and analysis    |
| `customer.sql`                   | SQL queries and database operations                |
| `Dashboard1.pbix`                | Power BI dashboard file                            |

---

## Dataset Information

The dataset contains customer shopping information including:

* Customer demographics
* Purchase details
* Product categories
* Shipping methods
* Payment methods
* Subscription status
* Review ratings
* Purchase frequency

### Main Columns

* `Customer ID`
* `Age`
* `Gender`
* `Item Purchased`
* `Category`
* `Purchase Amount (USD)`
* `Location`
* `Season`
* `Review Rating`
* `Subscription Status`
* `Shipping Type`
* `Payment Method`
* `Frequency of Purchases`

---

## Technologies Used

### Programming & Analysis

* Python
* Pandas
* Jupyter Notebook

### Database

* MySQL
* SQLAlchemy

### Visualization

* Power BI

---

## Data Cleaning Steps

The following preprocessing tasks were performed:

1. Checked missing values
2. Filled missing review ratings using median values
3. Renamed column names for better readability
4. Created new features:

   * `age_group`
   * `purchasing_frequency_days`
5. Removed redundant columns

---

## Exploratory Data Analysis (EDA)

The analysis focuses on:

* Customer age distribution
* Product category trends
* Seasonal purchase behavior
* Payment method preferences
* Shipping type analysis
* Purchase frequency insights
* Review rating patterns

---

## Power BI Dashboard Features

The dashboard provides:

* Sales overview
* Customer segmentation
* Purchase trends
* Category-wise analysis
* Interactive filters and slicers
* KPI cards and visual insights

---

## SQL Integration

The project also demonstrates:

* Creating a MySQL database
* Importing cleaned data into SQL
* Running analytical SQL queries
* Connecting Python with MySQL using SQLAlchemy

---

## How to Run the Project

### 1. Clone the Repository

```bash
git clone <repository-link>
cd <project-folder>
```

### 2. Install Required Libraries

```bash
pip install pandas mysql-connector-python sqlalchemy jupyter
```

### 3. Run Jupyter Notebook

```bash
jupyter notebook
```

Open `Project1.ipynb` and run all cells.

### 4. Open Power BI Dashboard

Open `Dashboard1.pbix` using Power BI Desktop.

---

## Key Learning Outcomes

* Data preprocessing using Pandas
* Feature engineering techniques
* SQL database connectivity
* Data visualization with Power BI
* Business insight generation from customer data

---

## Future Improvements

* Add machine learning models for customer prediction
* Deploy dashboard online
* Create automated ETL pipeline
* Add advanced customer segmentation

---

## Author

**Ujjwal Kumar**

Aspiring Data Analyst / Data Scientist
