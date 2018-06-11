#!/bin/bash
# A HANGMAN GAME 
#
#This programme read list of words and make you guess which word from list it chose
#
#Author: Zuzanna Kazior
#Date:  May 2018
#

declare -a word
declare -a word_img
declare -a alpha_img
i=0
incorrect=0
wordindex=0
correct=0
char=0
alpha=("a" "b" "c" "d" "e" "f" "g" )

function putWordsToArray {
	exec 3<&0
	exec 0<dict.dat

	while read LINE
	do

	word[i] =$LINE
	i=`expr $i +1`
	done
	exec 0<&3
}

function wrong1  {
	echo
	echo "		O			"
	echo
	echo
	echo
	echo
	echo
	echo
}

function wrong2  {
	echo
	echo "		O			"
	echo "		|			"
	echo
	echo
	echo
	echo
	echo
}

function wrong3  {
	echo
	echo "		 O			"
	echo "		/|			"
	echo
	echo
	echo
	echo
	echo
}

function wrong4  {
	echo
	echo "		 O			"
	echo "		/|\			"
	echo
	echo
	echo
	echo
	echo
}

function wrong5  {
	echo
	echo "		 O			"
	echo "		/|\			"
	echo "		/			"
	echo
	echo
	echo
	echo
}

function wrong6  {
	echo
	echo "		 O			"
	echo "		/|\			"
	echo "		/ \			"
	echo
	echo
	echo
	echo
}

function wrong7  {
	echo "		  ________	"
	echo "		 |	   	 |	"
	echo "		 O	     |	"
	echo "		/|\	     |	"
	echo "		/ \	     |	"
	echo "	    _________|__"
	echo
	echo
	echo " 		GAME OVER 		"
}

function init() {
	clear

	filename="movies.txt"

	echo
	display

	menu
}

function menu() {
#    exec 2> /dev/null

    title="Main Menu"
    prompt="Pick an option:"
    options=("Play the game" "Choose topic" "Exit")

    echo "$title"
    PS3="$prompt "
    select opt in "${options[@]}"; do

    case "$REPLY" in

    1 ) main;;
    2 ) choice;;
    3 ) exit;;

    $(( ${#options[@]}+1 )) ) echo "Goodbye!"; break;;
    *) echo "Invalid option. Try another one.";continue;;

    esac

    done

    echo

}

function choice() {

    title="Categories"
    prompt="Pick an option:"
    options=("Movies" "English words" "Go back")

    echo "$title"
    PS3="$prompt "
    select opt in "${options[@]}"; do

    case "$REPLY" in

    1 ) filename="movies.txt";;
    2 ) filename="english-words.txt";;
    4 ) menu;;

    $(( ${#options[@]}+1 )) ) echo "Goodbye!"; break;;
    *) echo "Invalid option. Try another one.";continue;;

    esac
    menu
    done
}

function play_again() {
	echo
	echo -n "Would you like to play again ? (y/n)  "
	read -n 1 choice 
	
	case $choice in 
	[yY]) clear
		main
	;;
	esac
	
	clear
	echo "See you next time!"

	tput cnorm
	exit 
}

function file_select() {
    filename=$(zenity --file-selection --title="Select a file")
    case $? in
        0)
        echo "\"$filename\" selected";;
        1)
        echo "No file selected" ;;
        -1)
        echo "Unexpected error occurred" ;;
    esac
}

function main() {
##The function used to read the word list
    read a < $filename

    randind=`expr $RANDOM % ${#a[@]}`

    movie=${a[$randind]}

    guess=()

    guesslist=()
    guin=0

    movie=`echo $movie | tr -dc '[:alnum:] \n\r' | tr '[:upper:]' '[:lower:]'`
    len=${#movie}

    for ((i=0;i<$len;i++)); do
        guess[$i]="_"
    done

    mov=()

    for ((i=0;i<$len;i++)); do
        mov[$i]=${movie:$i:1}
    # echo -n "${mov[$i]} "
    done

    for ((j=0;j<$len;j++)); do
    if [[ ${mov[$j]} == " " ]]; then
        guess[$j]=" "
    fi
    done

    ## Display the initial setup

    wrong=0

    while [[ $wrong -lt 7 ]]; do
        case $wrong in
            0)echo " "
            ;;
            1)wrong1
            ;;
            2)wrong2
            ;;
            3)wrong3
            ;;
            4)wrong4
            ;;
            5)wrong5
            ;;
            6)wrong6
            ;;
        esac

    if [[ wrong -eq 0 ]]; then
        for i in {1..7}
        do
            echo
        done
    fi

    notover=0
    for ((j=0;j<$len;j++)); do
        if [[ ${guess[$j]} == "_" ]]; then
            notover=1
        fi
    done

    echo Guess List: ${guesslist[@]}
    echo Wrong guesses: $wrong
    for ((k=0;k<$len;k++)); do
        echo -n "${guess[$k]} "
    done
    echo
    echo

    if [[ notover -eq 1 ]]; then
        echo -n "Guess a letter: "
        read -n 1 -e letter
        letter=$(echo $letter | tr [A-Z] [a-z])
        guesslist[$guin]=$letter
        guin=`expr $guin + 1`
    fi

    f=0;
    for ((i=0;i<$len;i++)); do
        if [[ ${mov[$i]} == $letter ]]; then
            guess[$i]=$letter
            f=1
        fi
    done
        if [[ f -eq 0 ]]; then
            wrong=`expr $wrong + 1`
        fi

        if [[ notover -eq 0 ]]; then
            echo
            echo You Win!
            echo $movie
            echo
            play_again
        fi
            clear
        done

    wrong7
    echo You lost!
    echo The word was: $movie
    play_again
}

function display() {
    echo " #     #    #    #     #  #####  #     #    #    #     # "
    echo " #     #   # #   ##    # #     # ##   ##   # #   ##    # "
    echo " #     #  #   #  # #   # #       # # # #  #   #  # #   # "
    echo " ####### #     # #  #  # #  #### #  #  # #     # #  #  # "
    echo " #     # ####### #   # # #     # #     # ####### #   # # "
    echo " #     # #     # #    ## #     # #     # #     # #    ## "
    echo " #     # #     # #     #  #####  #     # #     # #     # "
    echo
}




init





