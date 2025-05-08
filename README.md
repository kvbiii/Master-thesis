# How much to pay for a night? Predicting Airbnb listing prices using Machine Learning

## Overview
This project is part of my master thesis at the University of Warsaw, Faculty of Economic Sciences. It focuses on predicting Airbnb listing prices using machine learning techniques. The project includes:

- **Data Collection and Cleaning**: Gathering and preprocessing Airbnb data, location-based features, and metadata.
- **Exploratory Data Analysis (EDA)**: Analyzing datasets to uncover patterns and insights.
- **Image Analysis**: Classifying room types and extracting features from Airbnb listing images.
- **Location Analysis**: Evaluating the impact of geographical and neighborhood features on pricing.
- **Modeling**: Building and evaluating machine learning models to predict listing prices.
- **Visualization**: Presenting findings through visualizations and reports.

The project integrates various datasets, image processing techniques, and machine learning models to provide a comprehensive analysis of factors influencing Airbnb prices.

## Folder Structure
```
┣━ 📁 Data
┃  ┣━ 📁 Location
┃  ┃  ┣━ 📊 bus_stops.csv
┃  ┃  ┣━ 📊 crimes.csv
┃  ┃  ┣━ 📊 cultural.csv
┃  ┃  ┣━ 📊 education.csv
┃  ┃  ┣━ 📊 health.csv
┃  ┃  ┣━ 📊 main_attractions.csv
┃  ┃  ┣━ 📊 recreation.csv
┃  ┃  ┣━ 📊 religious.csv
┃  ┃  ┣━ 📊 restaurants.csv
┃  ┃  ┗━ 📊 subway_stations.csv
┃  ┣━ 📊 airbnb_data.csv
┃  ┣━ 📊 listings.csv
┃  ┣━ 📊 listings_cleaned.csv
┃  ┣━ 📊 listings_eda.csv
┃  ┗━ 📊 location_features.csv
┣━ 📁 Image_Analysis
┃  ┣━ 📁 Room_Classifier
┃  ┃  ┣━ 📁 dataset
┃  ┃  ┃  ┣━ 📁 test
┃  ┃  ┃  ┃  ┣━ 📁 bathroom
┃  ┃  ┃  ┃  ┃  ┣━ 🖼️ 344886.png
┃  ┃  ┃  ┃  ┃  ┣━ 🖼️ 362603.png
┃  ┃  ┃  ┃  ┃  ┣━ 🖼️ 47536.png
┃  ┃  ┃  ┃  ┃  ┣━ 🖼️ 64604.png
┃  ┃  ┃  ┃  ┃  ┗━ 🖼️ 75806.png
┃  ┃  ┃  ┃  ┣━ 📁 bedroom
┃  ┃  ┃  ┃  ┃  ┣━ 🖼️ 172518.png
┃  ┃  ┃  ┃  ┃  ┣━ 🖼️ 176792.png
┃  ┃  ┃  ┃  ┃  ┣━ 🖼️ 184389.png
┃  ┃  ┃  ┃  ┃  ┣━ 🖼️ 297425.png
┃  ┃  ┃  ┃  ┃  ┗━ 🖼️ 378381.png
┃  ┃  ┃  ┃  ┣━ 📁 dining_room
┃  ┃  ┃  ┃  ┃  ┣━ 🖼️ 237248.png
┃  ┃  ┃  ┃  ┃  ┣━ 🖼️ 288489.png
┃  ┃  ┃  ┃  ┃  ┣━ 🖼️ 293412.png
┃  ┃  ┃  ┃  ┃  ┣━ 🖼️ 361374.png
┃  ┃  ┃  ┃  ┃  ┗━ 🖼️ 40743.png
┃  ┃  ┃  ┃  ┣━ 📁 kitchen
┃  ┃  ┃  ┃  ┃  ┣━ 🖼️ 140929.png
┃  ┃  ┃  ┃  ┃  ┣━ 🖼️ 208710.png
┃  ┃  ┃  ┃  ┃  ┣━ 🖼️ 357867.png
┃  ┃  ┃  ┃  ┃  ┣━ 🖼️ 40294.png
┃  ┃  ┃  ┃  ┃  ┗━ 🖼️ 70120.png
┃  ┃  ┃  ┃  ┣━ 📁 living_room
┃  ┃  ┃  ┃  ┃  ┣━ 🖼️ 196479.png
┃  ┃  ┃  ┃  ┃  ┣━ 🖼️ 262175.png
┃  ┃  ┃  ┃  ┃  ┣━ 🖼️ 341986.png
┃  ┃  ┃  ┃  ┃  ┣━ 🖼️ 342621.png
┃  ┃  ┃  ┃  ┃  ┗━ 🖼️ 351606.png
┃  ┃  ┃  ┃  ┣━ 📁 outside_building
┃  ┃  ┃  ┃  ┃  ┣━ 🖼️ 117987.png
┃  ┃  ┃  ┃  ┃  ┣━ 🖼️ 146549.png
┃  ┃  ┃  ┃  ┃  ┣━ 🖼️ 230611.png
┃  ┃  ┃  ┃  ┃  ┣━ 🖼️ 367517.png
┃  ┃  ┃  ┃  ┃  ┗━ 🖼️ 42196.png
┃  ┃  ┃  ┃  ┗━ 📁 urban_environment
┃  ┃  ┃  ┃     ┣━ 🖼️ 250614.png
┃  ┃  ┃  ┃     ┣━ 🖼️ 259620.png
┃  ┃  ┃  ┃     ┣━ 🖼️ 301067.png
┃  ┃  ┃  ┃     ┣━ 🖼️ 302799.png
┃  ┃  ┃  ┃     ┗━ 🖼️ 34086.png
┃  ┃  ┃  ┣━ 📁 train
┃  ┃  ┃  ┃  ┣━ 📁 bathroom
┃  ┃  ┃  ┃  ┃  ┣━ 🖼️ 163175.png
┃  ┃  ┃  ┃  ┃  ┣━ 🖼️ 257946.png
┃  ┃  ┃  ┃  ┃  ┣━ 🖼️ 56447.png
┃  ┃  ┃  ┃  ┃  ┣━ 🖼️ 70404.png
┃  ┃  ┃  ┃  ┃  ┗━ 🖼️ 97660.png
┃  ┃  ┃  ┃  ┣━ 📁 bedroom
┃  ┃  ┃  ┃  ┃  ┣━ 🖼️ 122548.png
┃  ┃  ┃  ┃  ┃  ┣━ 🖼️ 168067.png
┃  ┃  ┃  ┃  ┃  ┣━ 🖼️ 335924.png
┃  ┃  ┃  ┃  ┃  ┣━ 🖼️ 82987.png
┃  ┃  ┃  ┃  ┃  ┗━ 🖼️ 94450.png
┃  ┃  ┃  ┃  ┣━ 📁 dining_room
┃  ┃  ┃  ┃  ┃  ┣━ 🖼️ 10460.png
┃  ┃  ┃  ┃  ┃  ┣━ 🖼️ 193371.png
┃  ┃  ┃  ┃  ┃  ┣━ 🖼️ 231819.png
┃  ┃  ┃  ┃  ┃  ┣━ 🖼️ 244852.png
┃  ┃  ┃  ┃  ┃  ┗━ 🖼️ 37241.png
┃  ┃  ┃  ┃  ┣━ 📁 kitchen
┃  ┃  ┃  ┃  ┃  ┣━ 🖼️ 203955.png
┃  ┃  ┃  ┃  ┃  ┣━ 🖼️ 345389.png
┃  ┃  ┃  ┃  ┃  ┣━ 🖼️ 369084.png
┃  ┃  ┃  ┃  ┃  ┣━ 🖼️ 43177.png
┃  ┃  ┃  ┃  ┃  ┗━ 🖼️ 509.png
┃  ┃  ┃  ┃  ┣━ 📁 living_room
┃  ┃  ┃  ┃  ┃  ┣━ 🖼️ 345920.png
┃  ┃  ┃  ┃  ┃  ┣━ 🖼️ 349879.png
┃  ┃  ┃  ┃  ┃  ┣━ 🖼️ 367230.png
┃  ┃  ┃  ┃  ┃  ┣━ 🖼️ 369255.png
┃  ┃  ┃  ┃  ┃  ┗━ 🖼️ 46975.png
┃  ┃  ┃  ┃  ┣━ 📁 outside_building
┃  ┃  ┃  ┃  ┃  ┣━ 🖼️ 252710.png
┃  ┃  ┃  ┃  ┃  ┣━ 🖼️ 279438.png
┃  ┃  ┃  ┃  ┃  ┣━ 🖼️ 315751.png
┃  ┃  ┃  ┃  ┃  ┣━ 🖼️ 341597.png
┃  ┃  ┃  ┃  ┃  ┗━ 🖼️ 6718.png
┃  ┃  ┃  ┃  ┗━ 📁 urban_environment
┃  ┃  ┃  ┃     ┣━ 🖼️ 111483.png
┃  ┃  ┃  ┃     ┣━ 🖼️ 252677.png
┃  ┃  ┃  ┃     ┣━ 🖼️ 363505.png
┃  ┃  ┃  ┃     ┣━ 🖼️ 56569.png
┃  ┃  ┃  ┃     ┗━ 🖼️ 83940.png
┃  ┃  ┃  ┗━ 📁 val
┃  ┃  ┃     ┣━ 📁 bathroom
┃  ┃  ┃     ┃  ┣━ 🖼️ 117427.png
┃  ┃  ┃     ┃  ┣━ 🖼️ 312094.png
┃  ┃  ┃     ┃  ┣━ 🖼️ 322430.png
┃  ┃  ┃     ┃  ┣━ 🖼️ 40421.png
┃  ┃  ┃     ┃  ┗━ 🖼️ 93609.png
┃  ┃  ┃     ┣━ 📁 bedroom
┃  ┃  ┃     ┃  ┣━ 🖼️ 132027.png
┃  ┃  ┃     ┃  ┣━ 🖼️ 185213.png
┃  ┃  ┃     ┃  ┣━ 🖼️ 309853.png
┃  ┃  ┃     ┃  ┣━ 🖼️ 340358.png
┃  ┃  ┃     ┃  ┗━ 🖼️ 49433.png
┃  ┃  ┃     ┣━ 📁 dining_room
┃  ┃  ┃     ┃  ┣━ 🖼️ 135433.png
┃  ┃  ┃     ┃  ┣━ 🖼️ 14594.png
┃  ┃  ┃     ┃  ┣━ 🖼️ 371659.png
┃  ┃  ┃     ┃  ┣━ 🖼️ 5315.png
┃  ┃  ┃     ┃  ┗━ 🖼️ 94738.png
┃  ┃  ┃     ┣━ 📁 kitchen
┃  ┃  ┃     ┃  ┣━ 🖼️ 129102.png
┃  ┃  ┃     ┃  ┣━ 🖼️ 262958.png
┃  ┃  ┃     ┃  ┣━ 🖼️ 360228.png
┃  ┃  ┃     ┃  ┣━ 🖼️ 375768.png
┃  ┃  ┃     ┃  ┗━ 🖼️ 74529.png
┃  ┃  ┃     ┣━ 📁 living_room
┃  ┃  ┃     ┃  ┣━ 🖼️ 311146.png
┃  ┃  ┃     ┃  ┣━ 🖼️ 322252.png
┃  ┃  ┃     ┃  ┣━ 🖼️ 374322.png
┃  ┃  ┃     ┃  ┣━ 🖼️ 377391.png
┃  ┃  ┃     ┃  ┗━ 🖼️ 77466.png
┃  ┃  ┃     ┣━ 📁 outside_building
┃  ┃  ┃     ┃  ┣━ 🖼️ 279639.png
┃  ┃  ┃     ┃  ┣━ 🖼️ 285800.png
┃  ┃  ┃     ┃  ┣━ 🖼️ 320467.png
┃  ┃  ┃     ┃  ┣━ 🖼️ 343162.png
┃  ┃  ┃     ┃  ┗━ 🖼️ 72131.png
┃  ┃  ┃     ┗━ 📁 urban_environment
┃  ┃  ┃        ┣━ 🖼️ 224866.png
┃  ┃  ┃        ┣━ 🖼️ 307278.png
┃  ┃  ┃        ┣━ 🖼️ 311484.png
┃  ┃  ┃        ┣━ 🖼️ 365416.png
┃  ┃  ┃        ┗━ 🖼️ 366361.png
┃  ┃  ┣━ 📁 dataset_utils
┃  ┃  ┃  ┣━ 🐍 dataloader.py
┃  ┃  ┃  ┣━ 🐍 dataset.py
┃  ┃  ┃  ┣━ 🐍 download_data.py
┃  ┃  ┃  ┗━ 🐍 readers.py
┃  ┃  ┣━ 📁 inference_utils
┃  ┃  ┃  ┣━ 🐍 room_classifier_model.py
┃  ┃  ┃  ┣━ 🐍 room_classifier_preprocessing.py
┃  ┃  ┃  ┗━ 🐍 test.py
┃  ┃  ┣━ 📁 model_utils
┃  ┃  ┃  ┣━ 🐍 early_stopping.py
┃  ┃  ┃  ┣━ 🐍 model_architecture.py
┃  ┃  ┃  ┗━ 🐍 train.py
┃  ┃  ┣━ 📁 Models
┃  ┃  ┃  ┗━ 📁 resnet18_07_03
┃  ┃  ┃     ┣━ 🖼️ accuracy.png
┃  ┃  ┃     ┣━ 📄 best.onnx
┃  ┃  ┃     ┣━ 📄 best.pt
┃  ┃  ┃     ┣━ 🖼️ f1_score.png
┃  ┃  ┃     ┣━ 📃 logs.txt
┃  ┃  ┃     ┣━ 🖼️ loss.png
┃  ┃  ┃     ┗━ 🖼️ precision_recall.png
┃  ┃  ┣━ 📁 utils
┃  ┃  ┃  ┣━ 🐍 config.py
┃  ┃  ┃  ┗━ 🐍 plots.py
┃  ┃  ┣━ 📓 EDA_dataset.ipynb
┃  ┃  ┣━ 🐍 main.py
┃  ┃  ┗━ 📓 Visualization.ipynb
┃  ┣━ 📓 1. Image_Analysis_Processing.ipynb
┃  ┣━ 📓 2. Image_Analysis_Segmentation.ipynb
┃  ┣━ 📓 3. Image_Analysis_Color_Attributes.ipynb
┃  ┣━ 📓 4. Image_Analysis_EDA.ipynb
┃  ┣━ 📓 5. Image_Analysis_Modelling.ipynb
┃  ┗━ 🐍 airbnb_images_scrapper.py
┣━ 📁 Location
┃  ┣━ 📁 Data
┃  ┃  ┣━ 📊 bus_stops.csv
┃  ┃  ┣━ 📄 neighbourhoods.geojson
┃  ┃  ┣━ 📊 NYPD_crimes.csv
┃  ┃  ┣━ 📄 Point_Of_Interest_dictionary.pdf
┃  ┃  ┣━ 📊 Points_of_Interest.csv
┃  ┃  ┣━ 📊 restaurants.csv
┃  ┃  ┗━ 📊 subway_stations.csv
┃  ┣━ 📓 1. Location_Processing.ipynb
┃  ┣━ 📓 2. Location_EDA.ipynb
┃  ┗━ 📓 3. Location_Modeling.ipynb
┣━ 📁 Metadata
┃  ┣━ 📓 1. Metadata_Processing.ipynb
┃  ┣━ 📓 2. Metadata_EDA.ipynb
┃  ┗━ 📓 3. Metadata_Modeling.ipynb
┣━ 📁 readme_generator
┃  ┣━ 🐍 __init__.py
┃  ┣━ 🐍 b.py
┃  ┣━ 🐍 cli.py
┃  ┣━ 🐍 descriptions_generator.py
┃  ┣━ 🐍 emoji_map.py
┃  ┣━ 🐍 readme_builder.py
┃  ┗━ 🐍 tree_generator.py
┣━ 📄 .gitignore
┣━ 📓 1. Merge listings.ipynb
┣━ 📓 2. EDA.ipynb
┣━ 📓 3. Modeling.ipynb
┗━ 📝 README.md
```

