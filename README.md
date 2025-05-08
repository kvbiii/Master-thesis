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
📁 Data:<br>
&nbsp;&nbsp;&nbsp;&nbsp;📁 Location:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📊 bus_stops.csv:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📊 crimes.csv:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📊 cultural.csv:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📊 education.csv:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📊 health.csv:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📊 main_attractions.csv:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📊 recreation.csv:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📊 religious.csv:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📊 restaurants.csv:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📊 subway_stations.csv:
&nbsp;&nbsp;&nbsp;&nbsp;📊 airbnb_data.csv:
&nbsp;&nbsp;&nbsp;&nbsp;📊 listings.csv:
&nbsp;&nbsp;&nbsp;&nbsp;📊 listings_cleaned.csv:
&nbsp;&nbsp;&nbsp;&nbsp;📊 listings_eda.csv:
&nbsp;&nbsp;&nbsp;&nbsp;📊 location_features.csv:
📁 Image_Analysis:
&nbsp;&nbsp;&nbsp;&nbsp;📁 Room_Classifier:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📁 dataset:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📁 test:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📁 bathroom:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 344886.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 362603.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 47536.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 64604.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 75806.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📁 bedroom:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 172518.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 176792.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 184389.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 297425.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 378381.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📁 dining_room:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 237248.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 288489.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 293412.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 361374.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 40743.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📁 kitchen:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 140929.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 208710.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 357867.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 40294.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 70120.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📁 living_room:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 196479.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 262175.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 341986.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 342621.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 351606.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📁 outside_building:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 117987.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 146549.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 230611.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 367517.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 42196.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📁 urban_environment:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 250614.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 259620.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 301067.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 302799.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 34086.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📁 train:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📁 bathroom:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 163175.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 257946.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 56447.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 70404.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 97660.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📁 bedroom:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 122548.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 168067.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 335924.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 82987.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 94450.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📁 dining_room:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 10460.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 193371.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 231819.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 244852.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 37241.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📁 kitchen:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 203955.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 345389.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 369084.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 43177.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 509.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📁 living_room:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 345920.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 349879.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 367230.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 369255.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 46975.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📁 outside_building:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 252710.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 279438.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 315751.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 341597.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 6718.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📁 urban_environment:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 111483.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 252677.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 363505.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 56569.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 83940.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📁 val:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📁 bathroom:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 117427.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 312094.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 322430.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 40421.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 93609.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📁 bedroom:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 132027.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 185213.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 309853.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 340358.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 49433.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📁 dining_room:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 135433.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 14594.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 371659.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 5315.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 94738.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📁 kitchen:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 129102.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 262958.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 360228.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 375768.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 74529.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📁 living_room:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 311146.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 322252.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 374322.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 377391.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 77466.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📁 outside_building:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 279639.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 285800.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 320467.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 343162.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 72131.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📁 urban_environment:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 224866.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 307278.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 311484.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 365416.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ 366361.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📁 dataset_utils:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🐍 dataloader.py:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🐍 dataset.py:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🐍 download_data.py:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🐍 readers.py:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📁 inference_utils:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🐍 room_classifier_model.py:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🐍 room_classifier_preprocessing.py:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🐍 test.py:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📁 model_utils:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🐍 early_stopping.py:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🐍 model_architecture.py:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🐍 train.py:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📁 Models:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📁 resnet18_07_03:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ accuracy.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📄 best.onnx:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📄 best.pt:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ f1_score.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📃 logs.txt:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ loss.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🖼️ precision_recall.png:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📁 utils:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🐍 config.py:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🐍 plots.py:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📓 EDA_dataset.ipynb:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🐍 main.py:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📓 Visualization.ipynb:
&nbsp;&nbsp;&nbsp;&nbsp;📓 1. Image_Analysis_Processing.ipynb:
&nbsp;&nbsp;&nbsp;&nbsp;📓 2. Image_Analysis_Segmentation.ipynb:
&nbsp;&nbsp;&nbsp;&nbsp;📓 3. Image_Analysis_Color_Attributes.ipynb:
&nbsp;&nbsp;&nbsp;&nbsp;📓 4. Image_Analysis_EDA.ipynb:
&nbsp;&nbsp;&nbsp;&nbsp;📓 5. Image_Analysis_Modelling.ipynb:
&nbsp;&nbsp;&nbsp;&nbsp;🐍 airbnb_images_scrapper.py:
📁 Location:
&nbsp;&nbsp;&nbsp;&nbsp;📁 Data:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📊 bus_stops.csv:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📄 neighbourhoods.geojson:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📊 NYPD_crimes.csv:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📄 Point_Of_Interest_dictionary.pdf:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📊 Points_of_Interest.csv:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📊 restaurants.csv:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📊 subway_stations.csv:
&nbsp;&nbsp;&nbsp;&nbsp;📓 1. Location_Processing.ipynb:
&nbsp;&nbsp;&nbsp;&nbsp;📓 2. Location_EDA.ipynb:
&nbsp;&nbsp;&nbsp;&nbsp;📓 3. Location_Modeling.ipynb:
📁 Metadata:
&nbsp;&nbsp;&nbsp;&nbsp;📓 1. Metadata_Processing.ipynb:
&nbsp;&nbsp;&nbsp;&nbsp;📓 2. Metadata_EDA.ipynb:
&nbsp;&nbsp;&nbsp;&nbsp;📓 3. Metadata_Modeling.ipynb:
📁 readme_generator:
&nbsp;&nbsp;&nbsp;&nbsp;🐍 __init__.py:
&nbsp;&nbsp;&nbsp;&nbsp;🐍 b.py:
&nbsp;&nbsp;&nbsp;&nbsp;🐍 cli.py:
&nbsp;&nbsp;&nbsp;&nbsp;🐍 descriptions_generator.py:
&nbsp;&nbsp;&nbsp;&nbsp;🐍 emoji_map.py:
&nbsp;&nbsp;&nbsp;&nbsp;🐍 readme_builder.py:
&nbsp;&nbsp;&nbsp;&nbsp;🐍 tree_generator.py:
📄 .gitignore:
📓 1. Merge listings.ipynb:
📓 2. EDA.ipynb:
📓 3. Modeling.ipynb:
📝 README.md:

## Installation

## Usage

**Last updated on 2025-05-08 19:02**
