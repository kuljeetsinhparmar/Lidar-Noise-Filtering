LiDAR Noise Filtering Project

Overview

This repository contains the code and documentation for a noise filtering project focused on LiDAR data preprocessing. The primary goal of this project was to develop efficient solutions for noise removal in LiDAR data using Statistical Outlier Removal (SOR) and Radius Outlier Removal techniques.

Project Objectives

Preprocessing LiDAR Data: Implementing techniques to clean and filter noise from raw LiDAR data.

Noise Filtering: Applying SOR and Radius Outlier Removal to enhance data quality.

Efficiency: Ensuring that the preprocessing stage is optimized for performance and accuracy.

Techniques Used

Statistical Outlier Removal (SOR): This technique removes points that are statistically farther from the average, based on a user-defined threshold.

Radius Outlier Removal: This method eliminates points that do not have a sufficient number of neighbors within a specified radius.

Repository Structure

src/: Contains the Python scripts for noise filtering.

data/: A sample dataset to test the filtering techniques.

notebooks/: Jupyter notebooks that document the experimentation process.

README.md: Project overview and documentation.
