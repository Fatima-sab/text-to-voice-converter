{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "gpuType": "T4",
      "authorship_tag": "ABX9TyO4CFeIbRlhvHha/NejcCs7",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    },
    "accelerator": "GPU"
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Fatima-sab/text-to-voice-converter/blob/main/app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "pip install gTTS"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GBnkoX8gD2hh",
        "outputId": "576a1cf1-d0a8-48b3-f086-536fa60074b6"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting gTTS\n",
            "  Downloading gTTS-2.5.3-py3-none-any.whl.metadata (4.1 kB)\n",
            "Requirement already satisfied: requests<3,>=2.27 in /usr/local/lib/python3.10/dist-packages (from gTTS) (2.32.3)\n",
            "Requirement already satisfied: click<8.2,>=7.1 in /usr/local/lib/python3.10/dist-packages (from gTTS) (8.1.7)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->gTTS) (3.4.0)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->gTTS) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->gTTS) (2.2.3)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->gTTS) (2024.8.30)\n",
            "Downloading gTTS-2.5.3-py3-none-any.whl (29 kB)\n",
            "Installing collected packages: gTTS\n",
            "Successfully installed gTTS-2.5.3\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from gtts import gTTS\n",
        "import os\n",
        "\n",
        "# Text you want to convert to speech\n",
        "text = \"Hello, this is a sample text to convert into audio using Python.\"\n",
        "\n",
        "# Language for the text-to-speech conversion (English here)\n",
        "language = 'en'\n",
        "\n",
        "# Create gTTS object\n",
        "tts = gTTS(text=text, lang=language, slow=False)  # slow=False means high speed\n",
        "\n",
        "# Save the speech to a file\n",
        "audio_file = \"output_audio.mp3\"\n",
        "tts.save(audio_file)\n",
        "\n",
        "# Optionally, play the audio file (for systems with an audio player)\n",
        "os.system(f\"start {audio_file}\")  # For Windows\n",
        "# os.system(f\"xdg-open {audio_file}\")  # For Linux\n",
        "# os.system(f\"open {audio_file}\")  # For macOS\n",
        "\n",
        "print(f\"Audio file saved as {audio_file}\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EWfjKXzAD-M_",
        "outputId": "56f1df97-59ab-4d32-dca3-c5bde84b066e"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Audio file saved as output_audio.mp3\n"
          ]
        }
      ]
    }
  ]
}