## Files Description
* 📁 `Data`:
    - 📁 `Location`: Contains datasets related to geographical locations and points of interest.
        - 📊 `bus_stops.csv`: Dataset of bus stop locations.
        - 📊 `crimes.csv`: Dataset of crime statistics.
        - 📊 `cultural.csv`: Dataset of cultural points of interest.
        - 📊 `education.csv`: Dataset of educational institutions.
        - 📊 `health.csv`: Dataset of healthcare facilities.
        - 📊 `main_attractions.csv`: Dataset of main tourist attractions.
        - 📊 `recreation.csv`: Dataset of recreational facilities.
        - 📊 `religious.csv`: Dataset of religious institutions.
        - 📊 `restaurants.csv`: Dataset of restaurants.
        - 📊 `subway_stations.csv`: Dataset of subway station locations.
    - 📊 `airbnb_data.csv`: Raw Airbnb data.
    - 📊 `listings.csv`: Airbnb listings dataset.
    - 📊 `listings_cleaned.csv`: Cleaned Airbnb listings dataset.
    - 📊 `listings_eda.csv`: Dataset prepared for exploratory data analysis.
    - 📊 `location_features.csv`: Dataset of location-based features.
* 📁 `Image_Analysis`:
    - 📁 `Room_Classifier`: Contains resources for room classification using images.
        - 📁 `dataset`: Organized datasets for training, testing, and validation.
            - 📁 `test`: Test dataset for room classification.
                - 📁 `bathroom`: Images of bathrooms for testing.
                    - 🖼️ `344886.png`: Bathroom image sample.
                    - 🖼️ `362603.png`: Bathroom image sample.
                    - 🖼️ `47536.png`: Bathroom image sample.
                    - 🖼️ `64604.png`: Bathroom image sample.
                    - 🖼️ `75806.png`: Bathroom image sample.
                - 📁 `bedroom`: Images of bedrooms for testing.
                    - 🖼️ `172518.png`: Bedroom image sample.
                    - 🖼️ `176792.png`: Bedroom image sample.
                    - 🖼️ `184389.png`: Bedroom image sample.
                    - 🖼️ `297425.png`: Bedroom image sample.
                    - 🖼️ `378381.png`: Bedroom image sample.
                - 📁 `dining_room`: Images of dining rooms for testing.
                    - 🖼️ `237248.png`: Dining room image sample.
                    - 🖼️ `288489.png`: Dining room image sample.
                    - 🖼️ `293412.png`: Dining room image sample.
                    - 🖼️ `361374.png`: Dining room image sample.
                    - 🖼️ `40743.png`: Dining room image sample.
                - 📁 `kitchen`: Images of kitchens for testing.
                    - 🖼️ `140929.png`: Kitchen image sample.
                    - 🖼️ `208710.png`: Kitchen image sample.
                    - 🖼️ `357867.png`: Kitchen image sample.
                    - 🖼️ `40294.png`: Kitchen image sample.
                    - 🖼️ `70120.png`: Kitchen image sample.
                - 📁 `living_room`: Images of living rooms for testing.
                    - 🖼️ `196479.png`: Living room image sample.
                    - 🖼️ `262175.png`: Living room image sample.
                    - 🖼️ `341986.png`: Living room image sample.
                    - 🖼️ `342621.png`: Living room image sample.
                    - 🖼️ `351606.png`: Living room image sample.
                - 📁 `outside_building`: Images of building exteriors for testing.
                    - 🖼️ `117987.png`: Exterior image sample.
                    - 🖼️ `146549.png`: Exterior image sample.
                    - 🖼️ `230611.png`: Exterior image sample.
                    - 🖼️ `367517.png`: Exterior image sample.
                    - 🖼️ `42196.png`: Exterior image sample.
                - 📁 `urban_environment`: Images of urban environments for testing.
                    - 🖼️ `250614.png`: Urban environment image sample.
                    - 🖼️ `259620.png`: Urban environment image sample.
                    - 🖼️ `301067.png`: Urban environment image sample.
                    - 🖼️ `302799.png`: Urban environment image sample.
                    - 🖼️ `34086.png`: Urban environment image sample.
            - 📁 `train`: Training dataset for room classification.
                - 📁 `bathroom`: Images of bathrooms for training.
                    - 🖼️ `163175.png`: Bathroom image sample.
                    - 🖼️ `257946.png`: Bathroom image sample.
                    - 🖼️ `56447.png`: Bathroom image sample.
                    - 🖼️ `70404.png`: Bathroom image sample.
                    - 🖼️ `97660.png`: Bathroom image sample.
                - 📁 `bedroom`: Images of bedrooms for training.
                    - 🖼️ `122548.png`: Bedroom image sample.
                    - 🖼️ `168067.png`: Bedroom image sample.
                    - 🖼️ `335924.png`: Bedroom image sample.
                    - 🖼️ `82987.png`: Bedroom image sample.
                    - 🖼️ `94450.png`: Bedroom image sample.
                - 📁 `dining_room`: Images of dining rooms for training.
                    - 🖼️ `10460.png`: Dining room image sample.
                    - 🖼️ `193371.png`: Dining room image sample.
                    - 🖼️ `231819.png`: Dining room image sample.
                    - 🖼️ `244852.png`: Dining room image sample.
                    - 🖼️ `37241.png`: Dining room image sample.
                - 📁 `kitchen`: Images of kitchens for training.
                    - 🖼️ `203955.png`: Kitchen image sample.
                    - 🖼️ `345389.png`: Kitchen image sample.
                    - 🖼️ `369084.png`: Kitchen image sample.
                    - 🖼️ `43177.png`: Kitchen image sample.
                    - 🖼️ `509.png`: Kitchen image sample.
                - 📁 `living_room`: Images of living rooms for training.
                    - 🖼️ `345920.png`: Living room image sample.
                    - 🖼️ `349879.png`: Living room image sample.
                    - 🖼️ `367230.png`: Living room image sample.
                    - 🖼️ `369255.png`: Living room image sample.
                    - 🖼️ `46975.png`: Living room image sample.
                - 📁 `outside_building`: Images of building exteriors for training.
                    - 🖼️ `252710.png`: Exterior image sample.
                    - 🖼️ `279438.png`: Exterior image sample.
                    - 🖼️ `315751.png`: Exterior image sample.
                    - 🖼️ `341597.png`: Exterior image sample.
                    - 🖼️ `6718.png`: Exterior image sample.
                - 📁 `urban_environment`: Images of urban environments for training.
                    - 🖼️ `111483.png`: Urban environment image sample.
                    - 🖼️ `252677.png`: Urban environment image sample.
                    - 🖼️ `363505.png`: Urban environment image sample.
                    - 🖼️ `56569.png`: Urban environment image sample.
                    - 🖼️ `83940.png`: Urban environment image sample.
            - 📁 `val`: Validation dataset for room classification.
                - 📁 `bathroom`: Images of bathrooms for validation.
                    - 🖼️ `117427.png`: Bathroom image sample.
                    - 🖼️ `312094.png`: Bathroom image sample.
                    - 🖼️ `322430.png`: Bathroom image sample.
                    - 🖼️ `40421.png`: Bathroom image sample.
                    - 🖼️ `93609.png`: Bathroom image sample.
                - 📁 `bedroom`: Images of bedrooms for validation.
                    - 🖼️ `132027.png`: Bedroom image sample.
                    - 🖼️ `185213.png`: Bedroom image sample.
                    - 🖼️ `309853.png`: Bedroom image sample.
                    - 🖼️ `340358.png`: Bedroom image sample.
                    - 🖼️ `49433.png`: Bedroom image sample.
                - 📁 `dining_room`: Images of dining rooms for validation.
                    - 🖼️ `135433.png`: Dining room image sample.
                    - 🖼️ `14594.png`: Dining room image sample.
                    - 🖼️ `371659.png`: Dining room image sample.
                    - 🖼️ `5315.png`: Dining room image sample.
                    - 🖼️ `94738.png`: Dining room image sample.
                - 📁 `kitchen`: Images of kitchens for validation.
                    - 🖼️ `129102.png`: Kitchen image sample.
                    - 🖼️ `262958.png`: Kitchen image sample.
                    - 🖼️ `360228.png`: Kitchen image sample.
                    - 🖼️ `375768.png`: Kitchen image sample.
                    - 🖼️ `74529.png`: Kitchen image sample.
                - 📁 `living_room`: Images of living rooms for validation.
                    - 🖼️ `311146.png`: Living room image sample.
                    - 🖼️ `322252.png`: Living room image sample.
                    - 🖼️ `374322.png`: Living room image sample.
                    - 🖼️ `377391.png`: Living room image sample.
                    - 🖼️ `77466.png`: Living room image sample.
                - 📁 `outside_building`: Images of building exteriors for validation.
                    - 🖼️ `279639.png`: Exterior image sample.
                    - 🖼️ `285800.png`: Exterior image sample.
                    - 🖼️ `320467.png`: Exterior image sample.
                    - 🖼️ `343162.png`: Exterior image sample.
                    - 🖼️ `72131.png`: Exterior image sample.
                - 📁 `urban_environment`: Images of urban environments for validation.
                    - 🖼️ `224866.png`: Urban environment image sample.
                    - 🖼️ `307278.png`: Urban environment image sample.
                    - 🖼️ `311484.png`: Urban environment image sample.
                    - 🖼️ `365416.png`: Urban environment image sample.
                    - 🖼️ `366361.png`: Urban environment image sample.
        - 📁 `dataset_utils`: Utilities for handling datasets.
            - 🐍 `dataloader.py`: Script for loading datasets.
            - 🐍 `dataset.py`: Dataset management script.
            - 🐍 `download_data.py`: Script for downloading datasets.
            - 🐍 `readers.py`: Script for reading dataset files.
        - 📁 `inference_utils`: Utilities for inference tasks.
            - 🐍 `room_classifier_model.py`: Room classification model script.
            - 🐍 `room_classifier_preprocessing.py`: Preprocessing script for room classification.
            - 🐍 `test.py`: Script for testing the model.
        - 📁 `model_utils`: Utilities for model training and evaluation.
            - 🐍 `early_stopping.py`: Early stopping implementation.
            - 🐍 `model_architecture.py`: Model architecture definition.
            - 🐍 `train.py`: Model training script.
        - 📁 `Models`: Pre-trained models and related files.
            - 📁 `resnet18_07_03`: Resources for the ResNet18 model.
                - 🖼️ `accuracy.png`: Accuracy plot.
                - 📄 `best.onnx`: Best model in ONNX format.
                - 📄 `best.pt`: Best model in PyTorch format.
                - 🖼️ `f1_score.png`: F1 score plot.
                - 📃 `logs.txt`: Training logs.
                - 🖼️ `loss.png`: Loss plot.
                - 🖼️ `precision_recall.png`: Precision-recall plot.
        - 📁 `utils`: General utility scripts.
            - 🐍 `config.py`: Configuration file.
            - 🐍 `plots.py`: Plotting utilities.
        - 📓 `EDA_dataset.ipynb`: Notebook for exploratory data analysis of the dataset.
        - 🐍 `main.py`: Main script for running the image analysis pipeline.
        - 📓 `Visualization.ipynb`: Notebook for visualizing image analysis results.
    - 📓 `1. Image_Analysis_Processing.ipynb`: Notebook for processing image data.
    - 📓 `2. Image_Analysis_Segmentation.ipynb`: Notebook for segmenting image data.
    - 📓 `3. Image_Analysis_Color_Attributes.ipynb`: Notebook for analyzing color attributes in images.
    - 📓 `4. Image_Analysis_EDA.ipynb`: Notebook for exploratory data analysis of image data.
    - 📓 `5. Image_Analysis_Modelling.ipynb`: Notebook for modeling image data.
    - 🐍 `airbnb_images_scrapper.py`: Script for scraping Airbnb images.
