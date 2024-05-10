import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import re
from main_Doc import *

def extract_question_number(html_content):
    match = re.search(r'Question #:\s*(\d+)', html_content)
    if match:
        return match.group(1)
    else:
        return None

def scrape_question(url, driver, output_file):
    driver.get(url)
    time.sleep(10)  # Wait for the page to load (adjust as needed)
    try:
        # Check if the page contains the desired text
        if "Professional Data Engineer" in driver.page_source:
            # Extract question number from the URL
            question_number = extract_question_number(driver.page_source)


            # Extract question and possible answers
            question_element = driver.find_element_by_class_name('question-body')
            question = question_element.find_element_by_tag_name('p').text.strip()

            answers_elements = driver.find_elements_by_class_name('multi-choice-item')
            answers = [answer.text.strip() for answer in answers_elements]

            # Save to file
            with open(output_file+".txt", 'a', encoding='utf-8') as file:
                file.write(f"Link: {url}\n")
                file.write(f"Question Number: {question_number}\n")
                file.write(f"Question: {question}\n")
                file.write("Possible Answers:\n")
                for idx, answer in enumerate(answers, start=1):
                    file.write(f"{idx}. {answer}\n")
                file.write("\n" + "=" * 50 + "\n")  # Just for better separation of results
                # Check if the page contains the desired text
            print("Data")
        elif "Professional Machine Learning Engineer" in driver.page_source:
            # Extract question number from the URL
            question_number = extract_question_number(driver.page_source)

            # Extract question and possible answers
            question_element = driver.find_element_by_class_name('question-body')
            question = question_element.find_element_by_tag_name('p').text.strip()

            answers_elements = driver.find_elements_by_class_name('multi-choice-item')
            answers = [answer.text.strip() for answer in answers_elements]

            # Save to file
            with open(output_file+'ML.txt', 'a', encoding='utf-8') as file:
                file.write(f"Link: {url}\n")
                file.write(f"Question Number: {question_number}\n")
                file.write(f"Question: {question}\n")
                file.write("Possible Answers:\n")
                for idx, answer in enumerate(answers, start=1):
                    file.write(f"{idx}. {answer}\n")
                file.write("\n" + "=" * 50 + "\n")  # Just for better separation of results
            print("ML")
        elif "Professional Cloud Database Engineer" in driver.page_source:
            # Extract question number from the URL
            question_number = extract_question_number(driver.page_source)

            # Extract question and possible answers
            question_element = driver.find_element_by_class_name('question-body')
            question = question_element.find_element_by_tag_name('p').text.strip()

            answers_elements = driver.find_elements_by_class_name('multi-choice-item')
            answers = [answer.text.strip() for answer in answers_elements]

            # Save to file
            with open(output_file+'BBDD.txt', 'a', encoding='utf-8') as file:
                file.write(f"Link: {url}\n")
                file.write(f"Question Number: {question_number}\n")
                file.write(f"Question: {question}\n")
                file.write("Possible Answers:\n")
                for idx, answer in enumerate(answers, start=1):
                    file.write(f"{idx}. {answer}\n")
                file.write("\n" + "=" * 50 + "\n")  # Just for better separation of results
            print("BBDD")
        elif "Professional Cloud Security Engineer" in driver.page_source:
            # Extract question number from the URL
            question_number = extract_question_number(driver.page_source)

            # Extract question and possible answers
            question_element = driver.find_element_by_class_name('question-body')
            question = question_element.find_element_by_tag_name('p').text.strip()

            answers_elements = driver.find_elements_by_class_name('multi-choice-item')
            answers = [answer.text.strip() for answer in answers_elements]

            # Save to file
            with open(output_file+'SEC.txt', 'a', encoding='utf-8') as file:
                file.write(f"Link: {url}\n")
                file.write(f"Question Number: {question_number}\n")
                file.write(f"Question: {question}\n")
                file.write("Possible Answers:\n")
                for idx, answer in enumerate(answers, start=1):
                    file.write(f"{idx}. {answer}\n")
                file.write("\n" + "=" * 50 + "\n")  # Just for better separation of results
            print("SEC")
        elif "Professional Cloud DevOps Engineer" in driver.page_source:
            # Extract question number from the URL
            question_number = extract_question_number(driver.page_source)

            # Extract question and possible answers
            question_element = driver.find_element_by_class_name('question-body')
            question = question_element.find_element_by_tag_name('p').text.strip()

            answers_elements = driver.find_elements_by_class_name('multi-choice-item')
            answers = [answer.text.strip() for answer in answers_elements]

            # Save to file
            with open(output_file+'DevOps.txt', 'a', encoding='utf-8') as file:
                file.write(f"Link: {url}\n")
                file.write(f"Question Number: {question_number}\n")
                file.write(f"Question: {question}\n")
                file.write("Possible Answers:\n")
                for idx, answer in enumerate(answers, start=1):
                    file.write(f"{idx}. {answer}\n")
                file.write("\n" + "=" * 50 + "\n")  # Just for better separation of results
            print("DevOps")
        elif "Professional Cloud Developer" in driver.page_source:
            # Extract question number from the URL
            question_number = extract_question_number(driver.page_source)

            # Extract question and possible answers
            question_element = driver.find_element_by_class_name('question-body')
            question = question_element.find_element_by_tag_name('p').text.strip()

            answers_elements = driver.find_elements_by_class_name('multi-choice-item')
            answers = [answer.text.strip() for answer in answers_elements]

            # Save to file
            with open(output_file+'Dev.txt', 'a', encoding='utf-8') as file:
                file.write(f"Link: {url}\n")
                file.write(f"Question Number: {question_number}\n")
                file.write(f"Question: {question}\n")
                file.write("Possible Answers:\n")
                for idx, answer in enumerate(answers, start=1):
                    file.write(f"{idx}. {answer}\n")
                file.write("\n" + "=" * 50 + "\n")  # Just for better separation of results
            print("Dev")
        elif "Professional Cloud Network Engineer" in driver.page_source:
            # Extract question number from the URL
            question_number = extract_question_number(driver.page_source)

            # Extract question and possible answers
            question_element = driver.find_element_by_class_name('question-body')
            question = question_element.find_element_by_tag_name('p').text.strip()

            answers_elements = driver.find_elements_by_class_name('multi-choice-item')
            answers = [answer.text.strip() for answer in answers_elements]

            # Save to file
            with open(output_file+'Net.txt', 'a', encoding='utf-8') as file:
                file.write(f"Link: {url}\n")
                file.write(f"Question Number: {question_number}\n")
                file.write(f"Question: {question}\n")
                file.write("Possible Answers:\n")
                for idx, answer in enumerate(answers, start=1):
                    file.write(f"{idx}. {answer}\n")
                file.write("\n" + "=" * 50 + "\n")  # Just for better separation of results
            print("Net")
        elif "Professional Google Workspace Administrator" in driver.page_source:
            # Extract question number from the URL
            question_number = extract_question_number(driver.page_source)

            # Extract question and possible answers
            question_element = driver.find_element_by_class_name('question-body')
            question = question_element.find_element_by_tag_name('p').text.strip()

            answers_elements = driver.find_elements_by_class_name('multi-choice-item')
            answers = [answer.text.strip() for answer in answers_elements]

            # Save to file
            with open(output_file+'Work.txt', 'a', encoding='utf-8') as file:
                file.write(f"Link: {url}\n")
                file.write(f"Question Number: {question_number}\n")
                file.write(f"Question: {question}\n")
                file.write("Possible Answers:\n")
                for idx, answer in enumerate(answers, start=1):
                    file.write(f"{idx}. {answer}\n")
                file.write("\n" + "=" * 50 + "\n")  # Just for better separation of results
            print("Work")
        elif "Exam Professional Cloud Architect" in driver.page_source:
            # Extract question number from the URL
            question_number = extract_question_number(driver.page_source)

            # Extract question and possible answers
            question_element = driver.find_element_by_class_name('question-body')
            question = question_element.find_element_by_tag_name('p').text.strip()

            answers_elements = driver.find_elements_by_class_name('multi-choice-item')
            answers = [answer.text.strip() for answer in answers_elements]

            # Save to file
            with open(output_file+'Archi.txt', 'a', encoding='utf-8') as file:
                file.write(f"Link: {url}\n")
                file.write(f"Question Number: {question_number}\n")
                file.write(f"Question: {question}\n")
                file.write("Possible Answers:\n")
                for idx, answer in enumerate(answers, start=1):
                    file.write(f"{idx}. {answer}\n")
                file.write("\n" + "=" * 50 + "\n")  # Just for better separation of results
            print("Archi")
        elif "Exam AWS Certified Cloud Practitioner" in driver.page_source:
            # Extract question number from the URL
            question_number = extract_question_number(driver.page_source)

            # Extract question and possible answers
            question_element = driver.find_element_by_class_name('question-body')
            question = question_element.find_element_by_tag_name('p').text.strip()

            answers_elements = driver.find_elements_by_class_name('multi-choice-item')
            answers = [answer.text.strip() for answer in answers_elements]

            # Save to file
            with open(output_file+'AWSCCP.txt', 'a', encoding='utf-8') as file:
                file.write(f"Link: {url}\n")
                file.write(f"Question Number: {question_number}\n")
                file.write(f"Question: {question}\n")
                file.write("Possible Answers:\n")
                for idx, answer in enumerate(answers, start=1):
                    file.write(f"{idx}. {answer}\n")
                file.write("\n" + "=" * 50 + "\n")  # Just for better separation of results
            print("AWSCCP")
        elif "AWS" in driver.page_source:
            # Extract question number from the URL
            question_number = extract_question_number(driver.page_source)

            # Extract question and possible answers
            question_element = driver.find_element_by_class_name('question-body')
            question = question_element.find_element_by_tag_name('p').text.strip()

            answers_elements = driver.find_elements_by_class_name('multi-choice-item')
            answers = [answer.text.strip() for answer in answers_elements]

            # Save to file
            with open(output_file+'AWS.txt', 'a', encoding='utf-8') as file:
                file.write(f"Link: {url}\n")
                file.write(f"Question Number: {question_number}\n")
                file.write(f"Question: {question}\n")
                file.write("Possible Answers:\n")
                for idx, answer in enumerate(answers, start=1):
                    file.write(f"{idx}. {answer}\n")
                file.write("\n" + "=" * 50 + "\n")  # Just for better separation of results

        elif "Azure" in driver.page_source:
            # Extract question number from the URL
            question_number = extract_question_number(driver.page_source)

            # Extract question and possible answers
            question_element = driver.find_element_by_class_name('question-body')
            question = question_element.find_element_by_tag_name('p').text.strip()

            answers_elements = driver.find_elements_by_class_name('multi-choice-item')
            answers = [answer.text.strip() for answer in answers_elements]

            # Save to file
            with open(output_file+'Azure.txt', 'a', encoding='utf-8') as file:
                file.write(f"Link: {url}\n")
                file.write(f"Question Number: {question_number}\n")
                file.write(f"Question: {question}\n")
                file.write("Possible Answers:\n")
                for idx, answer in enumerate(answers, start=1):
                    file.write(f"{idx}. {answer}\n")
                file.write("\n" + "=" * 50 + "\n")  # Just for better separation of results

        else:
            print(f"Text not found in the page: {url}")
    except Exception as e:
        print(f"An error occurred: {e}")

