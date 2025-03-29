# Social Media Application with Mini-Games

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)]()

A console-based social platform featuring user accounts and entertainment apps, demonstrating OOP principles and file handling in Python.

## Features
- 🔐 User authentication system
- 📝 Profile management
- 🎮 4 interactive games:
  - Arithmetic calculator
  - Tic-Tac-Toe (2-player)
  - Hangman (word guessing)
  - Timed math quiz

## System Architecture
```mermaid
graph TD
    A[Main Menu] --> B[Auth System]
    A --> C[Game Launcher]
    B --> D[User Profiles]
    C --> E[Calculator]
    C --> F[Tic-Tac-Toe]
    C --> G[Hangman]
    C --> H[Math Quiz]
