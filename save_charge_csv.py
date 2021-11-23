import csv
all_links = []

# Save
with open('all_ads_links.csv', 'w') as f:
    # using csv.writer method from CSV package
    csv.writer(f, delimiter='\n').writerow(all_links)


# Charge
with open('all_ads_links.csv', newline='') as f:
    all_links = list(csv.reader(f))
all_links = [item for sublist in all_links for item in sublist]

