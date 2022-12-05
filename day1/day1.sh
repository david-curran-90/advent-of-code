#!/bin/bash

elves=()

cal=0
while IFS= read -r l; do
  if [[ $l != "" ]]; then
    cal=$((cal + l))
  else
    elves+=("$cal")
    cal=0
  fi
done < input.txt

#echo "${elves[*]}" | sort -n
top=$(IFS=$'\n' sort <<<"${elves[*]}" | sort -n -r | head -1)

echo "Top elf has $top calories in their bag"

three=$(IFS=$'\n' sort <<<"${elves[*]}" | sort -n -r | head -3)

topthree=0
for n in $three; do
   topthree=$(( topthree + n ))
done

echo $topthree
