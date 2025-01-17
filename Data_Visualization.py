# Required Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from tkinter import Tk, filedialog, messagebox, Button, Label
import os

# Set display options
pd.set_option('display.max_columns', None)

# Function to upload and process CSV
def upload_and_process_csv():
    try:
        # Open file dialog to select CSV file
        file_path = filedialog.askopenfilename(
            filetypes=[("CSV Files", "*.csv")],
            title="Select a CSV File"
        )

        if not file_path:
            messagebox.showwarning("No File Selected", "Please select a CSV file to proceed.")
            return

        # Ask for output directory to save images
        output_dir = filedialog.askdirectory(title="Select Output Folder to Save Images")
        if not output_dir:
            messagebox.showwarning("No Folder Selected", "Please select a folder to save the images.")
            return

        # Read the CSV file into a pandas DataFrame
        data = pd.read_csv(file_path)

        # Display basic information in the console
        print("\n### Data Preview:")
        print(data.head())

        print("\n### Dataset Summary:")
        print(data.describe())

        print("\n### Missing Values:")
        print(data.isnull().sum())

        # Visualizations
        print("\nGenerating Visualizations...")

        # Numerical Columns
        numeric_cols = data.select_dtypes(include=['number']).columns

        if len(numeric_cols) > 0:
            # Histograms
            for col in numeric_cols:
                plt.figure(figsize=(8, 5))
                sns.histplot(data[col], bins=20, kde=True, color='blue')
                plt.title(f"Histogram of {col}")
                plt.xlabel(col)
                plt.ylabel("Frequency")
                plt.savefig(os.path.join(output_dir, f"Histogram_{col}.png"), dpi=300)
                plt.close()

            # Correlation Heatmap
            plt.figure(figsize=(10, 6))
            sns.heatmap(data[numeric_cols].corr(), annot=True, cmap="coolwarm", fmt=".2f")
            plt.title("Correlation Heatmap")
            plt.savefig(os.path.join(output_dir, "Correlation_Heatmap.png"), dpi=300)
            plt.close()

            # Boxplots
            for col in numeric_cols:
                plt.figure(figsize=(8, 5))
                sns.boxplot(y=data[col], color='lightblue')
                plt.title(f"Boxplot of {col}")
                plt.ylabel(col)
                plt.savefig(os.path.join(output_dir, f"Boxplot_{col}.png"), dpi=300)
                plt.close()

        # Categorical Columns
        categorical_cols = data.select_dtypes(include=['object', 'category']).columns

        if len(categorical_cols) > 0:
            # Bar Plots
            for col in categorical_cols:
                plt.figure(figsize=(8, 5))
                sns.countplot(x=data[col], hue=None, palette='viridis', legend=False)
                plt.title(f"Count Plot of {col}")
                plt.xticks(rotation=90)
                plt.tight_layout()
                plt.xlabel(col)
                plt.ylabel("Count")
                plt.savefig(os.path.join(output_dir, f"Countplot_{col}.png"), dpi=300)
                plt.close()

            # Pie Charts
            for col in categorical_cols:
                value_counts = data[col].value_counts()
                fig = px.pie(
                    values=value_counts.values,
                    names=value_counts.index,
                    title=f"Pie Chart of {col}",
                    color_discrete_sequence=px.colors.qualitative.Set3
                )
                # Save high-quality pie chart
                fig.write_image(os.path.join(output_dir, f"Piechart_{col}.png"), scale=2)

        # General Heatmap (Optional)
        if len(numeric_cols) > 1:
            plt.figure(figsize=(12, 8))
            sns.heatmap(data[numeric_cols].corr(), annot=True, cmap="Blues", fmt=".2f")
            plt.title("General Heatmap")
            plt.savefig(os.path.join(output_dir, "General_Heatmap.png"), dpi=300)
            plt.close()

        # Success Message
        messagebox.showinfo("Visualization Complete", f"All visualizations have been saved in: {output_dir}")

    except ImportError as e:
        messagebox.showerror("Missing Dependency", f"A required package is missing: {e}. Please install it and try again.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Initialize the GUI
def main():
    root = Tk()
    root.title("CSV Data Visualizer")
    root.geometry("400x200")

    # Label
    Label(root, text="CSV Data Visualizer", font=("Arial", 16)).pack(pady=20)

    # Upload Button
    Button(root, text="Upload and Visualize CSV", command=upload_and_process_csv, font=("Arial", 12)).pack(pady=20)

    # Run the GUI loop
    root.mainloop()

if __name__ == "__main__":
    main()
