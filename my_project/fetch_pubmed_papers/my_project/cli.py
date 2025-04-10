import re
import csv
from datetime import datetime
from Bio import Entrez
import argparse

Entrez.email = "mrinalk1361@gmail.com"  

COMPANY_KEYWORDS = [ "pharma", "biotech", "therapeutics", "biosciences", "pharmaceutical",
    "inc", "corp", "ltd", "llc", "gmbh", "s.a.", "co.", "company"]

def is_company_affiliation(affiliation):
    return any(keyword.lower() in affiliation.lower() for keyword in COMPANY_KEYWORDS)

def extract_paper_details(pmid, debug=False):
    handle = Entrez.efetch(db="pubmed", id=pmid, rettype="medline", retmode="text")
    record = handle.read()
    handle.close()

    title_match = re.search(r"TI  - (.+)", record)
    date_match = re.search(r"DP  - (.+)", record)
    authors = re.findall(r"FAU - (.+)", record)
    affiliations = re.findall(r"AD  - (.+)", record)
    emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", record)

    company_affiliations = [aff for aff in affiliations if is_company_affiliation(aff)]
    non_academic_authors = authors if company_affiliations else []

    if debug:
        print(f"[DEBUG] PMID: {pmid}")
        print(f"[DEBUG] Title: {title_match.group(1) if title_match else 'N/A'}")
        print(f"[DEBUG] Authors: {authors}")
        print(f"[DEBUG] Affiliations: {affiliations}")
        print(f"[DEBUG] Emails: {emails}")

    return {
        "PubmedID": pmid,
        "Title": title_match.group(1) if title_match else "N/A",
        "Publication Date": date_match.group(1) if date_match else "N/A",
        "Non-academic Author(s)": "; ".join(non_academic_authors),
        "Company Affiliation(s)": "; ".join(company_affiliations),
        "Corresponding Author Email": emails[0] if emails else "N/A"
    }

def fetch_papers(query, retmax=20, debug=False):
    handle = Entrez.esearch(db="pubmed", term=query, retmax=retmax)
    results = Entrez.read(handle)
    handle.close()

    pmids = results["IdList"]
    if debug:
        print(f"[DEBUG] Found {len(pmids)} papers.")

    final_data = []
    for pmid in pmids:
        data = extract_paper_details(pmid, debug)
        if data["Company Affiliation(s)"]:
            final_data.append(data)
    return final_data

def parse_args():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers with at least one non-academic author.")
    parser.add_argument("query", help="Search query (use PubMed syntax)")
    parser.add_argument("-d", "--debug", action="store_true", help="Print debug info")
    parser.add_argument("-f", "--file", help="Output CSV filename")
    return parser.parse_args()

def main():
    args = parse_args()
    data = fetch_papers(args.query, debug=args.debug)

    if args.file:
        with open(args.file, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        print(f"Saved {len(data)} papers to {args.file}")
    else:
        for row in data:
            print(row)

def entry_point():
    main()