def organize():
    file_path = "questionsArchi.txt"
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    # Split the text into sections based on the "Question Number" pattern
    sections = re.split(r'={50,}', text)[1:]

    # Organize questions by question number
    organized_questions = {}
    for section in sections:
        match = re.search(r'Question Number: (\d+)', section)
        if match:
            question_number = int(match.group(1))
            organized_questions[question_number] = section.strip()

    # Save organized questions to a new text file
    output_file_path = "organized_questionsArchi.txt"
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        for question_number, question_text in sorted(organized_questions.items()):

            output_file.write(question_text + "\n" + "=" * 50 + "\n")

    print(f"Organized questions have been saved to: {output_file_path}")

def botPreg(start_number, end_number, base_url, driver, output_file):
    for number in range(start_number, end_number):
        url = f"{base_url}{number}-exam-professional-data-engineer-topic-1-question-260-discussion/"
        scrape_question(url, driver, output_file)

def main():
    # Set the path to your GeckoDriver executable
    # You can download it from: https://github.com/mozilla/geckodriver/releases
    gecko_driver_path = 'path/to/geckodriver'

    # Set the path to your Firefox binary
    firefox_binary_path = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    gecko_driver_path = r'F:\ProgramFiles\drivefirefox\geckodriver.exe'
    base_url = "https://www.examtopics.com/discussions/google/view/"
    start_number = 137652 #118130  #104394 #101798###134280  #104143#131017 #130358 /105393
    end_number = start_number + 1000 # You can adjust the range as needed
    output_file = 'questions'
    # Set up the Firefox browser
    options = Options()
    options.binary_location = firefox_binary_path
    # options.add_argument('--headless')  # Comment this line to make the browser visible
    driver = webdriver.Firefox(executable_path=gecko_driver_path, options=options)

    #main_Doc(driver)
    botPreg(start_number, end_number, base_url, driver, output_file)
    # Close the browser window
    driver.quit()


if __name__ == "__main__":
    main()
