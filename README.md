# HackAssembler - Nand2Tetris Project

This is a Hack assembler designed for the Nand2Tetris course. The assembler translates assembly language code written in the Hack assembly language into binary code that can be executed on the Hack computer, a simplified computer architecture introduced in the Nand2Tetris course.

## Table of Contents

- [Introduction](#introduction)
- [Usage](#usage)
- [Features](#features)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Debugging (Optional)](#debugging-optional)
- [License](#license)

## Introduction

The HackAssembler project is part of the Nand2Tetris course, which aims to build a modern computer system from first principles. The assembler takes Hack assembly code and converts it into binary machine code. This machine code can be executed on the Hack hardware platform, allowing you to write and run software for the computer you've built from the ground up.

## Usage

To use the HackAssembler, follow the command format below:

In Unix or Linux systems:
```bash
hack-asm.sh <file.asm> [-debug (optional)]
```

In Windows systems:
```bat
hack-asm <file.asm> [-debug (optional)]
```

- `<file.asm>`: The path to the Hack assembly code file that you want to assemble.
- `-debug` (optional): Use this flag to enable debugging mode. This will provide additional information during the assembly process.

## Features

- Converts Hack assembly language to binary code.
- Easy-to-use command-line interface.
- Optional debugging mode for detailed information during assembly.

## Installation

1. Clone the repository:

```bash
git clone hack-assembler.git
```

2. Change into the project directory:

```bash
cd hack-assembler
```

3. Install any dependencies (if applicable) using your preferred package manager.

4. Build the project (if necessary).

## Getting Started

1. Ensure you have a Hack assembly code file (e.g., `my_program.asm`) that you want to assemble.

2. Open your terminal and navigate to the directory where you cloned the HackAssembler project.

3. Run the assembler with your Hack assembly code (In Windows):

```bat
hack-asm my_program.asm
```

4. The assembler will generate a binary output file (e.g., `my_program.hack`) in the same directory.

5. You can now load and execute the generated binary code on the Hack computer.

## Debugging (Optional)

If you want more detailed information during the assembly process, you can use the `-debug` flag (In Windows):

```bat
hack-asm my_program.asm -debug
```

This will provide additional output to help you identify and resolve any issues in your assembly code.

## License

This project is licensed under the NSS License - see the [LICENSE.md](LICENSE.md) file for details.