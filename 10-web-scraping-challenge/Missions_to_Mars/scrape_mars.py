# SCRAP FUNCTION

#imports
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape():
    executable_path = {'executable_path': ChromeDriverManager().install()}

    # NASA Mars News
    with  Browser('chrome', **executable_path, headless=True) as browser:
        url = 'https://mars.nasa.gov/news/'
        browser.visit(url)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        news_title = soup.find('div', class_='bottom_gradient').text
        news_p = soup.find('div', class_='article_teaser_body').text

    # JPL Mars Images
    with  Browser('chrome', **executable_path, headless=False) as browser:
        url_jpl = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
        browser.visit(url_jpl)
        full_image = browser.find_by_id('full_image')
        full_image.click()
        linked_site = browser.find_link_by_partial_text('more info')
        linked_site.click()
        html_jpl = browser.html
        soup_jpl = BeautifulSoup(html_jpl, 'html.parser')
        partial_url = soup_jpl.select_one('figure.lede a img').get('src')
        featured_image_url = f'https://www.jpl.nasa.gov{partial_url}'

    # Mars Facts
    url_mars_facts = 'https://space-facts.com/mars/'
    tables = pd.read_html(url_mars_facts)
    mars_df = tables[0]
    mars_df_fixing = mars_df.rename(columns={0: 'Description', 1: 'Mars'})
    mars_facts_df = mars_df_fixing.set_index('Description')
    mars_facts_html = mars_facts_df.to_html()

    # Mars Hemispheres
    with  Browser('chrome', **executable_path, headless=False) as browser:
        url_hemisphere = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
        browser.visit(url_hemisphere)
        html_hemisphere = browser.html
        soup_hemisphere = BeautifulSoup(html_hemisphere, 'html.parser')
        results = soup_hemisphere.find_all('div', class_='item')

        hemisphere_image_urls = []
        for result in results:
            title_text = result.h3.text
            browser.click_link_by_partial_text(title_text)
            click_url = browser.url
            browser.visit(click_url)
            html_clicked = browser.html
            soup_clicked = BeautifulSoup(html_clicked, 'html.parser')
            img_url = soup_clicked.find('a', text='Sample')['href']
            hemisphere_image_urls.append({"title": title_text,"img_url": img_url})
            browser.back()        
        hemi_title_text1 = hemisphere_image_urls[0]["title"]
        hemi_title_text2 = hemisphere_image_urls[1]["title"]
        hemi_title_text3 = hemisphere_image_urls[2]["title"]
        hemi_title_text4 = hemisphere_image_urls[3]["title"]
        hemi_image_url1 = hemisphere_image_urls[0]["img_url"]
        hemi_image_url2 = hemisphere_image_urls[1]["img_url"]
        hemi_image_url3 = hemisphere_image_urls[2]["img_url"]
        hemi_image_url4 = hemisphere_image_urls[3]["img_url"] 
        
    return {
        "news_tile": news_title, 
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "mars_facts_html": mars_facts_html,
        "hemi_title_text1": hemi_title_text1,
        "hemi_title_text2": hemi_title_text2,
        "hemi_title_text3": hemi_title_text3,
        "hemi_title_text4": hemi_title_text4,
        "hemi_image_url1": hemi_image_url1,
        "hemi_image_url2": hemi_image_url2,
        "hemi_image_url3": hemi_image_url3,
        "hemi_image_url4": hemi_image_url4,
        }


