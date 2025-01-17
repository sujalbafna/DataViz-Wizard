# CSV Data Visualization Tool 🔄

A user-friendly Python-based tool to visualize and analyze CSV files. Upload your CSV file through a simple GUI and generate high-quality visualizations such as histograms, boxplots, heatmaps, pie charts, and more. Save all visualizations as high-resolution images for analysis and presentations. 📊

---

## **Features** 🌐

- Intuitive GUI for uploading CSV files and selecting output folders. 📝
- High-quality visualizations for numerical and categorical data:
  - **Histograms** 🌄
  - **Boxplots** 🔢
  - **Correlation Heatmaps** 🔎
  - **Bar Plots** 📊
  - **Pie Charts** 🍓
- Saves all visualizations as PNG files for easy sharing and analysis. 🔐
- Handles missing values and displays dataset summaries. 🔧

---

## **Requirements** ⚡

Make sure you have Python installed (version 3.7 or later). Install the required dependencies using the following command:

```bash
pip install pandas seaborn matplotlib plotly kaleido
```

---

## **How to Use** 📚

### **1. Clone the Repository** 🔄
Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### **2. Run the Application** 🔄
Run the Python script to launch the GUI:

```bash
python Data_Visualization.py
```

### **3. Use the Tool** 🎨
1. **Upload CSV File**: 
   - Click the **"Upload and Visualize CSV"** button in the GUI. 📎
   - Select the CSV file you want to analyze. 🔢

2. **Choose Output Folder**:
   - After uploading the CSV file, you’ll be prompted to select a folder to save the visualizations. 📂

3. **View Progress**:
   - The tool processes the file, generates visualizations, and saves them as high-quality images in the selected folder. 🖼

4. **Check Output**:
   - Navigate to the output folder to view PNG images of all visualizations. 📷

---

## **Visualizations Generated** 📊

1. **Histograms** for numerical columns. 🌄
2. **Boxplots** to identify outliers. 🔢
3. **Correlation Heatmaps** for numeric column relationships. 🔎
4. **Bar Plots** for categorical columns. 📈
5. **Pie Charts** for categorical data distributions. 🍓
6. **General Heatmap** of the dataset (if applicable). 🎨

---

## **Troubleshooting** 🚒

- **Missing Dependencies**:
  If you encounter an error about missing dependencies, ensure you’ve installed all required packages:
  ```bash
  pip install pandas seaborn matplotlib plotly kaleido
  ```

- **Invalid File Format**:
  Ensure the file you upload is a valid `.csv` file. 🔖

- **Kaleido Errors**:
  Make sure `kaleido` is installed for exporting `plotly` images:
  ```bash
  pip install -U kaleido
  ```

---

## **Contributing** 🎩

Contributions are welcome! Feel free to fork this repository, create a new branch, and submit a pull request with your improvements or new features. 📊

---

## **License** 🏆

This project is licensed under the [MIT License](LICENSE). 🔒

---

## **Contact** 📧

For any questions or suggestions, feel free to contact me via GitHub or open an issue in this repository. 🛠️

---

