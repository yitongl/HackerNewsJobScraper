import urllib.request
import re
import webbrowser
from bs4 import BeautifulSoup
from functools import partial
import fire


class HNScraper(object):
    def __show_in_browser(self, results):
        output_file_path = '/tmp/jobs.html'
        with open(output_file_path, 'w+') as f:
            f.write("\n<hr>".join(results))

        webbrowser.open('file://' + output_file_path)

    def __get_comment_text(self, comment_html):
        return "\n".join(map(str, comment_html.span.contents))

    def __filter_attribute(self, attributes, comment):
        return any(re.search(attribute, comment, re.IGNORECASE) for attribute in attributes)

    def __filter_matches(self, comments_list, attributes):
        return filter(partial(self.__filter_attribute, attributes), comments_list)

    def scrape(self, url, locations=['new york'], occupations=['Data science', 'Data scientist']):

        html = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html, 'html.parser')

        comments = list(
            map(self.__get_comment_text, soup.find_all('div', class_='comment')))

        occupation_matches = self.__filter_matches(comments, occupations)

        location_occupation_matches = self.__filter_matches(
            occupation_matches, locations)

        results = list(location_occupation_matches)

        if (len(results) > 0):
            self.__show_in_browser(results)
        else:
            print('No results')


if __name__ == '__main__':
    fire.Fire(HNScraper)
