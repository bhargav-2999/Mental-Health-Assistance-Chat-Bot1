# import requests
# from bs4 import BeautifulSoup
# import html2text
# import os

# def scrape_to_text(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, "html.parser")

#     # Remove script and style tags
#     for tag in soup(["script", "style"]):
#         tag.decompose()

#     # Get visible text and convert to Markdown
#     html_content = soup.get_text()
#     markdown = html2text.html2text(html_content)

#     return markdown.strip()

# if __name__ == "__main__":
#     os.makedirs("scraped_data", exist_ok=True)

#     url = "https://www.helpguide.org/articles/stress/stress-management.htm"
#     content = scrape_to_text(url)

#     output_path = "scraped_data/stress.txt"
#     with open(output_path, "w", encoding="utf-8") as f:
#         f.write(content)

#     print(f"✅ Saved: {output_path}")
















import requests
from bs4 import BeautifulSoup
import html2text
import os

def scrape_to_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    for tag in soup(["script", "style"]):
        tag.decompose()

    html_content = soup.get_text()
    markdown = html2text.html2text(html_content)
    return markdown.strip()

if __name__ == "__main__":
    os.makedirs("scraped_data", exist_ok=True)

    urls = [
        # Anxiety, Stress, Depression
        "https://www.helpguide.org/articles/stress/stress-management.htm",
        "https://www.helpguide.org/articles/anxiety/anxiety-disorders-and-anxiety-attacks.htm",
        "https://www.helpguide.org/articles/depression/coping-with-depression.htm",

        # Mindfulness, Meditation, Emotional Wellness
        "https://www.verywellmind.com/how-to-practice-mindfulness-3145187",
        "https://www.mindful.org/what-is-mindfulness/",
        "https://www.headspace.com/mindfulness",
        "https://www.psychologytoday.com/us/blog/pieces-mind/202303/why-emotional-awareness-matters",

        # Sleep and Self-Care
        "https://www.sleepfoundation.org/sleep-hygiene",
        "https://www.sleepfoundation.org/mental-health",
        "https://www.nhs.uk/every-mind-matters/mental-wellbeing-tips/self-care/ways-to-improve-your-mental-wellbeing/",

        # Mental Resilience, CBT, Cognitive Skills
        "https://www.therapistaid.com/worksheets/cognitive-distortions.pdf",
        "https://positivepsychology.com/cbt-cognitive-behavioral-therapy-techniques-worksheets/",
        "https://www.psychologytools.com/resource/cognitive-restructuring/",
        "https://www.mentalhealth.org.uk/explore-mental-health/publications/guide-how-to-stress-less",

        # Relationships, Connection
        "https://www.mind.org.uk/information-support/types-of-mental-health-problems/relationships-and-mental-health/",
        "https://www.verywellmind.com/how-to-build-social-connection-5192947",
        "https://www.betterup.com/blog/strong-relationships",

        # Positivity and Gratitude
        "https://www.mind.org.uk/information-support/types-of-mental-health-problems/self-esteem/",
        "https://www.psychologytoday.com/us/blog/words-matter/202112/the-science-gratitude",
        "https://www.healthline.com/health/mental-health/positive-self-talk"
    ]

    for i, url in enumerate(urls):
        try:
            content = scrape_to_text(url)
            with open(f"scraped_data/doc_{i+1}.txt", "w", encoding="utf-8") as f:
                f.write(content)
            print(f"✅ Saved: scraped_data/doc_{i+1}.txt")
        except Exception as e:
            print(f"❌ Failed to scrape {url}: {e}")
