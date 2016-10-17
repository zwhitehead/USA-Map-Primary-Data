"""this file determines USA county's primary election votes and creates new svg files with color-coded counties based on votes"""
import csv
from bs4 import BeautifulSoup

def main():
    '''this function calls the results() function'''
    results()


def results():
    """this function sorts the winners for each county and color coordinates on each new map"""
    rep_county = {}
    dem_county = {}
    with open('primary_results.csv', newline='') as csvfile:  # open the file
        csv_reader = csv.reader(csvfile, delimiter=",")  # create the reader object
        next(csv_reader, None)

        for row in csv_reader:  # loop through each row
            if row[4] == 'Democrat' and float(row[7]) > 0.5:  # find democratic winner for each county
                if row[5] == 'Hillary Clinton':
                    dem_county[row[3].rstrip('0').rstrip('.').zfill(5)] = row[5]
                if row[5] == 'Bernie Sanders':
                    dem_county[row[3].rstrip('0').rstrip('.').zfill(5)] = row[5]

            if row[4] == 'Republican' and float(row[7]) > 0.5:  # find republican winner for each county
                if row[5] == 'Donald Trump':
                    rep_county[row[3].rstrip('0').rstrip('.').zfill(5)] = row[5]
                if row[5] == 'Ted Cruz':
                    rep_county[row[3].rstrip('0').rstrip('.').zfill(5)] = row[5]
                if row[5] == 'John Kasich':
                    rep_county[row[3].rstrip('0').rstrip('.').zfill(5)] = row[5]
                if row[5] == 'Marco Rubio':
                    rep_county[row[3].rstrip('0').rstrip('.').zfill(5)] = row[5]
                if row[5] == 'Ben Carson':
                    rep_county[row[3].rstrip('0').rstrip('.').zfill(5)] = row[5]

        for key in sorted(rep_county):  # place republican winners in dictionary
            print(key, ':', rep_county[key])

        for key in sorted(dem_county):  # place democratic winners in dictionary
            print(key, ':', dem_county[key])


        with open('counties.svg', 'r') as fin:
            svg_data = fin.read()
            soup = BeautifulSoup(svg_data, "html.parser")
            paths = soup.findAll('path')

            for p in paths:
            # handle all the id's in the .svg file, but leave the
            # "State_Lines" and "separator" paths alone.
                if p['id'] not in ["State_Lines", "separator"]:  # creates new style for each candidate

                    new_path_style = 'font-size:12px;fill-rule:nonzero;stroke:#000000;stroke-opacity:1;' \
                                     'stroke-width:0.1;stroke-miterlimit:4;stroke-dasharray:none;stroke-linecap:' \
                                     'butt;marker-start:none;stroke-linejoin:bevel;fill:'

                    dem_colors = ['#de2d26', '#fee0d2']
                    rep_colors = ['#253494', '#2c7fb8', '#41b6c4', '#a1dab4', '#ffffcc']
                    missing_colors = ['#cccccc']

                    p['style'] = new_path_style

                    if p['id'] in dem_county:  # replace democratic counties with correct fill color
                        if row[5] == 'Hillary Clinton':
                            p['style'] += dem_colors[0].strip()
                        elif row[5] == 'Bernie Sanders':
                            p['style'] += dem_colors[1].strip()
                        else:
                            p['style'] += missing_colors[0].strip()

                    with open('democrat_map.svg', mode='w') as out_svg:  # creates new svg file with updated colors
                        print(soup.prettify(), file=out_svg)

                    if p['id'] in rep_county:  # replace republican counties with correct fill color
                        if row[5] == 'Donald Trump':
                            p['style'] += rep_colors[0].strip()
                        elif row[5] == 'Ted Cruz':
                            p['style'] += rep_colors[1].strip()
                        elif row[5] == 'John Kasich':
                            p['style'] += rep_colors[2].strip()
                        elif row[5] == 'Marco Rubio':
                            p['style'] += rep_colors[3].strip()
                        elif row[5] == 'Ben Carson':
                            p['style'] += rep_colors[4].strip()
                        else:
                            p['style'] += missing_colors[0].strip()

                    with open('republican_map.svg', mode='w') as out_svg:  # creates new svg file with updated colors
                        print(soup.prettify(), file=out_svg)


if __name__ == '__main__':
    main()