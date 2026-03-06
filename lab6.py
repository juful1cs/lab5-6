{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fc6e4288-c9bd-44cc-9f16-b4f2a9695736",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Question 1\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter number:  10\n",
      "Enter number:  5.5\n",
      "Enter number:  7\n",
      "Enter number:  12\n",
      "Enter number:  3.2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sum: 37.7\n",
      "Average: 7.540000000000001\n",
      "Max: 12.0\n",
      "Min: 3.2\n",
      "\n",
      "Question 2\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter word:  apple\n",
      "Enter word:  banana\n",
      "Enter word:  orange\n",
      "Enter word:  mango\n",
      "Enter word:  pear\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "First word: apple\n",
      "Last word: pear\n",
      "Total words: 5\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter word to search:  banana\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Word found\n",
      "\n",
      "Question 3\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter student name:  Ali\n",
      "Enter score:  90\n",
      "Enter student name:  Sara\n",
      "Enter score:  85\n",
      "Enter student name:  Omar\n",
      "Enter score:  95\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Students and scores:\n",
      "Ali : 90.0\n",
      "Sara : 85.0\n",
      "Omar : 95.0\n",
      "Highest score student: Omar\n",
      "\n",
      "Question 4\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter numbers for list1 separated by space:  1 2 3 4\n",
      "Enter numbers for list2 separated by space:  3 4 5 6\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Union: {1, 2, 3, 4, 5, 6}\n",
      "Intersection: {3, 4}\n",
      "Difference: {1, 2}\n",
      "\n",
      "Question 5\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter name:  Ali\n",
      "Enter name:  Sara\n",
      "Enter name:  Omar\n"
     ]
    }
   ],
   "source": [
    "# -------- Question 1 --------\n",
    "print(\"Question 1\")\n",
    "\n",
    "numbers = []\n",
    "\n",
    "for i in range(5):\n",
    "    num = float(input(\"Enter number: \"))\n",
    "    numbers.append(num)\n",
    "\n",
    "print(\"Sum:\", sum(numbers))\n",
    "print(\"Average:\", sum(numbers)/len(numbers))\n",
    "print(\"Max:\", max(numbers))\n",
    "print(\"Min:\", min(numbers))\n",
    "\n",
    "\n",
    "# -------- Question 2 --------\n",
    "print(\"\\nQuestion 2\")\n",
    "\n",
    "words = []\n",
    "\n",
    "for i in range(5):\n",
    "    w = input(\"Enter word: \")\n",
    "    words.append(w)\n",
    "\n",
    "words_tuple = tuple(words)\n",
    "\n",
    "print(\"First word:\", words_tuple[0])\n",
    "print(\"Last word:\", words_tuple[-1])\n",
    "print(\"Total words:\", len(words_tuple))\n",
    "\n",
    "search = input(\"Enter word to search: \")\n",
    "\n",
    "if search in words_tuple:\n",
    "    print(\"Word found\")\n",
    "else:\n",
    "    print(\"Word not found\")\n",
    "\n",
    "\n",
    "# -------- Question 3 --------\n",
    "print(\"\\nQuestion 3\")\n",
    "\n",
    "students = {}\n",
    "\n",
    "for i in range(3):\n",
    "    name = input(\"Enter student name: \")\n",
    "    score = float(input(\"Enter score: \"))\n",
    "    students[name] = score\n",
    "\n",
    "print(\"Students and scores:\")\n",
    "for name, score in students.items():\n",
    "    print(name, \":\", score)\n",
    "\n",
    "top_student = max(students, key=students.get)\n",
    "\n",
    "print(\"Highest score student:\", top_student)\n",
    "\n",
    "\n",
    "# -------- Question 4 --------\n",
    "print(\"\\nQuestion 4\")\n",
    "\n",
    "list1 = input(\"Enter numbers for list1 separated by space: \")\n",
    "list2 = input(\"Enter numbers for list2 separated by space: \")\n",
    "\n",
    "set1 = set(map(int, list1.split()))\n",
    "set2 = set(map(int, list2.split()))\n",
    "\n",
    "print(\"Union:\", set1 | set2)\n",
    "print(\"Intersection:\", set1 & set2)\n",
    "print(\"Difference:\", set1 - set2)\n",
    "\n",
    "\n",
    "# -------- Question 5 --------\n",
    "print(\"\\nQuestion 5\")\n",
    "\n",
    "names = []\n",
    "\n",
    "for i in range(5):\n",
    "    n = input(\"Enter name: \")\n",
    "    names.append(n)\n",
    "\n",
    "names_tuple = tuple(names)\n",
    "\n",
    "print(\"Tuple:\", names_tuple)\n",
    "\n",
    "name_length_dict = {}\n",
    "\n",
    "for name in names:\n",
    "    name_length_dict[name] = len(name)\n",
    "\n",
    "print(\"Dictionary:\", name_length_dict)\n",
    "\n",
    "length_set = set(name_length_dict.values())\n",
    "\n",
    "print(\"Unique name lengths:\", length_set)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "507f7ee6-bab0-4dca-9b9d-d126964fd997",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
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
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
