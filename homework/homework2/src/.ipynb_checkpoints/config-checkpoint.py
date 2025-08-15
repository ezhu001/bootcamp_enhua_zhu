{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "d1c3e9e9-ed06-4799-ba3c-e8ba3ec47933",
   "metadata": {},
   "outputs": [],
   "source": [
    "from dotenv import load_dotenv\n",
    "import os\n",
    "\n",
    "def load_env():\n",
    "    load_dotenv()\n",
    "\n",
    "def get_key(key_name):\n",
    "    return os.getenv(key_name)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
