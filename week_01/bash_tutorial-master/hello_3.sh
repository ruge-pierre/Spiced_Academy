#!/bin/bash
declare -a StringArray=("Hello World!" "Hi" "Hallo" "Bonjour" "Hola" "Konnichi wa" "Salve" "Salut" "Merhaba" "Hoi")

for ((i = 0; i < $1; i++));  do
  echo ${StringArray[$i]}
done