* 📁 `Location`:
    - 📁 `Data`: Contains datasets related to location analysis.
        - 📊 `bus_stops.csv`: Dataset of bus stop locations.
        - 📄 `neighbourhoods.geojson`: GeoJSON file of neighborhoods.
        - 📊 `NYPD_crimes.csv`: Dataset of NYPD crime statistics.
        - 📄 `Point_Of_Interest_dictionary.pdf`: PDF containing a dictionary of points of interest.
        - 📊 `Points_of_Interest.csv`: Dataset of points of interest.
        - 📊 `restaurants.csv`: Dataset of restaurants.
        - 📊 `subway_stations.csv`: Dataset of subway station locations.
    - 📓 `1. Location_Processing.ipynb`: Notebook for processing location data.
    - 📓 `2. Location_EDA.ipynb`: Notebook for exploratory data analysis of location data.
    - 📓 `3. Location_Modeling.ipynb`: Notebook for modeling location data.
* 📁 `Metadata`:
    - 📓 `1. Metadata_Processing.ipynb`: Notebook for processing metadata.
    - 📓 `2. Metadata_EDA.ipynb`: Notebook for exploratory data analysis of metadata.
    - 📓 `3. Metadata_Modeling.ipynb`: Notebook for modeling metadata.
* 📁 `readme_generator`:
    - 🐍 `__init__.py`: Initialization file for the readme generator module.
    - 🐍 `b.py`: Utility script for the readme generator.
    - 🐍 `cli.py`: Command-line interface for the readme generator.
    - 🐍 `descriptions_generator.py`: Script for generating descriptions.
    - 🐍 `emoji_map.py`: Script for mapping emojis to file types.
    - 🐍 `readme_builder.py`: Script for building the README file.
    - 🐍 `tree_generator.py`: Script for generating folder structure trees.
* 📄 `.gitignore`: Git ignore file specifying untracked files.
* 📓 `1. Merge listings.ipynb`: Notebook for merging Airbnb listings.
* 📓 `2. EDA.ipynb`: Notebook for exploratory data analysis.
* 📓 `3. Modeling.ipynb`: Notebook for modeling data.
* 📝 `README.md`: Main README file for the project.

-------------------------------------------
**Last updated on 2025-05-08 19:30**
