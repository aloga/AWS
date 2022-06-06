{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled37.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyNtbCHfzlsFFKF7S7yX4kgR",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/aloga/AWS/blob/main/Prime_Number.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Is it a prime number?\n"
      ],
      "metadata": {
        "id": "f1jEdCBAAS3b"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2GgU0g2TAPNu",
        "outputId": "e4fb1401-f911-48d6-e805-440a09923a3c"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a positive number to check if it is a Prime Number : 19\n",
            "19  is a Prime Number\n"
          ]
        }
      ],
      "source": [
        "n = int(input(\"Enter a positive number to check if it is a Prime Number : \"))\n",
        "counter = 0\n",
        "\n",
        "for i in range(1, n+1):\n",
        "    if n % i == 0:\n",
        "        counter += 1\n",
        "\n",
        "if (n == 0) or (n == 1) or (counter >= 3):\n",
        "    print(n, \" is not a Prime Number\")\n",
        "\n",
        "else:\n",
        "    print(n, \" is a Prime Number\")\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "digit1 = input(\"Enter a number : \")\n",
        "while not digit1.isdigit():\n",
        "    print(\"You must enter the number you entered as digits\")\n",
        "    digit1 = int(input(\"Enter a number : \"))\n",
        "    break\n",
        "dgt = int(digit1)\n",
        "if (dgt == 1) or (dgt == 0):\n",
        "    print(\"The number\", dgt,\n",
        "          \"is not a prime number. The smallest prime number is considered to be 2.\")\n",
        "else:\n",
        "    for i in range(2, dgt):\n",
        "        if (dgt % i != 0) and (dgt > 1):\n",
        "            print(\"Hello, the number you entered is \",\n",
        "                  digit1, \"and that is prime number.\")\n",
        "        else:\n",
        "            print(\"Opppss, the number you entered is \",\n",
        "                  digit1, \"and that is not prime number\")\n",
        "        break\n"
      ],
      "metadata": {
        "id": "j8CQ0lSpAQbc"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "number = int(input(\"Enter any number: \"))\n",
        "\n",
        "if number > 1:\n",
        "\n",
        "    for i in range(2, number):\n",
        "\n",
        "        if (number % i) == 0:\n",
        "\n",
        "            print(number, \"is not a prime number\")\n",
        "\n",
        "            break\n",
        "\n",
        "    else:\n",
        "\n",
        "        print(number, \"is a prime number\")\n",
        "\n",
        "else:\n",
        "\n",
        "    print(number, \"is not a prime number\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xpy8S2yiA7Fa",
        "outputId": "0992fd24-f939-498d-dd02-84e2a4f72a02"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter any number: 2\n",
            "2 is a prime number\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "6zWMc_UnBMII"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}