# PsychoPy Installation and Experiment Setup

This experiment was coded using **Python 3.10**, and the following instructions outline how to install it and run **PsychoPy 2024.2.5**.  

## Installing Python 3.10  

PsychoPy requires **Python 3.8 or 3.10**. This guide uses **Python 3.10.16**.  

### **MacOS Installation**  
Open the terminal and run:  
```sh
brew install python@3.10
```
> For assistance on installing brew, refer to this [guide](https://builtin.com/articles/install-homebrew#:~:text=7%20Steps%20to%20Install%20Homebrew,Verify%20Installation)

### **Windows Installation**  
Python **3.10.16** must be installed manually from the [official Python website](https://www.python.org/downloads/release/python-31016/).  

---

## Setting Up a Virtual Environment  
It is recommended to use a **virtual environment** to avoid conflicts with dependencies.  

### **Create a virtual environment**  
Navigate to the directory where you want the environment and run:  
```sh
python3.10 -m venv name_of_env
```

### **Activate the virtual environment**  
Once created, activate the environment:  
```sh
source name_of_env/bin/activate
```
You should now see the name of your environment on the left side of your terminal prompt.  

> **Note:** Ensure you are in the directory where you created the virtual environment before activating it.  

---

## Installing PsychoPy Dependencies  

### **Fix `wxPython` dependency**  
Run the following commands inside your virtual environment:  
```sh
pip uninstall wxPython
pip install wxPython==4.2.1
```

### **Install PsychoPy**  
Now, install **PsychoPy**:  
```sh
pip install psychopy
```

### **Verify Installation**  
To confirm PsychoPy is installed, run:  
```sh
psychopy --version
```
If installed correctly, this command should return the PsychoPy version.

---

## Running the `foraging.py` Experiment  

1. **Clone the repository** or download it as a ZIP.  
2. **Activate your virtual environment** using the `source` command:  
   ```sh
   source name_of_env/bin/activate
   ```
3. **Navigate to the experiment directory**:  
   ```sh
   cd /experiment/run_exp
   ```
4. **Run the experiment**:  
   ```sh
   python3 foraging.py <participant_id>
   ```


>**Note:** If you wish to force exit the PsychoPy terminal on Linux press option + cmd + esc. Otherwise please ensure there is a way to close the experiment window when debugging such as removing the fullscreen toggle in the code.  

---

## Questions  
If you have any questions about the code or installation, please contact me at rapalsul@uci.edu  
