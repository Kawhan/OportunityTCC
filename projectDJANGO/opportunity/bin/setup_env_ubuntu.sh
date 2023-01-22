python3 -m venv venv
activate () {
    source venv/bin/activate.fish
    echo "install requirements to virtual environment"
    pip install -r requirements.txt
}