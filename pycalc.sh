#!/bin/zsh

function pycalc() {
    if [ $! -eq 0 ]; then
        echo "Usage: pycalc --init | --new <filename>"
        return 1
    elif [ $1 = "-init" ]; then
        echo "Initializing a new PyCalc project..."
        python -m venv ./PyCalcEnv

        wget -O ./.temp/requirements.txt "https://raw.githubusercontent.com/ismager7878/PyCalc/refs/heads/main/requirement.txt"
        
        source ./PyCalcEnv/bin/activate

        pip install -r requirements.txt

        rm ./.temp/requirements.txt
        rmdir ./.temp

        echo "PyCalc project initialized successfully."

        return 0
    fi
}