# 

## Overview
Describe your project here

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
📁 Data:
    - 📁 Location:
        - 📊 bus_stops.csv:
        - 📊 crimes.csv:
        📊 cultural.csv:
        📊 education.csv:
        📊 health.csv:
        📊 main_attractions.csv:
        📊 recreation.csv:
        📊 religious.csv:
        📊 restaurants.csv:
        📊 subway_stations.csv:
    📊 airbnb_data.csv:
    📊 listings.csv:
    📊 listings_cleaned.csv:
    📊 listings_eda.csv:
    📊 location_features.csv:
📁 Image_Analysis:
    📁 Room_Classifier:
        📁 dataset:
            📁 test:
                📁 bathroom:
                    🖼️ 344886.png:
                    🖼️ 362603.png:
                    🖼️ 47536.png:
                    🖼️ 64604.png:
                    🖼️ 75806.png:
                📁 bedroom:
                    🖼️ 172518.png:
                    🖼️ 176792.png:
                    🖼️ 184389.png:
                    🖼️ 297425.png:
                    🖼️ 378381.png:
                📁 dining_room:
                    🖼️ 237248.png:
                    🖼️ 288489.png:
                    🖼️ 293412.png:
                    🖼️ 361374.png:
                    🖼️ 40743.png:
                📁 kitchen:
                    🖼️ 140929.png:
                    🖼️ 208710.png:
                    🖼️ 357867.png:
                    🖼️ 40294.png:
                    🖼️ 70120.png:
                📁 living_room:
                    🖼️ 196479.png:
                    🖼️ 262175.png:
                    🖼️ 341986.png:
                    🖼️ 342621.png:
                    🖼️ 351606.png:
                📁 outside_building:
                    🖼️ 117987.png:
                    🖼️ 146549.png:
                    🖼️ 230611.png:
                    🖼️ 367517.png:
                    🖼️ 42196.png:
                📁 urban_environment:
                    🖼️ 250614.png:
                    🖼️ 259620.png:
                    🖼️ 301067.png:
                    🖼️ 302799.png:
                    🖼️ 34086.png:
            📁 train:
                📁 bathroom:
                    🖼️ 163175.png:
                    🖼️ 257946.png:
                    🖼️ 56447.png:
                    🖼️ 70404.png:
                    🖼️ 97660.png:
                📁 bedroom:
                    🖼️ 122548.png:
                    🖼️ 168067.png:
                    🖼️ 335924.png:
                    🖼️ 82987.png:
                    🖼️ 94450.png:
                📁 dining_room:
                    🖼️ 10460.png:
                    🖼️ 193371.png:
                    🖼️ 231819.png:
                    🖼️ 244852.png:
                    🖼️ 37241.png:
                📁 kitchen:
                    🖼️ 203955.png:
                    🖼️ 345389.png:
                    🖼️ 369084.png:
                    🖼️ 43177.png:
                    🖼️ 509.png:
                📁 living_room:
                    🖼️ 345920.png:
                    🖼️ 349879.png:
                    🖼️ 367230.png:
                    🖼️ 369255.png:
                    🖼️ 46975.png:
                📁 outside_building:
                    🖼️ 252710.png:
                    🖼️ 279438.png:
                    🖼️ 315751.png:
                    🖼️ 341597.png:
                    🖼️ 6718.png:
                📁 urban_environment:
                    🖼️ 111483.png:
                    🖼️ 252677.png:
                    🖼️ 363505.png:
                    🖼️ 56569.png:
                    🖼️ 83940.png:
            📁 val:
                📁 bathroom:
                    🖼️ 117427.png:
                    🖼️ 312094.png:
                    🖼️ 322430.png:
                    🖼️ 40421.png:
                    🖼️ 93609.png:
                📁 bedroom:
                    🖼️ 132027.png:
                    🖼️ 185213.png:
                    🖼️ 309853.png:
                    🖼️ 340358.png:
                    🖼️ 49433.png:
                📁 dining_room:
                    🖼️ 135433.png:
                    🖼️ 14594.png:
                    🖼️ 371659.png:
                    🖼️ 5315.png:
                    🖼️ 94738.png:
                📁 kitchen:
                    🖼️ 129102.png:
                    🖼️ 262958.png:
                    🖼️ 360228.png:
                    🖼️ 375768.png:
                    🖼️ 74529.png:
                📁 living_room:
                    🖼️ 311146.png:
                    🖼️ 322252.png:
                    🖼️ 374322.png:
                    🖼️ 377391.png:
                    🖼️ 77466.png:
                📁 outside_building:
                    🖼️ 279639.png:
                    🖼️ 285800.png:
                    🖼️ 320467.png:
                    🖼️ 343162.png:
                    🖼️ 72131.png:
                📁 urban_environment:
                    🖼️ 224866.png:
                    🖼️ 307278.png:
                    🖼️ 311484.png:
                    🖼️ 365416.png:
                    🖼️ 366361.png:
        📁 dataset_utils:
            🐍 dataloader.py:
            🐍 dataset.py:
            🐍 download_data.py:
            🐍 readers.py:
        📁 inference_utils:
            🐍 room_classifier_model.py:
            🐍 room_classifier_preprocessing.py:
            🐍 test.py:
        📁 model_utils:
            🐍 early_stopping.py:
            🐍 model_architecture.py:
            🐍 train.py:
        📁 Models:
            📁 resnet18_07_03:
                🖼️ accuracy.png:
                📄 best.onnx:
                📄 best.pt:
                🖼️ f1_score.png:
                📃 logs.txt:
                🖼️ loss.png:
                🖼️ precision_recall.png:
        📁 utils:
            🐍 config.py:
            🐍 plots.py:
        📓 EDA_dataset.ipynb:
        🐍 main.py:
        📓 Visualization.ipynb:
    📓 1. Image_Analysis_Processing.ipynb:
    📓 2. Image_Analysis_Segmentation.ipynb:
    📓 3. Image_Analysis_Color_Attributes.ipynb:
    📓 4. Image_Analysis_EDA.ipynb:
    📓 5. Image_Analysis_Modelling.ipynb:
    🐍 airbnb_images_scrapper.py:
📁 Location:
    📁 Data:
        📊 bus_stops.csv:
        📄 neighbourhoods.geojson:
        📊 NYPD_crimes.csv:
        📄 Point_Of_Interest_dictionary.pdf:
        📊 Points_of_Interest.csv:
        📊 restaurants.csv:
        📊 subway_stations.csv:
    📓 1. Location_Processing.ipynb:
    📓 2. Location_EDA.ipynb:
    📓 3. Location_Modeling.ipynb:
📁 Metadata:
    📓 1. Metadata_Processing.ipynb:
    📓 2. Metadata_EDA.ipynb:
    📓 3. Metadata_Modeling.ipynb:
📁 readme_generator:
    🐍 __init__.py:
    🐍 b.py:
    🐍 cli.py:
    🐍 descriptions_generator.py:
    🐍 emoji_map.py:
    🐍 readme_builder.py:
    🐍 tree_generator.py:
📄 .gitignore:
📓 1. Merge listings.ipynb:
📓 2. EDA.ipynb:
📓 3. Modeling.ipynb:
📝 README.md:

## Installation

## Usage

**Last updated on 2025-05-07 19:43**
