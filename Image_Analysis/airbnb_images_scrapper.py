import os, time, requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from typing import List, Union

class AirbnbImagesScrapping:
    def __init__(self) -> None:
        """
        Initialize the AirbnbImagesScrapping class.
        """
        self.driver: webdriver.Chrome = self.selenium_connection()
    
    def selenium_connection(self) -> webdriver.Chrome:
        """
        Create a connection to the Chrome browser using Selenium.

        Returns:
            webdriver.Chrome: The Selenium driver.
        """
        os.system("taskkill /im chrome.exe /f") # Close all chrome processes
        options = webdriver.ChromeOptions()
        options.add_argument(r"--user-data-dir={}".format(os.environ['Chrome_User_Data']))
        options.add_argument(r'--profile-directory=Profile 1')
        prefs = {"profile.default_content_setting_values.geolocation" :2}
        options.add_experimental_option("prefs",prefs)
        driver = webdriver.Chrome(options=options)
        return driver
    
    def run(self, listing_url: str) -> Union[List[str], str]:
        """
        Run the AirbnbImagesScrapping class to scrape images from an Airbnb listing.
        
        Args:
            listing_url (str): The URL of the Airbnb listing.
        
        Returns:
            Union[List[str], str]: A list of image URLs or an error message.
        """
        if not self._check_if_exists(listing_url):
            return "URL not found"
        results = self.scrape_images(listing_url)
        return results
    
    def scrape_images(self, listing_url: str) -> Union[List[str], str]:
        """
        Scrape images from an Airbnb listing.
        
        Args:
            listing_url (str): The URL of the Airbnb listing.
        
        Returns:
            Union[List[str], str]: A list of image URLs or an error message.
        """
        try:
            self._navigate_to_listing(listing_url)
            navigation_result = self._navigate_to_all_images()
            if navigation_result == "Image found":
                images, room_types = self._get_single_image_url()
            else:
                images, room_types = self._get_images_urls()
            return {
                "images": images,
                "room_types": room_types
            }
        except:
            return "Failed to scrape images"
    
    @staticmethod
    def _check_if_exists(listing_url: str) -> bool:
        """
        Check if the listing URL exists.

        Args:
            listing_url (str): The URL of the Airbnb listing.
        
        Returns:
            bool: True if the URL exists, False otherwise.
        """
        webpage_html = requests.get(listing_url)
        if webpage_html.status_code < 400:
            return True
        return False
    
    def _navigate_to_listing(self, listing_url: str) -> None:
        """
        Navigate to the Airbnb listing page.
        
        Args:
            listing_url (str): The URL of the Airbnb listing.
        """
        try:
            self.driver.get(listing_url)
        except:
            raise Exception("The listing page is not loading")
    
    def _navigate_to_all_images(self) -> str:
        """
        Navigate to the section with all images (option 1) or check if there is only one image (option 2).
        
        Returns:
            str: "Image found" if there is only one image, "Button clicked" if the button was clicked.
        """
        image_x_path = '/html/body/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[1]/main/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/picture/img'
        show_all_images_button_x_path = '//*[@id="site-content"]/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div/div[2]/button'
        try:
            #Option 1: There is a button to show all images
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, show_all_images_button_x_path)))
        except:
            try:
                #Option 2: There is only one image and no button to show all images
                WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, image_x_path)))
                return "Image found"
            except:
                raise Exception("The show all images button is not loading or the image is not loading")
        try:
            show_all_images_button = self.driver.find_element("xpath", show_all_images_button_x_path)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(show_all_images_button))
            show_all_images_button.click()
            return "Button clicked"
        except:
            raise Exception("The show all images button is not clickable")
    
    def _get_single_image_url(self) -> List[str]:
        """
        Get the URL of the single image.

        Returns:
            List[str]: The URL of the single image.
        """
        image_x_path = '/html/body/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[1]/main/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/picture/img'
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, image_x_path)))
            image = self.driver.find_element("xpath", image_x_path)
            image_url = image.get_attribute("src")
            return [image_url], [""]
        except Exception as e:
            raise Exception(f"Failed to retrieve the single image: {e}")
            
    def _get_images_urls(self) -> List[str]:
        """
        Get the URLs of all images.

        Returns:
            List[str]: The URLs of all images.
        """
        images_section = self._get_images_section()
        images = self._scroll_and_collect_images(images_section)
        return images
    
    def _get_images_section(self) -> webdriver.Chrome:
        """
        Get the section with all images.

        Returns:
            webdriver.Chrome: The section with all images.
        """
        images_section_xpath = "/html/body/div[9]/div/div/section/div/div/div[2]/div/section/div/div/div/div/section/div/div/div[2]/div/div[2]/div"
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, images_section_xpath)))
            return self.driver.find_element(By.XPATH, images_section_xpath)
        except Exception as e:
            raise Exception(f"Failed to load the images section: {e}")

    def _scroll_and_collect_images(self, images_section: webdriver.Chrome) -> List[str]:
        """
        Scroll through the images section and collect all image URLs.

        Args:
            images_section (webdriver.Chrome): The section with all images.
        
        Returns:
            List[str]: The URLs of all images.
        """
        all_images, all_room_types = [], []
        counter = 0
        images_scroll = self._get_images_from_section(images_section)
        while True:
            last_image = images_scroll[-1]
            ActionChains(self.driver).move_to_element(last_image).perform()
            time.sleep(0.3)
            images_scroll = self._get_images_from_section(images_section)
            new_images = [image.get_attribute("src") for image in images_scroll]
            room_types = [image.get_attribute("alt") for image in images_scroll]
            all_images.extend(new_images)
            all_room_types.extend(room_types)
            if images_scroll[-1] == last_image:
                counter += 1
                if counter == 3:
                    break
            else:
                counter = 0
        final_images, final_room_types = self._remove_duplicates(all_images, all_room_types)
        return final_images, final_room_types

    def _get_images_from_section(self, section: webdriver.Chrome) -> List[webdriver.Chrome]:
        """
        Get the images from the section.

        Args:
            section (webdriver.Chrome): The section with all images.
        
        Returns:
            List[webdriver.Chrome]: The images from the section.
        """
        try:
            images = section.find_elements(By.TAG_NAME, "img")
            if not images:
                raise Exception("No images found in the section.")
            return images
        except Exception as e:
            raise Exception(f"Failed to retrieve images from the section: {e}")
    
    def _remove_duplicates(self, all_images: List[str], all_room_types: List[str]) -> List[str]:
        """
        Remove duplicate elements from the list of images and room types.

        Args:
            all_images (List[str]): The list of all images.
            all_room_types (List[str]): The list of all room types.
        
        Returns:
            List[str]: The list of unique images.
        """
        unique_images, unique_room_types = [], []
        for i in range(len(all_images)):
            if all_images[i] not in unique_images:
                unique_images.append(all_images[i])
                unique_room_types.append(all_room_types[i])
        return unique_images, unique_room_types