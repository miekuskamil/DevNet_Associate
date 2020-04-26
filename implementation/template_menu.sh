#!/bin/bash

echo "" > template_input.csv
clear
cat template_list.txt
echo -ne "\n"
read  -p "Choose template from list above: " template
echo -ne "\n"
clear

echo -ne "Paste CSV file content and finish with Ctrl+D\n"
arr=()
while IFS= read -r l; do
    arr+=( "$l" )
done
printf '%s\n' "${arr[@]}" > template_input.csv

ansible-playbook template_generator.yml --extra-vars "source=$template"

sleep 1
echo -ne "\n"

while true; do
    read  -p "Do you wish to see variable file now? Yy/Nn: " yn
    case $yn in
        [Yy]* ) cat roles/$template/vars/main.yml; break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done

rm template_input.csv
