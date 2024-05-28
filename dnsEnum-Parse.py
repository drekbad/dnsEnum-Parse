#!/usr/bin/python3

import argparse

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('-i', '--input', required=True, help='Input file')
  parser.add_argument('-o', '--output', required=True, help='Output file')
  parser.add_argument('-d', '--domain', required=True, help='Domain to search for')
  args = parser.parse_args()

  subdomains = set()

  with open(args.input, 'r') as infile:
    for line in infile:
      if '|' in line:
        subdomain = line.split('|')[0].strip()
        if subdomain and subdomain != args.domain:
          fqdn = f"{subdomain.lower()}.{args.domain.lower()}"
          subdomains.add(fqdn)

    unique_subdomains = sorted(subdomains)

    with open(args.output, 'w') as outfile:
      for subdomain in unique_subdomains:
        outfile.write(subdomain + '\n')

if __name__ == '__main__':
  main()
