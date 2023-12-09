import subprocess

def execute_script(script_name):
    try:
        subprocess.run(['python', script_name])
    except FileNotFoundError:
        print(f"Error: {script_name} not found.")

if __name__ == "__main__":
    user_choice = input("Enter '1' for Sender, or '0' for Receiver: ")

    if user_choice == '1':
        execute_script('Sender.py')

    else:
        execute_script('Receiver.py')
