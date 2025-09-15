#!/bin/zsh

function pycalc() {
    if [ -z "$1" ]; then
        echo "Usage: pycalc --init | --new <filename>"
        return 1
    elif [ $1 = "--init" ]; then
        echo "Initializing a new PyCalc project..."

        python -m venv ./PyCalcEnv
        
        echo "Downloading requirements.txt..."
        
        mkdir ./.temp

        wget -O ./.temp/requirements.txt "https://raw.githubusercontent.com/ismager7878/PyCalc/refs/heads/main/requirement.txt"
        
        source ./PyCalcEnv/bin/activate

        pip install -r ./.temp/requirements.txt

        rm ./.temp/requirements.txt
        rmdir ./.temp

        echo "PyCalc project initialized successfully."

        return 0
    elif [ $1 = "--new" ]; then
        if [ -z "$2" ]; then
            echo "Usage: pycalc --new <filename>"
            return 1
        fi

        echo "Creating a new PyCalc file: $2"

        wget -O ./$2.py "https://raw.githubusercontent.com/ismager7878/PyCalc/refs/heads/main/Template.py"

        echo "New PyCalc file created successfully."

        return 0

    elif [ $1 = "--examples" ]; then
        echo "Example usages of PyCalc:"
        curl "https://raw.githubusercontent.com/ismager7878/PyCalc/refs/heads/main/Example.py"

    
    elif [ $1 = "--help" ]; then
        echo "PyCalc - A simple calculator project initializer and file creator."
        echo ""
        echo "Usage:"
        echo "  pycalc --init            Initialize a new PyCalc project."
        echo "  pycalc --new <filename>  Create a new PyCalc file with the specified filename."
        echo "  pycalc --examples        Display example usages."
        echo "  pycalc --help            Display this help message."
        return 0
    else
        echo "Unknown option: $1"
        echo "Usage: pycalc --init | --new <filename> | --help"
        return 1
    fi
}